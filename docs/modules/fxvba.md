# fxVBA — VBA/Access Compatibility

Functions with names and behaviors matching VBA and Microsoft Access, designed for developers migrating from the Microsoft Office ecosystem.

## Submodules

| Submodule | Purpose |
|-----------|---------|
| [`string_functions`](../reference/fxVBA/string_functions.md) | Left, Right, Mid, InStr, Len, Trim, etc. |
| [`math_functions`](../reference/fxVBA/math_functions.md) | Abs, Int, Fix, Sgn, Sqr, etc. |
| [`date_functions`](../reference/fxVBA/date_functions.md) | DateAdd, DateDiff, DatePart, etc. |
| [`conversion_functions`](../reference/fxVBA/conversion_functions.md) | CStr, CInt, CDbl, CBool, etc. |
| [`format_functions`](../reference/fxVBA/format_functions.md) | Format, FormatNumber, FormatCurrency, etc. |
| [`logic_functions`](../reference/fxVBA/logic_functions.md) | IIf, Switch, Choose, etc. |
| [`financial_functions`](../reference/fxVBA/financial_functions.md) | DDB, SLN, SYD, Rate, etc. |
| [`array_functions`](../reference/fxVBA/array_functions.md) | Array, UBound, LBound, Split, Join, etc. |
| [`misc_functions`](../reference/fxVBA/misc_functions.md) | TypeName, IsNumeric, IsDate, etc. |
| [`system_functions`](../reference/fxVBA/system_functions.md) | Environ, Timer, etc. |

## Quick Examples

```python
from formulite import fxVBA

text = "Hello World"

# String functions (1-based indexing, like VBA)
start = fxVBA.Left(text, 5)              # "Hello"
position = fxVBA.InStr(1, text, "World")  # 7

# Type conversions
value = fxVBA.CInt("42")   # 42
flag = fxVBA.CBool(1)      # True

# Conditional
result = fxVBA.IIf(10 > 5, "Yes", "No")  # "Yes"
```

!!! note
    Function names use PascalCase to match VBA conventions (e.g., `InStr`, not `instr`).
