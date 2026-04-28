# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased][Unreleased]

---

## [0.3.1][0.3.1] — 2026-04-28

### Changed

- Rename PyPI package from `agentfx` to `shortfx` — the `agentfx` name was already taken on PyPI
- Rename import package directory `agentfx/` → `shortfx/`
- Update all internal imports, docs, examples, MCP config, and entry points

---

## [0.3.0][0.3.0] — 2026-04-23

Breaking rename release: PyPI package renamed from `formulite` to `agentfx` to avoid name conflict with existing PyPI project.

### Changed

- Rename PyPI package from `formulite` to `agentfx` to avoid name conflict with existing PyPI project
- Add PEP 561 `py.typed` marker file for typed package support
- Add `twine` to dev dependencies

---

## [0.2.2][0.2.2] — 2026-04-21

Documentation infrastructure release: add MkDocs Material site with auto-generated API reference and GitHub Pages deployment.

### Added

- Add MkDocs Material documentation site with auto-generated API reference via mkdocstrings
- Add GitHub Pages deployment workflow (`.github/workflows/docs.yml`)
- Add `docs` dependency group in `pyproject.toml` (mkdocs-material, mkdocstrings, gen-files, literate-nav, section-index)

### Fixed

- Add `pymdownx.emoji` extension for Material icons rendering in MkDocs

---

## [0.2.1][0.2.1] — 2026-04-16

Security hardening release: remove all `subprocess` usage, unsafe dispatch functions, and interactive I/O from library code. Add Python 3.10/3.11 compatibility fix and CI coverage enforcement.

### Security

- Remove `execute_os_command` function from `py_operations.py` — a function library must not execute OS commands
- Remove `subprocess`-based auto-installation from `string_similarity.py` — `_lazy_import` now only attempts `importlib.import_module` and logs install instructions on failure
- Add `_safe_factorial` with `_MAX_FACTORIAL=170` guard in `calculator_functions.py` to prevent DoS via expensive factorial computations
- Restrict `ast.Attribute` access in `apply_expression()` (`py_tools.py`) to safe built-in types (`str`, `int`, `float`, `bool`, `list`, `tuple`, `dict`, `set`) and block private attribute access (`_`-prefixed)
- Add `n > 170` upper-bound guard to `factorial()` and `multinomial_coefficient()` in `arithmetic_functions.py`, and to `poisson_probability()`, `erlang_pdf()`, `poisson_pmf()`, `multinomial_coefficient()` in `statistics_functions.py` — aligns with existing `_MAX_FACTORIAL=170` in `calculator_functions.py`
- Remove `CallByName()` — exposed unrestricted `getattr`/`setattr` on arbitrary objects via MCP
- Remove `MsgBox()` and `InputBox()` from `fxVBA/system_functions.py` — interactive I/O (`print`/`input`) has no place in a pure function library

### Fixed

- Add Python 3.10/3.11 compatibility shims for `itertools.batched` and `math.sumprod` in `py_itertools.py` (were Python 3.12+ only)

### Removed

- `execute_os_command()` from `fxPython.py_operations` (security: no OS command execution in a function library)
- `_is_uv_managed_environment()`, `_find_pyproject_dir()`, `_validate_package_name()`, `_install_library()` and all `subprocess` auto-install strategies from `fxString.string_similarity`
- `shortfx_AUTO_INSTALL` / `ALLOW_AUTO_INSTALL` environment variables (no longer needed — library never installs packages)
- `CallByName()` from `fxVBA.misc_functions` (unrestricted `getattr`/`setattr` dispatch not appropriate for a formula library)

### Changed

- `.gitignore` — add patterns for secrets, credentials, IDE, OS, database files
- CI (`ci.yml`) — add `pytest-cov` with `--cov-fail-under=80`, `uv lock --check`, and `pip-audit` steps
- `pyproject.toml` — add `pytest-cov>=6.0.0` to dev dependencies

---

## [0.2.0][0.2.0] — 2026-04-13

Massive architecture overhaul: introduce `auto_export` dynamic re-export system, shared validators, AI agent integration layer (registry + MCP server + semantic search), and expand the library from ~580 to 3 000+ functions. All `fx*` packages now use `_loader.auto_export()`. The `fxNumeric` module is reorganised from 6 files into 30+ domain-specific submodules. New `fxString` submodules for encoding, hashing, compression, regex, and case conversion. All existing modules receive significant function additions and improved docstrings with Google-style format.

**60 tracked files changed** | +80 258 −10 625 lines | **~40 new untracked files**

### Added

#### Core Infrastructure

- `shortfx/_loader.py` — Central `auto_export()` dynamic re-export helper; all `fx*/__init__.py` files now delegate to it (40 lines)
- `shortfx/_validators.py` — Shared input validation (`ensure_type`, `ensure_numeric`, `ensure_positive`, `ensure_non_negative`, `ensure_in_range`, `ensure_not_empty`) replacing ad-hoc `isinstance` checks (104 lines)
- `shortfx/registry.py` — Automatic function discovery, OpenAI-compatible JSON Schema generation (`get_tool_schemas`), invocation dispatcher (`invoke_tool`), and keyword/semantic search (`search_tools`) (360 lines)
- `shortfx/semantic_search.py` — `SemanticToolSearch` class using fastembed embeddings for natural-language function discovery (157 lines)
- `shortfx/__main__.py` — CLI entry point for `python -m shortfx` (3 lines)

#### MCP Server (AI Agent Integration)

- `shortfx/mcp/` — New MCP (Model Context Protocol) server package:
  - `server.py` — FastMCP server exposing 6 meta-tools: `search_shortfx_tools`, `inspect_shortfx_tool`, `call_shortfx`, `list_shortfx_categories`, `get_shortfx_stats`, `get_shortfx_function_names` (218 lines)
  - `mcp.json` — MCP client configuration template (9 lines)
  - `README.md` — MCP integration documentation (281 lines)
  - `__init__.py`, `__main__.py` — Package init and entry point
- `shortfx/mcp_server.py` — Convenience re-export entry point (7 lines)

#### fxNumeric — 24 New Submodules (~18 000 lines)

- `calculator_functions.py` — AST-based safe expression evaluator (`scientific_calculate`) (283 lines)
- `complex_functions.py` — Complex number arithmetic, polar/rect conversion (603 lines)
- `conformal_functions.py` — Conformal mappings (Joukowski, Möbius, etc.) (288 lines)
- `constants_functions.py` — Mathematical/physical constants (π, e, φ, c, h, etc.) (191 lines)
- `coordinate_systems_functions.py` — Cartesian ↔ polar ↔ spherical ↔ cylindrical conversions (302 lines)
- `curves_functions.py` — Parametric curves, Bézier, splines, arc length, curvature (1 291 lines)
- `distribution_functions.py` — Probability distributions (normal, binomial, Poisson, exponential, etc.) (898 lines)
- `finite_differences_functions.py` — Forward/backward/central differences, numerical derivatives (382 lines)
- `format_functions.py` — Number formatting utilities (118 lines)
- `geometry_functions.py` — 2D/3D geometry: areas, volumes, distances, polygons (1 312 lines)
- `inequalities_functions.py` — Inequality solving and evaluation (312 lines)
- `interpolation_functions.py` — Linear, Lagrange, Newton, cubic spline interpolation (504 lines)
- `mechanics_functions.py` — Classical mechanics formulas (force, energy, momentum, etc.) (436 lines)
- `number_theory_functions.py` — Primes, GCD, LCM, factorisation, modular arithmetic, Euler's totient (3 309 lines)
- `numerical_methods_functions.py` — Root-finding (bisection, Newton, secant), numerical integration (742 lines)
- `polynomial_functions.py` — Polynomial evaluation, roots, addition, multiplication (337 lines)
- `probability_extra_functions.py` — Combinatorics, Bayes' theorem, expected value (575 lines)
- `random_functions.py` — Random number generation with various distributions (216 lines)
- `rounding_functions.py` — Rounding modes (banker's, floor, ceiling, significant figures) (454 lines)
- `series_functions.py` — Arithmetic/geometric/harmonic/Taylor/Fourier series (1 146 lines)
- `special_functions.py` — Gamma, beta, erf, Bessel, zeta, Legendre, Laguerre (3 028 lines)
- `tensor_functions.py` — Tensor operations (dot, cross, outer product, trace) (331 lines)
- `transform_functions.py` — DFT, DCT, Hadamard, Z-transform (601 lines)
- `vector_analysis_functions.py` — Gradient, divergence, curl, line/surface integrals (532 lines)

#### fxString — 5 New Submodules (~579 lines)

- `string_caseconv.py` — Case conversion utilities (camelCase, snake_case, kebab-case, PascalCase, etc.) (159 lines)
- `string_compression.py` — Zlib-based string compression/decompression (50 lines)
- `string_encoding.py` — Base64, hex, URL, ROT13, morse code encoding/decoding (198 lines)
- `string_hashing.py` — MD5, SHA-256, SHA-512 string hashing (58 lines)
- `string_regex.py` — Regex utilities (match, find_all, replace, split, validate) (114 lines)

#### fxPython — 1 New Submodule

- `py_logic.py` — Logic helper functions (IIf, Switch, Choose, coalesce, etc.) (70 lines)

#### Project Files

- `CONTRIBUTING.md` — Contribution guidelines (294 lines)
- `CHANGELOG.md` — Full changelog reconstructed from commit history
- `quality_functions.md` — Function quality checklist (24 lines)
- `_audit.py` — Function catalogue audit and quality metrics tool (2 334 lines)
- `_scan_core.py` — Core module scanner utility (30 lines)

### Changed

#### Architecture — `auto_export` Migration

- All 6 `fx*/__init__.py` files rewritten to use `shortfx._loader.auto_export()` instead of manual imports or dynamic `__all__` construction
- `shortfx/__init__.py` — Emptied; subpackages are now imported explicitly by consumers

#### fxNumeric — Rename & Expand (5 files renamed, 1 deleted)

- `numeric_arithmetic.py` → `arithmetic_functions.py` — Expanded from 358 to 4 824 lines with new functions
- `numeric_convertions.py` → `conversion_functions.py` — Expanded from 1 080 to 9 203 lines
- `numeric_finance.py` → `finance_functions.py` — Expanded from 680 to 9 334 lines
- `numeric_statistics.py` → `statistics_functions.py` — Expanded from 584 to 11 999 lines
- `numeric_trigonometry.py` → `trigonometry_functions.py` — Expanded from 1 156 to 5 446 lines
- `fxNumeric/README.md` — Comprehensive documentation rewrite (+5 292 lines)

#### fxString — Expand Existing Modules

- `string_operations.py` — +3 083 lines: new string functions
- `string_evaluations.py` — +2 293 lines: new evaluation and validation functions
- `string_convertions.py` — +1 141 lines: new conversion functions
- `string_format.py` — +640 lines: new formatting functions
- `string_similarity.py` — +155 lines: additional similarity algorithms and fallbacks
- `fxString/README.md` — Comprehensive documentation rewrite (+2 268 lines)

#### fxDate — Expand Existing Modules

- `date_operations.py` — +3 625 lines: new date arithmetic and manipulation functions
- `date_evaluations.py` — +2 566 lines: new date validation and evaluation functions
- `date_convertions.py` — +1 075 lines: new date conversion functions
- `date_sys.py` — +168 lines: new system date functions
- `fxDate/README.md` — Comprehensive documentation rewrite (+1 481 lines)

#### fxExcel — Expand All Modules

- `statistic_formulas.py` — +2 217 lines: expanded statistical functions
- `math_formulas.py` — +817 lines: expanded math functions
- `lookup_formulas.py` — +734 lines: expanded lookup/reference functions
- `financial_formulas.py` — +656 lines: expanded financial functions
- `engineering_formulas.py` — +447 lines: expanded engineering functions
- `text_formulas.py` — +397 lines: expanded text functions
- `date_formulas.py` — +282 lines: expanded date formulas
- `logic_formulas.py` — +150 lines: expanded logic functions
- `database_formulas.py` — +95 lines: expanded database functions
- `information_formulas.py` — +81 lines: expanded information functions
- `fxExcel/README.md` — Comprehensive documentation rewrite (+6 168 lines)

#### fxPython — Expand Existing Modules

- `py_operations.py` — +2 008 lines: new iterable/dict operations
- `py_tools.py` — +120 lines: expanded utility functions
- `py_convertions.py` — +123 lines: expanded conversion functions
- `py_itertools.py` — Refactored (−38 lines, streamlined)
- `fxPython/README.md` — Comprehensive documentation rewrite (+1 084 lines)

#### fxVBA — Expand Existing Modules

- `string_functions.py` — +429 lines: expanded VBA string functions
- `financial_functions.py` — +293 lines: expanded VBA financial functions
- `date_functions.py` — +176 lines: expanded VBA date functions
- `conversion_functions.py` — +144 lines: expanded VBA conversion functions
- `misc_functions.py` — +97 lines: expanded miscellaneous VBA functions
- `format_functions.py` — +82 lines: expanded VBA format functions
- `math_functions.py` — +54 lines: expanded VBA math functions
- `logic_functions.py` — +19 lines: expanded VBA logic functions

#### Documentation

- `README.md` — Updated project description and module overview (+65 lines)
- `llms.txt` — Major expansion with function catalogue for AI discovery (+2 329 lines)
- `uv.lock` — Updated dependency lock file (+1 819 lines)
- `examples/examples_fxPython.py` — Updated examples (+79 lines)

### Removed

- `shortfx/fxNumeric/numeric_operations.py` — Deleted (−1 143 lines); functions redistributed to new domain-specific submodules
- `shortfx/fxVBA/README.md` — Removed (−42 lines)
- `shortfx/fxVBA/system_functions.py` — Reduced (−24 lines)

---

## [0.1.0][0.1.0] — 2026-03-29

Initial development release of shortfx — a Python library for high-level functions similar to Excel formulas, organized into thematic modules (fxDate, fxString, fxNumeric, fxPython, fxExcel, fxVBA).

---

### `5be2a69` — string function updates (2026-03-29)

Add data masking, distinct split, improved lazy imports with auto-install, and CIF validation fix.

**5 files changed** | +314 −49

#### Added

- `shortfx/fxString/string_format.py` — Add `mask_data()` for data anonymization/obfuscation with positional masking modes (`all`, `start`, `end`, `index`) (+77 lines)
- `shortfx/fxString/string_operations.py` — Add `distinct_split()` to split delimited strings, remove duplicate tokens preserving order, and re-join (+66 lines)
- `shortfx/fxString/README.md` — Document `distinct_split` function in index and reference sections (+37 lines)

#### Changed

- `shortfx/fxString/string_similarity.py` — Rewrite `_lazy_import()` with multi-strategy auto-install (uv add → uv pip → pip → pip --break-system-packages); add graceful fallbacks for `metaphone_score()` and `hamming_score()` when dependencies are unavailable (+122 −37)

#### Fixed

- `shortfx/fxString/string_spanish.py` — Fix CIF validation per AEAT (RD 1065/2007): correct odd/even digit sum algorithm and add letter `K` to letter-control-only group (+12 −12)

---

### `135974d` — new ignore (2026-02-05)

Extend `.gitignore` with comprehensive API key and secret exclusion patterns.

**1 file changed** | +11 −0

#### Changed

- `.gitignore` — Add glob patterns for `*key*` and `*secret*` files (`.txt`, `.csv`, `.json`, `.cfg`, `.toml`, `.env`) in any subdirectory

---

### `9e1defd` — string evaluations update (2026-02-03)

Clean up docstrings across string evaluation functions.

**1 file changed** | +5 −87

#### Changed

- `shortfx/fxString/string_evaluations.py` — Remove verbose `**Cost:**` annotations from 20+ function docstrings; simplify module-level docstring; standardize docstring format

---

### `88a8d19` — uv lock (2026-01-19)

Add uv lock file for reproducible dependency resolution.

**1 file changed** | +3 −0

#### Added

- `uv.lock` — Generated lock file for uv package manager

---

### `7b55779` — empty init (2026-01-13)

Remove all re-exports from `__init__.py` files; prefer explicit module imports.

**7 files changed** | +0 −263

#### Changed

- `shortfx/__init__.py` — Remove package docstring and star imports of subpackages (−20 lines)
- `shortfx/fxDate/__init__.py` — Remove `diff_time` re-export and `__all__` (−12 lines)
- `shortfx/fxExcel/__init__.py` — Remove dynamic submodule re-exports (−60 lines)
- `shortfx/fxNumeric/__init__.py` — Remove docstring and `__version__` (−9 lines)
- `shortfx/fxPython/__init__.py` — Remove explicit function re-exports from `py_operations`, `py_convertions`, `py_tools`, `py_itertools` (−60 lines)
- `shortfx/fxString/__init__.py` — Remove docstring and import guidance comment (−12 lines)
- `shortfx/fxVBA/__init__.py` — Remove dynamic re-exports and VBA aliases (`Join`, `Array`, `Filter`, `Type_`, `Input_`) (−90 lines)

---

### `ff63fd7` — fix documentation (2026-01-13)

Fix documentation issues across the project.

**Files changed** | Documentation corrections

#### Fixed

- Documentation fixes (diff unavailable — inferred from commit message)

---

### `34e2d32` — Merge branch 'main' (2026-01-08)

Merge commit incorporating documentation overhaul and syntax error fix.

**58 files changed** | +43329 −1426

#### Changed

- Merge of `261b3f6` + `e58ba2b` — Consolidate documentation overhaul with syntax fix

---

### `261b3f6` — sintax error (2026-01-08)

Remove duplicate `string_merge` function definition.

**1 file changed** | +0 −138

#### Fixed

- `shortfx/fxString/string_operations.py` — Remove duplicated `string_merge()` function code block that caused syntax error (−138 lines)

---

### `e58ba2b` — Documentation and new functions (2026-01-07)

Major release: complete documentation rewrite, add fxExcel and fxVBA modules, add date evaluations, and comprehensive LLMs.txt.

**58 files changed** | +43329 −1564

#### Added

- `shortfx/fxExcel/` — New Excel-compatible formulas module with 11 submodules:
  - `database_formulas.py` — Database functions (DSUM, DCOUNT, DAVERAGE, etc.)
  - `date_formulas.py` — Date/time functions (DATE, TIME, NOW, TODAY, etc.)
  - `engineering_formulas.py` — Engineering functions (DEC2BIN, HEX2DEC, CONVERT, etc.)
  - `financial_formulas.py` — Financial functions (PMT, FV, PV, NPV, IRR, etc.)
  - `information_formulas.py` — Information functions (ISNUMBER, ISTEXT, TYPE, etc.)
  - `logic_formulas.py` — Logic functions (IF, AND, OR, NOT, XOR, IFS, etc.)
  - `lookup_formulas.py` — Lookup functions (VLOOKUP, HLOOKUP, INDEX, MATCH, etc.)
  - `math_formulas.py` — Math functions (SUM, PRODUCT, MOD, POWER, etc.)
  - `statistic_formulas.py` — Statistical functions (AVERAGE, MEDIAN, STDEV, etc.)
  - `text_formulas.py` — Text functions (CONCATENATE, LEFT, RIGHT, MID, etc.)
  - `fxExcel.md` — Module documentation
- `shortfx/fxVBA/` — New VBA/Access-compatible functions module:
  - `array_functions.py`, `conversion_functions.py`, `string_functions.py`
  - `date_functions.py`, `math_functions.py`, `financial_functions.py`
  - `logic_functions.py`, `system_functions.py`, `format_functions.py`
  - `interaction_functions.py`, `error_functions.py`
- `shortfx/fxDate/date_evaluations.py` — New date evaluation and validation functions
- `shortfx/fxDate/fxDate.md` — Module documentation
- `shortfx/fxNumeric/fxNumeric.md` — Module documentation
- `LLMs.txt` — Comprehensive LLM-friendly project description (+770 lines)
- `Help.md` — Help documentation

#### Changed

- `README.md` — Complete rewrite with new structure: module overview, usage examples for fxExcel, fxDate, fxString, fxVBA; installation instructions (+120 −92)
- `shortfx/__init__.py` — Add package docstring with domain descriptions; add subpackage imports (+15 −4)
- `shortfx/fxDate/__init__.py` — Add docstring, `diff_time` re-export, and `__all__` (+11 −2)

---

### `0468292` — more funcitons (2025-12-22)

Add itertools module, string merge function, and fix ISO datetime conversion.

**5 files changed** | +1089 −24

#### Added

- `shortfx/fxPython/py_itertools.py` — New itertools-based utilities module (+796 lines): batch processing, sliding windows, chain operations, grouping utilities, and more
- `shortfx/fxString/string_operations.py` — Add `string_merge()` for 3-way string merging with conflict detection and markers (+279 lines)

#### Changed

- `.gitignore` — Replace specific `secrets.toml` with generic `**/secrets.*` pattern (+1 −2)
- `LLMs.txt` — Whitespace normalization

#### Fixed

- `shortfx/fxDate/date_convertions.py` — Fix `from_iso_to_local_datetime()` for Python 3.10 compatibility: handle `'Z'` suffix by replacing with `'+00:00'`; use `datetime.astimezone()` without argument instead of `ZoneInfo("localtime")` for cross-platform support (+13 −22)

---

### `8c1d366` — reorganization (2025-12-22)

Project structure reorganization.

**Files changed** | Structural refactoring

#### Changed

- Reorganize project file structure (diff unavailable — inferred from commit message)

---

### `c84fdba` — reorder functions and new flat_vowels (2025-08-05)

Reorder and rename dictionary functions, remove Pydantic dependency, improve `flat_vowels`.

**4 files changed** | +348 −288

#### Added

- `shortfx/fxPython/py_convertions.py` — Add `dictionary_to_string()`, `string_to_dictionary()`, and `convert_string_to_list()` functions
- `shortfx/fxPython/py_operations.py` — Add `dictionary_filter_by_keys()` and `combine_dictionaries()` (union/intersection) (+161 lines)

#### Changed

- `shortfx/fxPython/py_convertions.py` — Rename `dict_*` functions to `dictionary_*` for consistency: `dictionary_keys_to_list`, `dictionary_items_to_list_of_tuples`, `dictionary_keys_to_set`, `dictionary_values_to_set`
- `shortfx/fxString/string_format.py` — Rewrite `flat_vowels()` to preserve Spanish special characters (ñ, ç, ü) while removing only acute accents; add `TypeError` raise instead of returning `False` for non-string input (+39 −7)

#### Removed

- `shortfx/fxPython/py_convertions.py` — Remove `json_schema_to_pydantic_model()` and Pydantic dependency (`from pydantic import BaseModel, Field, create_model`)
- `shortfx/fxString/string_convertions.py` — Remove `string_to_list()` (moved to `py_convertions.py` as `convert_string_to_list`) (−73 lines)

---

### `c00a855` — Refactor estructura y añade conversión de JSON Schema a Pydantic (2025-07-28)

Refactor project structure and add JSON Schema to Pydantic model conversion.

**Files changed** | Structural refactoring + new features

#### Added

- JSON Schema to Pydantic model conversion functionality (diff unavailable — inferred from commit message)

#### Changed

- Project structure refactoring

---

### `7b8af4b` — move files to folder (2025-07-24)

Move all source modules into `shortfx/` package directory; add example files.

**30 files changed** | +325 −69

#### Added

- `examples.py` — Usage examples for math, text, and lookup functions (+36 lines)
- `shortfx/fxString/example_grammar.py` — Grammar correction example using `SpellCorrector` (+39 lines)
- `shortfx/fxString/example_names_corrector.py` — Name correction and validation example with SQLite integration (+238 lines)

#### Changed

- All modules renamed from root to `shortfx/` package:
  - `fxDate/*.py` → `shortfx/fxDate/*.py` (5 files)
  - `fxNumeric/*.py` → `shortfx/fxNumeric/*.py` (6 files)
  - `fxPython/*.py` → `shortfx/fxPython/*.py` (3 files)
  - `fxString/*.py` → `shortfx/fxString/*.py` (8 files)
- `__init__.py` — Remove `py_classes` import (module deleted)
- `.gitignore` — Add exclusions for `.github/`, `.vscode/`, `tests/`, `docs/`, `notebooks/`, `ToDo/`

#### Removed

- `shortfx/fxPython/py_tools.py` — Remove `generate_key()` function and its prime number generator (−67 lines)

---

### `45bfa8e` — move data structures to fastETL (2025-07-24)

Move data structure classes to the fastETL project.

**1 file changed** | +0 −321

#### Removed

- `fxPython/py_classes.py` — Remove data structure classes (moved to external fastETL project) (−321 lines)

---

### `985f0b6` — codebase (2025-07-13)

Initial codebase upload with all core function modules.

**Files changed** | Large initial upload

#### Added

- `fxDate/` — Date manipulation module: `date_convertions.py`, `date_operations.py`, `date_sys.py`, `date_excel.py`
- `fxNumeric/` — Numeric operations module: `numeric_arithmetic.py`, `numeric_convertions.py`, `numeric_finance.py`, `numeric_operations.py`, `numeric_statistics.py`, `numeric_trigonometry.py`
- `fxPython/` — Python utilities module: `py_classes.py`, `py_convertions.py`, `py_operations.py`, `py_tools.py`
- `fxString/` — String manipulation module: `string_convertions.py`, `string_evaluations.py`, `string_format.py`, `string_grammar.py`, `string_operations.py`, `string_similarity.py`, `string_spanish.py`, `string_validations.py`
- `__init__.py` — Package initialization with star imports from all modules

---

### `79a264d` — Initial commit (2025-06-08)

Repository initialization with license and README.

**3 files changed** | +216 −0

#### Added

- `.gitignore` — Comprehensive Python gitignore template (+194 lines)
- `LICENSE` — MIT License, Copyright (c) 2025 DatamanEdge (+21 lines)
- `README.md` — Initial project title (+1 line)

---

[Unreleased]: https://github.com/jrodriguezgar/shortfx/compare/v0.3.1...HEAD
[0.3.1]: https://github.com/jrodriguezgar/shortfx/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/jrodriguezgar/shortfx/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/jrodriguezgar/shortfx/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/jrodriguezgar/shortfx/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/jrodriguezgar/shortfx/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/jrodriguezgar/shortfx/releases/tag/v0.1.0
