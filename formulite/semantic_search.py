"""Semantic search engine for FormuLite tool discovery.

Uses fastembed to generate vector embeddings of tool descriptions at
startup, then performs cosine-similarity search to match natural-language
queries against the function catalogue — even across languages.

No external numerical libraries are required at runtime; vector
operations use only the Python standard library (``math``).

Example:
    >>> from formulite.semantic_search import SemanticToolSearch
    >>> engine = SemanticToolSearch(tool_schemas)
    >>> results = engine.search("calculate compound interest", top_k=5)
    >>> results[0]["name"]
    'fxNumeric.finance_functions.compound_interest'

Complexity:
    - Index build: O(n) embeddings where n = number of tools.
    - Search: O(n) cosine comparisons per query (brute-force, fine for <1000 tools).
"""

import math
from typing import Any, Optional

# Singleton model instance — loaded once, shared across searches.
_MODEL: Optional[Any] = None

# Default model: small, fast, good multilingual support via ONNX.
DEFAULT_MODEL_NAME = "BAAI/bge-small-en-v1.5"


def _get_model(model_name: str = DEFAULT_MODEL_NAME) -> Any:
    """Lazy-load the fastembed TextEmbedding model.

    Automatically injects system SSL certificates via ``truststore``
    if available, to support corporate proxy environments.

    Args:
        model_name: HuggingFace model identifier for fastembed.

    Returns:
        A ``fastembed.TextEmbedding`` instance.

    Raises:
        ImportError: If fastembed is not installed.

    Complexity: O(1) after first call (cached singleton).
    """
    global _MODEL

    if _MODEL is not None:
        return _MODEL

    # Inject system SSL certs for corporate proxies (best-effort).
    try:
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass

    from fastembed import TextEmbedding

    _MODEL = TextEmbedding(model_name=model_name)

    return _MODEL


def _build_tool_text(schema: dict[str, Any]) -> str:
    """Build a rich text representation of a tool for embedding.

    Concatenates the tool name, description, and parameter info into a
    single string that captures the function's full semantic context.

    Args:
        schema: Tool schema dict with ``name``, ``description``, and
            ``parameters`` keys.

    Returns:
        A single text string optimised for embedding.

    Complexity: O(p) where p is the number of parameters.
    """
    parts: list[str] = []

    # Tool name — replace dots and underscores with spaces for tokenisation.
    name = schema.get("name", "")
    readable_name = name.replace(".", " ").replace("_", " ")
    parts.append(readable_name)

    # Description.
    description = schema.get("description", "")

    if description:
        parts.append(description)

    # Parameter names and descriptions.
    properties = schema.get("parameters", {}).get("properties", {})

    for param_name, param_info in properties.items():
        param_text = param_name.replace("_", " ")
        param_desc = param_info.get("description", "")

        if param_desc:
            param_text += f": {param_desc}"

        parts.append(param_text)

    return ". ".join(parts)


class SemanticToolSearch:
    """Vector-based semantic search over FormuLite tool schemas.

    Builds an embedding index from tool schemas at construction time,
    then supports fast cosine-similarity queries.

    Args:
        tool_schemas: List of tool schema dicts (from ``get_tool_schemas()``).
        model_name: Fastembed model identifier. Defaults to
            ``BAAI/bge-small-en-v1.5``.

    Example:
        >>> from formulite.registry import get_tool_schemas
        >>> from formulite.semantic_search import SemanticToolSearch
        >>> engine = SemanticToolSearch(get_tool_schemas())
        >>> results = engine.search("convert temperature celsius fahrenheit")
        >>> results[0]["name"]
        'fxNumeric.conversion_functions.temperature_convert'

    Complexity: O(n) for construction, O(n) per search query.
    """

    def __init__(
        self,
        tool_schemas: list[dict[str, Any]],
        model_name: str = DEFAULT_MODEL_NAME,
    ) -> None:
        self._schemas = tool_schemas
        self._model = _get_model(model_name)
        self._embeddings: list[list[float]] = self._build_index()

    def _build_index(self) -> list[list[float]]:
        """Compute normalised embeddings for all tool schemas.

        Returns:
            A list of normalised embedding vectors.

        Complexity: O(n) embedding computations.
        """
        texts = [_build_tool_text(schema) for schema in self._schemas]
        raw = [list(vec) for vec in self._model.embed(texts)]

        # Normalise each vector for cosine similarity via dot product.
        matrix: list[list[float]] = []

        for vec in raw:
            norm = math.sqrt(sum(v * v for v in vec))
            norm = norm if norm > 0 else 1.0
            matrix.append([v / norm for v in vec])

        return matrix

    def search(
        self,
        query: str,
        top_k: int = 10,
        threshold: float = 0.3,
    ) -> list[dict[str, Any]]:
        """Find tools semantically similar to a natural-language query.

        Args:
            query: Free-text search query in any language the model
                supports (English works best with bge-small-en).
            top_k: Maximum number of results to return.
            threshold: Minimum cosine similarity score (0.0–1.0).
                Results below this are excluded.

        Returns:
            List of tool schema dicts sorted by relevance (best first).

        Example:
            >>> engine.search("round a number to 2 decimals", top_k=3)
            [{"name": "fxExcel.math_formulas.ROUND", ...}, ...]

        Complexity: O(n) cosine comparisons + O(k log k) sorting.
        """
        raw_embedding = list(self._model.embed([query]))[0]
        query_vec = list(raw_embedding)

        # Normalise query vector.
        norm = math.sqrt(sum(v * v for v in query_vec))

        if norm > 0:
            query_vec = [v / norm for v in query_vec]

        # Cosine similarity via dot product (vectors are pre-normalised).
        scored = []

        for i, emb in enumerate(self._embeddings):
            score = sum(a * b for a, b in zip(emb, query_vec))

            if score >= threshold:
                scored.append((score, i))

        # Sort descending by score and take top_k.
        scored.sort(key=lambda x: x[0], reverse=True)

        return [self._schemas[i] for _, i in scored[:top_k]]
