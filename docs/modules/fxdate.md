# fxDate — Date Operations

Date manipulation, evaluations, conversions, and system date queries.

## Submodules

| Submodule | Purpose |
|-----------|---------|
| [`date_operations`](../reference/fxDate/date_operations.md) | Add/subtract time, calculate differences, date arithmetic |
| [`date_evaluations`](../reference/fxDate/date_evaluations.md) | Validate dates, check leap years, compare dates |
| [`date_convertions`](../reference/fxDate/date_convertions.md) | Convert between formats, parse strings, epoch conversions |
| [`date_sys`](../reference/fxDate/date_sys.md) | System date/time queries, current timestamps |

## Quick Examples

```python
from datetime import datetime
from shortfx.fxDate import date_operations, date_evaluations

# Add 30 days to a date
new_date = date_operations.add_time_to_date(datetime(2025, 1, 15), 30, "days")

# Validate a date string
is_valid = date_operations.is_valid_date("2025-02-30")  # False

# Check if a year is a leap year
is_leap = date_evaluations.is_leap_year(2024)  # True
```

## API Reference

See the full auto-generated reference for each submodule:

- [date_operations](../reference/fxDate/date_operations.md)
- [date_evaluations](../reference/fxDate/date_evaluations.md)
- [date_convertions](../reference/fxDate/date_convertions.md)
- [date_sys](../reference/fxDate/date_sys.md)
