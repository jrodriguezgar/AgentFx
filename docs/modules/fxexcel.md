# fxExcel — Excel-Compatible Functions

Functions with names and behaviors identical to Microsoft Excel, making the transition from spreadsheets to Python seamless.

## Submodules

| Submodule | Purpose |
|-----------|---------|
| [`database_formulas`](../reference/fxExcel/database_formulas.md) | DSUM, DAVERAGE, DCOUNT, etc. |
| [`date_formulas`](../reference/fxExcel/date_formulas.md) | DATE, YEAR, MONTH, DAY, NOW, etc. |
| [`engineering_formulas`](../reference/fxExcel/engineering_formulas.md) | BIN2DEC, HEX2OCT, CONVERT, etc. |
| [`financial_formulas`](../reference/fxExcel/financial_formulas.md) | PMT, FV, PV, NPV, IRR, etc. |
| [`information_formulas`](../reference/fxExcel/information_formulas.md) | ISNUMBER, ISTEXT, ISERROR, TYPE, etc. |
| [`logic_formulas`](../reference/fxExcel/logic_formulas.md) | IF, AND, OR, NOT, IFS, SWITCH, etc. |
| [`lookup_formulas`](../reference/fxExcel/lookup_formulas.md) | VLOOKUP, HLOOKUP, INDEX, MATCH, etc. |
| [`math_formulas`](../reference/fxExcel/math_formulas.md) | SUM, SUMIF, ROUND, ABS, MOD, etc. |
| [`statistic_formulas`](../reference/fxExcel/statistic_formulas.md) | AVERAGE, MEDIAN, STDEV, COUNT, etc. |
| [`text_formulas`](../reference/fxExcel/text_formulas.md) | CONCATENATE, LEFT, RIGHT, MID, TRIM, etc. |

## Quick Examples

```python
from formulite import fxExcel

# VLOOKUP
table = [
    ["Name", "Age", "City"],
    ["Ana", 25, "Madrid"],
    ["Juan", 30, "Barcelona"],
]
age = fxExcel.VLOOKUP("Ana", table, 2)  # 25

# Text functions
greeting = fxExcel.CONCATENATE("Hello", " ", "World")  # "Hello World"

# Math
total = fxExcel.SUMIF([10, 20, 30, 40], ">15")  # 90

# Logic
result = fxExcel.IF(True, "Yes", "No")  # "Yes"
```

!!! note
    All function names use UPPERCASE to match Excel conventions (e.g., `VLOOKUP`, not `vlookup`).
