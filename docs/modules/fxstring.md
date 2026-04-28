# fxString — String Manipulation

Advanced text manipulation, regex, hashing, validation, encoding, similarity algorithms, and Spanish NLP.

## Submodules

| Submodule | Purpose |
|-----------|---------|
| [`string_operations`](../reference/fxString/string_operations.md) | Core string operations (search, replace, split, join) |
| [`string_caseconv`](../reference/fxString/string_caseconv.md) | Case conversions (camelCase, snake_case, title, etc.) |
| [`string_compression`](../reference/fxString/string_compression.md) | String compression/decompression |
| [`string_convertions`](../reference/fxString/string_convertions.md) | String-to-type conversions |
| [`string_encoding`](../reference/fxString/string_encoding.md) | Base64, URL, HTML encoding/decoding |
| [`string_evaluations`](../reference/fxString/string_evaluations.md) | String analysis and evaluation |
| [`string_format`](../reference/fxString/string_format.md) | String formatting utilities |
| [`string_hashing`](../reference/fxString/string_hashing.md) | Hash generation (MD5, SHA, etc.) |
| [`string_regex`](../reference/fxString/string_regex.md) | Regular expression utilities |
| [`string_similarity`](../reference/fxString/string_similarity.md) | String similarity algorithms (Levenshtein, Jaro-Winkler, etc.) |
| [`string_spanish`](../reference/fxString/string_spanish.md) | Spanish language processing (NIF, NIE, CIF validation) |
| [`string_spellcheck`](../reference/fxString/string_spellcheck.md) | Spell checking utilities |
| [`string_validations`](../reference/fxString/string_validations.md) | Input validation (email, URL, phone, etc.) |

## Quick Examples

```python
from shortfx.fxString import string_operations, string_validations

# Find substring positions
text = "Programming is fun, programming is great"
positions = string_operations.position_in_string(text, "is")  # [13, 36]

# Validate an email address
is_valid = string_validations.is_valid_email("user@example.com")  # True
```

!!! tip "Spanish NLP"
    The `string_spanish` submodule includes specialized functions for validating Spanish identity documents (NIF, NIE, CIF) and other locale-specific text processing.
