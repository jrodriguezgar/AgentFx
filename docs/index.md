---
hide:
  - navigation
---

# AgentFx

> _"Write less, do more."_
> _"The deterministic toolset your AI agents can trust."_

**AgentFx** is a Python library that encapsulates complex programming logic into **3,000+ reusable functions**, organized like Excel formulas. It also serves as a **deterministic toolset for AI agents** via `llms.txt` and a built-in MCP server.

---

<div class="grid cards" markdown>

-   :material-function-variant:{ .lg .middle } **3,000+ Functions**

    ---

    The largest open-source Python formula library — dates, math, finance, statistics, strings, Excel & VBA compatibility.

    [:octicons-arrow-right-24: Browse modules](modules/index.md)

-   :material-robot:{ .lg .middle } **AI-Native via MCP**

    ---

    Built-in Model Context Protocol server lets AI agents discover, inspect, and execute any function as a tool.

    [:octicons-arrow-right-24: AI integration](ai-integration/index.md)

-   :material-package-variant:{ .lg .middle } **Zero Dependencies**

    ---

    Core library uses only the Python standard library — no NumPy, no Pandas.

    [:octicons-arrow-right-24: Get started](getting-started.md)

-   :material-file-document:{ .lg .middle } **`llms.txt` Included**

    ---

    A machine-readable function catalogue so LLMs can look up signatures and descriptions without calling a server.

    [:octicons-arrow-right-24: Learn more](ai-integration/llms-txt.md)

</div>

---

## Module Overview

| Module | Functions | Scope |
|--------|----------:|-------|
| [`fxNumeric`](modules/fxnumeric.md) | 1,602 | Finance, statistics, geometry, transforms, series, number theory |
| [`fxExcel`](modules/fxexcel.md) | 489 | Excel-compatible formulas (VLOOKUP, PMT, CONCATENATE …) |
| [`fxString`](modules/fxstring.md) | 331 | Text manipulation, regex, hashing, validation, encoding, similarity |
| [`fxDate`](modules/fxdate.md) | 261 | Date operations, evaluations, conversions, system dates |
| [`fxVBA`](modules/fxvba.md) | 133 | VBA/Access-compatible functions (Left, InStr, Format …) |
| [`fxPython`](modules/fxpython.md) | 116 | Iterable utilities, type conversions, logic helpers |

## Quick Example

```python
from agentfx import fxDate, fxExcel, fxNumeric

# Date arithmetic
from datetime import datetime
new_date = fxDate.date_operations.add_time_to_date(datetime(2025, 1, 15), 30, "days")

# Excel-style VLOOKUP
table = [["Name", "Age"], ["Ana", 25], ["Juan", 30]]
age = fxExcel.VLOOKUP("Ana", table, 2)  # 25

# Financial calculations
fv = fxNumeric.finance_functions.future_value(rate=0.05, nper=10, pmt=-100, pv=-1000)
```
