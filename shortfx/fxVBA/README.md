# shortfx - fxVBA Functions Documentation

## Overview

The `fxVBA` module provides VBA-compatible functions for shortfx. These functions replicate VBA/Access behavior across multiple categories:
- **Array Functions**: Array manipulation, splitting, joining, filtering, bounds checking
- **Conversion Functions**: Type conversions compatible with VBA (CBool, CInt, CDate, etc.)
- **Date and Time Functions**: Date manipulation, date parts, date arithmetic
- **Financial Functions**: Loan payments, depreciation, present value, internal rate of return
- **Format Functions**: Number formatting, currency formatting, date formatting
- **Logic Functions**: Conditional evaluation, type checking, null handling
- **Math Functions**: Mathematical operations, trigonometry, rounding
- **Miscellaneous Functions**: Error handling, color functions, evaluation
- **String Functions**: Text manipulation, search, replacement, case conversion
- **System Functions**: File system operations, environment variables, user dialogs

## Module Structure

- **array_functions.py**: VBA-compatible array manipulation functions
- **conversion_functions.py**: VBA-compatible type conversion functions
- **date_functions.py**: VBA-compatible date and time functions
- **financial_functions.py**: VBA-compatible financial functions
- **format_functions.py**: VBA-compatible formatting functions
- **logic_functions.py**: VBA-compatible logical and conditional functions
- **math_functions.py**: VBA-compatible mathematical functions
- **misc_functions.py**: VBA-compatible miscellaneous utility functions
- **string_functions.py**: VBA-compatible text manipulation functions
- **system_functions.py**: VBA-compatible system and file functions

## Table of Contents

- [Function Categories](#function-categories)
  - [Array Functions](#array-functions)
  - [Conversion Functions](#conversion-functions)
  - [Date Functions](#date-functions)
  - [Financial Functions](#financial-functions)
  - [Format Functions](#format-functions)
  - [Logic Functions](#logic-functions)
  - [Math Functions](#math-functions)
  - [Miscellaneous Functions](#miscellaneous-functions)
  - [String Functions](#string-functions)
  - [System Functions](#system-functions)
- [Function Index](#function-index)
- [Credits](#credits)

---

## Function Categories

### Array Functions
- [Split](#split) - Divides string into array of substrings using delimiter
- [Join_](#join_) - Joins array elements into string using delimiter
- [Filter_](#filter_) - Filters array elements that contain (or not) specific string
- [LBound](#lbound) - Returns lower bound of array dimension
- [UBound](#ubound) - Returns upper bound of array dimension
- [Array_](#array_) - Creates array from list of values

### Conversion Functions
- [CBool](#cbool) - Converts expression to Boolean
- [CByte](#cbyte) - Converts number to Byte (0-255)
- [CCur](#ccur) - Converts number to Currency (4 decimal places)
- [CDate](#cdate) - Converts expression to datetime
- [CDbl](#cdbl) - Converts expression to Double
- [CDec](#cdec) - Converts expression to Decimal
- [CInt](#cint) - Converts expression to Integer (with rounding)
- [CLng](#clng) - Converts expression to Long Integer
- [CSng](#csng) - Converts expression to Single precision float
- [CStr](#cstr) - Converts expression to String
- [CVar](#cvar) - Converts expression to Variant (Any type)
- [DateValue](#datevalue) - Converts date string to date
- [TimeValue](#timevalue) - Converts time string to time
- [Val](#val) - Extracts numeric value from string

### Date Functions
- [Date_](#date_) - Returns current system date
- [DateAdd](#dateadd) - Adds time interval to date
- [DateDiff](#datediff) - Returns difference between two dates
- [DatePart](#datepart) - Returns specific part of date
- [DateSerial](#dateserial) - Creates date from year, month, day
- [Day](#day) - Returns day of month from date
- [Hour](#hour) - Returns hour component from datetime
- [Minute](#minute) - Returns minute component from datetime
- [Month](#month) - Returns month from date
- [MonthName](#monthname) - Returns name of month
- [Now](#now) - Returns current date and time
- [Second](#second) - Returns second component from datetime
- [Time_](#time_) - Returns current system time
- [Timer](#timer) - Returns seconds since midnight
- [TimeSerial](#timeserial) - Creates time from hour, minute, second
- [WeekDay](#weekday) - Returns day of week from date
- [WeekDayName](#weekdayname) - Returns name of weekday
- [Year](#year) - Returns year from date

### Financial Functions
- [DDB](#ddb) - Calculates depreciation using double-declining balance method
- [FV](#fv) - Calculates future value of investment
- [IPmt](#ipmt) - Returns interest payment for specific period
- [IRR](#irr) - Returns internal rate of return for cash flows
- [MIRR](#mirr) - Returns modified internal rate of return
- [NPer](#nper) - Returns number of periods for investment
- [NPV](#npv) - Calculates net present value of investment
- [Pmt](#pmt) - Calculates payment for loan
- [PPmt](#ppmt) - Returns principal payment for specific period
- [PV](#pv) - Calculates present value of investment
- [Rate](#rate) - Returns interest rate per period
- [SLN](#sln) - Calculates straight-line depreciation
- [SYD](#syd) - Calculates sum-of-years' digits depreciation

### Format Functions
- [Format_](#format_) - Formats expression according to format string
- [FormatCurrency](#formatcurrency) - Formats number as currency
- [FormatDateTime](#formatdatetime) - Formats datetime with named format
- [FormatNumber](#formatnumber) - Formats number with specific options
- [FormatPercent](#formatpercent) - Formats number as percentage

### Logic Functions
- [Choose](#choose) - Returns value from list based on index
- [IIf](#iif) - Returns one of two values based on condition
- [IsArray](#isarray) - Tests if variable is array
- [IsDate](#isdate) - Tests if expression can be converted to date
- [IsEmpty](#isempty) - Tests if variable is empty/None
- [IsError](#iserror) - Tests if expression is error value
- [IsMissing](#ismissing) - Tests if optional argument was provided
- [IsNull](#isnull) - Tests if expression is None
- [IsNumeric](#isnumeric) - Tests if expression can be converted to number
- [IsObject](#isobject) - Tests if variable is object
- [Switch](#switch) - Evaluates list of expressions and returns associated value

### Math Functions
- [Abs_](#abs_) - Returns absolute value of number
- [Atn](#atn) - Returns arctangent in radians
- [Cos](#cos) - Returns cosine of angle in radians
- [Exp](#exp) - Returns e raised to power
- [Fix](#fix) - Returns integer part truncating toward zero
- [Int_](#int_) - Returns integer part truncating toward negative infinity
- [Log](#log) - Returns natural logarithm
- [Rnd](#rnd) - Returns random number between 0 and 1
- [Round_](#round_) - Rounds number to specified decimal places
- [Sgn](#sgn) - Returns sign of number (-1, 0, or 1)
- [Sin](#sin) - Returns sine of angle in radians
- [Sqr](#sqr) - Returns square root
- [Tan](#tan) - Returns tangent of angle in radians

### Miscellaneous Functions
- [AccessError](#accesserror) - Returns error description for Access error number
- [CurrentUser](#currentuser) - Returns current user name
- [Eval_](#eval_) - Evaluates string expression
- [Hex_](#hex_) - Converts number to hexadecimal string
- [HexS](#hexs) - Converts number to hexadecimal string (String version)
- [Oct_](#oct_) - Converts number to octal string
- [OctS](#octs) - Converts number to octal string (String version)
- [QBColor](#qbcolor) - Returns RGB color code for QBasic color
- [RGB](#rgb) - Returns RGB color value
- [SysCmd](#syscmd) - Executes system command

### String Functions
- [Asc](#asc) - Returns character code of first character
- [AscB](#ascb) - Returns code of first byte
- [Chr_](#chr_) - Returns character from character code
- [ChrS](#chrs) - Returns character from character code (String version)
- [ChrW](#chrw) - Returns Unicode character from code
- [ChrWS](#chrws) - Returns Unicode character from code (String version)
- [InStr](#instr) - Finds position of substring within string
- [InStrRev](#instrrev) - Finds position of substring searching from end
- [LCase](#lcase) - Converts string to lowercase
- [LCaseS](#lcases) - Converts string to lowercase (String version)
- [Left](#left) - Returns leftmost characters from string
- [LeftS](#lefts) - Returns leftmost characters (String version)
- [LeftB](#leftb) - Returns leftmost bytes from string
- [LeftBS](#leftbs) - Returns leftmost bytes (String version)
- [Len_](#len_) - Returns length of string
- [LenB](#lenb) - Returns length in bytes
- [LTrim](#ltrim) - Removes leading spaces
- [LTrimS](#ltrims) - Removes leading spaces (String version)
- [Mid](#mid) - Returns substring from middle of string
- [MidS](#mids) - Returns substring from middle (String version)
- [MidB](#midb) - Returns bytes from middle of string
- [MidBS](#midbs) - Returns bytes from middle (String version)
- [Replace](#replace) - Replaces substring with another substring
- [Right](#right) - Returns rightmost characters from string
- [RightS](#rights) - Returns rightmost characters (String version)
- [RightB](#rightb) - Returns rightmost bytes from string
- [RightBS](#rightbs) - Returns rightmost bytes (String version)
- [RTrim](#rtrim) - Removes trailing spaces
- [RTrimS](#rtrims) - Removes trailing spaces (String version)
- [Space](#space) - Returns string of spaces
- [Str_](#str_) - Converts number to string
- [StrS](#strs) - Converts number to string (String version)
- [StrComp](#strcomp) - Compares two strings
- [StrConv](#strconv) - Converts string with specified conversion
- [String](#string) - Returns string of repeated character
- [StrReverse](#strreverse) - Reverses string
- [Trim](#trim) - Removes leading and trailing spaces
- [TrimS](#trims) - Removes leading and trailing spaces (String version)
- [UCase](#ucase) - Converts string to uppercase
- [UCaseS](#ucases) - Converts string to uppercase (String version)

### System Functions
- [BuildCriteria](#buildcriteria) - Builds SQL WHERE clause from parameters
- [Command](#command) - Returns command line arguments
- [CurDir](#curdir) - Returns current directory path
- [Dir_](#dir_) - Returns file or directory name matching pattern
- [Environ](#environ) - Returns environment variable value
- [EnvironS](#environs) - Returns environment variable value (String version)
- [Error](#error) - Returns error message for error number
- [FileDateTime](#filedatetime) - Returns modification datetime of file
- [FileLen](#filelen) - Returns size of file in bytes
- [GetAttr_](#getattr_) - Returns attributes of file
- [Nz](#nz) - Returns value if not null, otherwise returns alternative
- [Partition](#partition) - Returns range string where number falls
- [TypeName](#typename) - Returns string describing variable type
- [VarType](#vartype) - Returns integer indicating variable type

---

## Function Index

**A**
- [Abs_](#abs_) - Returns absolute value of number
- [AccessError](#accesserror) - Returns error description for Access error number
- [Array_](#array_) - Creates array from list of values
- [Asc](#asc) - Returns character code of first character
- [AscB](#ascb) - Returns code of first byte
- [Atn](#atn) - Returns arctangent in radians

**B**
- [BuildCriteria](#buildcriteria) - Builds SQL WHERE clause from parameters

**C**
- [CBool](#cbool) - Converts expression to Boolean
- [CByte](#cbyte) - Converts number to Byte (0-255)
- [CCur](#ccur) - Converts number to Currency (4 decimal places)
- [CDate](#cdate) - Converts expression to datetime
- [CDbl](#cdbl) - Converts expression to Double
- [CDec](#cdec) - Converts expression to Decimal
- [Choose](#choose) - Returns value from list based on index
- [Chr_](#chr_) - Returns character from character code
- [ChrS](#chrs) - Returns character from character code (String version)
- [ChrW](#chrw) - Returns Unicode character from code
- [ChrWS](#chrws) - Returns Unicode character from code (String version)
- [CInt](#cint) - Converts expression to Integer (with rounding)
- [CLng](#clng) - Converts expression to Long Integer
- [Command](#command) - Returns command line arguments
- [Cos](#cos) - Returns cosine of angle in radians
- [CSng](#csng) - Converts expression to Single precision float
- [CStr](#cstr) - Converts expression to String
- [CurrentUser](#currentuser) - Returns current user name
- [CurDir](#curdir) - Returns current directory path
- [CVar](#cvar) - Converts expression to Variant (Any type)

**D**
- [Date_](#date_) - Returns current system date
- [DateAdd](#dateadd) - Adds time interval to date
- [DateDiff](#datediff) - Returns difference between two dates
- [DatePart](#datepart) - Returns specific part of date
- [DateSerial](#dateserial) - Creates date from year, month, day
- [DateValue](#datevalue) - Converts date string to date
- [Day](#day) - Returns day of month from date
- [DDB](#ddb) - Calculates depreciation using double-declining balance method
- [Dir_](#dir_) - Returns file or directory name matching pattern

**E**
- [Environ](#environ) - Returns environment variable value
- [EnvironS](#environs) - Returns environment variable value (String version)
- [Error](#error) - Returns error message for error number
- [Eval_](#eval_) - Evaluates string expression
- [Exp](#exp) - Returns e raised to power

**F**
- [FileDateTime](#filedatetime) - Returns modification datetime of file
- [FileLen](#filelen) - Returns size of file in bytes
- [Filter_](#filter_) - Filters array elements that contain (or not) specific string
- [Fix](#fix) - Returns integer part truncating toward zero
- [Format_](#format_) - Formats expression according to format string
- [FormatCurrency](#formatcurrency) - Formats number as currency
- [FormatDateTime](#formatdatetime) - Formats datetime with named format
- [FormatNumber](#formatnumber) - Formats number with specific options
- [FormatPercent](#formatpercent) - Formats number as percentage
- [FV](#fv) - Calculates future value of investment

**G**
- [GetAttr_](#getattr_) - Returns attributes of file

**H**
- [Hex_](#hex_) - Converts number to hexadecimal string
- [HexS](#hexs) - Converts number to hexadecimal string (String version)
- [Hour](#hour) - Returns hour component from datetime

**I**
- [IIf](#iif) - Returns one of two values based on condition
- [InStr](#instr) - Finds position of substring within string
- [InStrRev](#instrrev) - Finds position of substring searching from end
- [Int_](#int_) - Returns integer part truncating toward negative infinity
- [IPmt](#ipmt) - Returns interest payment for specific period
- [IRR](#irr) - Returns internal rate of return for cash flows
- [IsArray](#isarray) - Tests if variable is array
- [IsDate](#isdate) - Tests if expression can be converted to date
- [IsEmpty](#isempty) - Tests if variable is empty/None
- [IsError](#iserror) - Tests if expression is error value
- [IsMissing](#ismissing) - Tests if optional argument was provided
- [IsNull](#isnull) - Tests if expression is None
- [IsNumeric](#isnumeric) - Tests if expression can be converted to number
- [IsObject](#isobject) - Tests if variable is object

**J**
- [Join_](#join_) - Joins array elements into string using delimiter

**L**
- [LBound](#lbound) - Returns lower bound of array dimension
- [LCase](#lcase) - Converts string to lowercase
- [LCaseS](#lcases) - Converts string to lowercase (String version)
- [Left](#left) - Returns leftmost characters from string
- [LeftB](#leftb) - Returns leftmost bytes from string
- [LeftBS](#leftbs) - Returns leftmost bytes (String version)
- [LeftS](#lefts) - Returns leftmost characters (String version)
- [Len_](#len_) - Returns length of string
- [LenB](#lenb) - Returns length in bytes
- [Log](#log) - Returns natural logarithm
- [LTrim](#ltrim) - Removes leading spaces
- [LTrimS](#ltrims) - Removes leading spaces (String version)

**M**
- [Mid](#mid) - Returns substring from middle of string
- [MidB](#midb) - Returns bytes from middle of string
- [MidBS](#midbs) - Returns bytes from middle (String version)
- [MidS](#mids) - Returns substring from middle (String version)
- [Minute](#minute) - Returns minute component from datetime
- [MIRR](#mirr) - Returns modified internal rate of return
- [Month](#month) - Returns month from date
- [MonthName](#monthname) - Returns name of month

**N**
- [Now](#now) - Returns current date and time
- [NPer](#nper) - Returns number of periods for investment
- [NPV](#npv) - Calculates net present value of investment
- [Nz](#nz) - Returns value if not null, otherwise returns alternative

**O**
- [Oct_](#oct_) - Converts number to octal string
- [OctS](#octs) - Converts number to octal string (String version)

**P**
- [Partition](#partition) - Returns range string where number falls
- [Pmt](#pmt) - Calculates payment for loan
- [PPmt](#ppmt) - Returns principal payment for specific period
- [PV](#pv) - Calculates present value of investment

**Q**
- [QBColor](#qbcolor) - Returns RGB color code for QBasic color

**R**
- [Rate](#rate) - Returns interest rate per period
- [Replace](#replace) - Replaces substring with another substring
- [RGB](#rgb) - Returns RGB color value
- [Right](#right) - Returns rightmost characters from string
- [RightB](#rightb) - Returns rightmost bytes from string
- [RightBS](#rightbs) - Returns rightmost bytes (String version)
- [RightS](#rights) - Returns rightmost characters (String version)
- [Rnd](#rnd) - Returns random number between 0 and 1
- [Round_](#round_) - Rounds number to specified decimal places
- [RTrim](#rtrim) - Removes trailing spaces
- [RTrimS](#rtrims) - Removes trailing spaces (String version)

**S**
- [Second](#second) - Returns second component from datetime
- [Sgn](#sgn) - Returns sign of number (-1, 0, or 1)
- [Sin](#sin) - Returns sine of angle in radians
- [SLN](#sln) - Calculates straight-line depreciation
- [Space](#space) - Returns string of spaces
- [Split](#split) - Divides string into array of substrings using delimiter
- [Sqr](#sqr) - Returns square root
- [Str_](#str_) - Converts number to string
- [StrComp](#strcomp) - Compares two strings
- [StrConv](#strconv) - Converts string with specified conversion
- [String](#string) - Returns string of repeated character
- [StrReverse](#strreverse) - Reverses string
- [StrS](#strs) - Converts number to string (String version)
- [Switch](#switch) - Evaluates list of expressions and returns associated value
- [SYD](#syd) - Calculates sum-of-years' digits depreciation
- [SysCmd](#syscmd) - Executes system command

**T**
- [Tan](#tan) - Returns tangent of angle in radians
- [Time_](#time_) - Returns current system time
- [Timer](#timer) - Returns seconds since midnight
- [TimeSerial](#timeserial) - Creates time from hour, minute, second
- [TimeValue](#timevalue) - Converts time string to time
- [Trim](#trim) - Removes leading and trailing spaces
- [TrimS](#trims) - Removes leading and trailing spaces (String version)
- [TypeName](#typename) - Returns string describing variable type

**U**
- [UBound](#ubound) - Returns upper bound of array dimension
- [UCase](#ucase) - Converts string to uppercase
- [UCaseS](#ucases) - Converts string to uppercase (String version)

**V**
- [Val](#val) - Extracts numeric value from string
- [VarType](#vartype) - Returns integer indicating variable type

**W**
- [WeekDay](#weekday) - Returns day of week from date
- [WeekDayName](#weekdayname) - Returns name of weekday

**Y**
- [Year](#year) - Returns year from date

---

## Array Functions

### `Split()`

Divides string into array of substrings using delimiter.

**Parameters:**
- `expression` (str): String to divide.
- `delimiter` (str): Delimiter (default space).
- `limit` (int): Maximum number of substrings (-1 = all). Defaults to -1.
- `compare` (int): Comparison type (0=binary, 1=text). Defaults to 0.

**Returns:**
- `List[str]`: Array of substrings.

**Example:**
```python
from shortfx.fxVBA.array_functions import Split

# Basic split
print(Split("uno,dos,tres", ","))  # ['uno', 'dos', 'tres']

# Split with limit
print(Split("a b c d", " ", 2))  # ['a', 'b c d']
```

**Cost:** O(n) where n is length of expression

---

### `Join_()`

Joins array elements into string using delimiter.

**Parameters:**
- `source_array` (List[Any]): Array of elements to join.
- `delimiter` (str): Delimiter between elements (default space).

**Returns:**
- `str`: String resulting from joining elements.

**Example:**
```python
from shortfx.fxVBA.array_functions import Join_

# Join strings
print(Join_(["uno", "dos", "tres"], ","))  # 'uno,dos,tres'

# Join numbers
print(Join_([1, 2, 3], "-"))  # '1-2-3'
```

**Cost:** O(n) where n is number of elements

---

### `Filter_()`

Filters array elements that contain (or not) specific string.

**Parameters:**
- `source_array` (List[Any]): Source array.
- `match` (str): String to search for.
- `include` (bool): True to include matches, False to exclude. Defaults to True.
- `compare` (int): Comparison type (0=binary, 1=text/case-insensitive). Defaults to 0.

**Returns:**
- `List[Any]`: Filtered array.

**Example:**
```python
from shortfx.fxVBA.array_functions import Filter_

# Include matches
print(Filter_(["apple", "banana", "apricot"], "ap"))  # ['apple', 'apricot']

# Exclude matches
print(Filter_(["apple", "banana", "apricot"], "ap", False))  # ['banana']
```

**Cost:** O(n*m) where n is array size, m is length of match

---

### `LBound()`

Returns lower bound of array dimension.

**Parameters:**
- `array_var` (List[Any]): Array.
- `dimension` (int): Dimension (1-based, default 1).

**Returns:**
- `int`: Lower index (always 0 in Python).

**Raises:**
- `ValueError`: If array is empty.

**Example:**
```python
from shortfx.fxVBA.array_functions import LBound

print(LBound([1, 2, 3, 4, 5]))  # 0
print(LBound(["a", "b", "c"]))  # 0
```

**Cost:** O(1)

---

### `UBound()`

Returns upper bound of array dimension.

**Parameters:**
- `array_var` (List[Any]): Array.
- `dimension` (int): Dimension (1-based, default 1).

**Returns:**
- `int`: Upper index (length - 1 in Python).

**Raises:**
- `ValueError`: If array is empty.

**Example:**
```python
from shortfx.fxVBA.array_functions import UBound

print(UBound([1, 2, 3, 4, 5]))  # 4
print(UBound(["a", "b", "c"]))  # 2
```

**Cost:** O(1)

---

### `Array_()`

Creates array (list) with provided values.

**Parameters:**
- `*values` (Any): Values to include in array.

**Returns:**
- `List[Any]`: Array with the values.

**Example:**
```python
from shortfx.fxVBA.array_functions import Array_

print(Array_(1, 2, 3, 4, 5))  # [1, 2, 3, 4, 5]
print(Array_("rojo", "verde", "azul"))  # ['rojo', 'verde', 'azul']
```

**Cost:** O(n) where n is number of values

---

## Conversion Functions

### `CBool()`

Converts expression to Boolean.

**Parameters:**
- `expression` (Any): Expression to convert.

**Returns:**
- `bool`: Boolean value.

**Raises:**
- `ValueError`: If expression cannot be converted.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CBool

print(CBool(1))  # True
print(CBool(0))  # False
print(CBool("True"))  # True
```

**Cost:** O(1)

---

### `CByte()`

Converts number to Byte (0-255).

**Parameters:**
- `expression` (Any): Number to convert.

**Returns:**
- `int`: Value between 0 and 255.

**Raises:**
- `ValueError`: If value is out of range.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CByte

print(CByte(42))  # 42
print(CByte(255))  # 255
```

**Cost:** O(1)

---

### `CCur()`

Converts number to Currency (4 fixed decimals).

**Parameters:**
- `expression` (Any): Number to convert.

**Returns:**
- `float`: Value rounded to 4 decimals.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CCur

print(CCur(123.456789))  # 123.4568
print(CCur("99.99"))  # 99.99
```

**Cost:** O(1)

---

### `CDate()`

Converts expression to datetime.

**Parameters:**
- `expression` (Any): Expression to convert (string, number, etc.).

**Returns:**
- `datetime`: Datetime object.

**Raises:**
- `ValueError`: If cannot be converted to valid date.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CDate

print(CDate("2024-01-15"))  # datetime.datetime(2024, 1, 15, 0, 0)
```

**Cost:** O(1)

---

### `CDbl()`

Converts number to Double (double-precision floating point).

**Parameters:**
- `expression` (Any): Number to convert.

**Returns:**
- `float`: Floating point value.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CDbl

print(CDbl(42))  # 42.0
print(CDbl("3.14159"))  # 3.14159
```

**Cost:** O(1)

---

### `CDec()`

Converts number to Decimal (high precision).

**Parameters:**
- `expression` (Any): Number to convert.

**Returns:**
- `float`: Decimal value.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CDec

print(CDec("123.456"))  # 123.456
```

**Cost:** O(1)

---

### `CInt()`

Converts expression to Integer (rounds to nearest integer).

**Parameters:**
- `expression` (Any): Expression to convert.

**Returns:**
- `int`: Integer value.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CInt

print(CInt(3.7))  # 4
print(CInt(3.2))  # 3
print(CInt("42"))  # 42
```

**Cost:** O(1)

---

### `CLng()`

Converts expression to Long (long integer).

**Parameters:**
- `expression` (Any): Expression to convert.

**Returns:**
- `int`: Integer value.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CLng

print(CLng(1234567))  # 1234567
print(CLng("999999"))  # 999999
```

**Cost:** O(1)

---

### `CSng()`

Converts expression to Single (single-precision floating point).

**Parameters:**
- `expression` (Any): Expression to convert.

**Returns:**
- `float`: Floating point value.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CSng

print(CSng(42))  # 42.0
print(CSng("3.14"))  # 3.14
```

**Cost:** O(1)

---

### `CStr()`

Converts expression to text.

**Parameters:**
- `expression` (Any): Expression to convert.

**Returns:**
- `str`: Text representation.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CStr

print(CStr(42))  # '42'
print(CStr(3.14))  # '3.14'
print(CStr(True))  # 'True'
```

**Cost:** O(1)

---

### `CVar()`

Converts argument to Variant (most generic type). In Python, simply returns the value unchanged.

**Parameters:**
- `expression` (Any): Expression to convert.

**Returns:**
- `Any`: The same value.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import CVar

print(CVar(42))  # 42
print(CVar("texto"))  # 'texto'
```

**Cost:** O(1)

---

### `DateValue()`

Converts formatted string as date to date value.

**Parameters:**
- `date_str` (str): String with date format.

**Returns:**
- `date`: Date object.

**Raises:**
- `ValueError`: If string doesn't have valid format.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import DateValue

print(DateValue("2024-01-15"))  # datetime.date(2024, 1, 15)
```

**Cost:** O(1)

---

### `TimeValue()`

Converts formatted string as time to Time value.

**Parameters:**
- `time_str` (str): String with time format (HH:MM:SS).

**Returns:**
- `time`: Time object.

**Raises:**
- `ValueError`: If string doesn't have valid format.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import TimeValue

print(TimeValue("14:30:00"))  # datetime.time(14, 30)
print(TimeValue("09:15:30"))  # datetime.time(9, 15, 30)
```

**Cost:** O(1)

---

### `Val()`

Returns numeric part of string if it's at the beginning of text.

**Parameters:**
- `string` (str): String to evaluate.

**Returns:**
- `float`: Numeric value found or 0.0 if no numbers.

**Example:**
```python
from shortfx.fxVBA.conversion_functions import Val

print(Val("123.45abc"))  # 123.45
print(Val("  42  "))  # 42.0
print(Val("abc123"))  # 0.0
```

**Cost:** O(n) where n is string length

---

## Date Functions

### `Date_()`

Returns current system date.

**Returns:**
- `date`: Current date.

**Example:**
```python
from shortfx.fxVBA.date_functions import Date_

print(Date_())  # datetime.date(2024, 1, 15)
```

**Cost:** O(1)

---

### `DateAdd()`

Adds time interval to date.

**Parameters:**
- `interval` (str): Interval type (yyyy, q, m, y, d, w, ww, h, n, s).
- `number` (float): Number of intervals to add.
- `date_val` (datetime): Base date.

**Returns:**
- `datetime`: New date.

**Example:**
```python
from shortfx.fxVBA.date_functions import DateAdd
from datetime import datetime

print(DateAdd("d", 5, datetime(2024, 1, 1)))  # datetime.datetime(2024, 1, 6, 0, 0)
print(DateAdd("m", 2, datetime(2024, 1, 15)))  # datetime.datetime(2024, 3, 15, 0, 0)
```

**Cost:** O(1)

---

### `DateDiff()`

Calculates difference between two dates according to interval.

**Parameters:**
- `interval` (str): Interval type (yyyy, q, m, d, ww, h, n, s).
- `date1` (datetime): Initial date.
- `date2` (datetime): Final date.
- `first_day_of_week` (int): First day of week (0-7). Defaults to 0.
- `first_week_of_year` (int): First week of year (0-3). Defaults to 0.

**Returns:**
- `int`: Difference in specified interval.

**Example:**
```python
from shortfx.fxVBA.date_functions import DateDiff
from datetime import datetime

print(DateDiff("d", datetime(2024, 1, 1), datetime(2024, 1, 10)))  # 9
print(DateDiff("m", datetime(2024, 1, 1), datetime(2024, 6, 1)))  # 5
```

**Cost:** O(1)

---

### `DatePart()`

Extracts specific part of date.

**Parameters:**
- `interval` (str): Interval type (yyyy, q, m, y, d, w, ww, h, n, s).
- `date_val` (datetime): Date to analyze.
- `first_day_of_week` (int): First day of week. Defaults to 0.
- `first_week_of_year` (int): First week of year. Defaults to 0.

**Returns:**
- `int`: Requested date part.

**Example:**
```python
from shortfx.fxVBA.date_functions import DatePart
from datetime import datetime

print(DatePart("m", datetime(2024, 6, 15)))  # 6
print(DatePart("yyyy", datetime(2024, 6, 15)))  # 2024
```

**Cost:** O(1)

---

### `DateSerial()`

Returns date composed of indicated year, month, and day.

**Parameters:**
- `year` (int): Year.
- `month` (int): Month.
- `day` (int): Day (0 = last day of previous month).

**Returns:**
- `date`: Date object.

**Example:**
```python
from shortfx.fxVBA.date_functions import DateSerial

print(DateSerial(2024, 6, 15))  # datetime.date(2024, 6, 15)
```

**Cost:** O(1)

---

### `Day()`

Extracts day from date.

**Parameters:**
- `date_val` (datetime): Date.

**Returns:**
- `int`: Day number.

**Example:**
```python
from shortfx.fxVBA.date_functions import Day
from datetime import datetime

print(Day(datetime(2024, 6, 15)))  # 15
```

**Cost:** O(1)

---

### `Hour()`

Returns hour from DateTime expression.

**Parameters:**
- `time_val` (datetime): Date/time value.

**Returns:**
- `int`: Hour (0-23).

**Example:**
```python
from shortfx.fxVBA.date_functions import Hour
from datetime import datetime

print(Hour(datetime(2024, 1, 1, 14, 30)))  # 14
```

**Cost:** O(1)

---

### `Minute()`

Returns minutes from time expression.

**Parameters:**
- `time_val` (datetime): Date/time value.

**Returns:**
- `int`: Minutes (0-59).

**Example:**
```python
from shortfx.fxVBA.date_functions import Minute
from datetime import datetime

print(Minute(datetime(2024, 1, 1, 14, 30)))  # 30
```

**Cost:** O(1)

---

### `Month()`

Returns month number from date.

**Parameters:**
- `date_val` (datetime): Date.

**Returns:**
- `int`: Month (1-12).

**Example:**
```python
from shortfx.fxVBA.date_functions import Month
from datetime import datetime

print(Month(datetime(2024, 6, 15)))  # 6
```

**Cost:** O(1)

---

### `MonthName()`

Returns name of month.

**Parameters:**
- `month_num` (int): Month number (1-12).
- `abbreviate` (bool): If True, returns abbreviation. Defaults to False.

**Returns:**
- `str`: Month name.

**Raises:**
- `ValueError`: If month is not between 1 and 12.

**Example:**
```python
from shortfx.fxVBA.date_functions import MonthName

print(MonthName(1))  # 'January'
print(MonthName(1, True))  # 'Jan'
```

**Cost:** O(1)

---

### `Now()`

Returns current system date and time.

**Returns:**
- `datetime`: Current date and time.

**Example:**
```python
from shortfx.fxVBA.date_functions import Now

print(Now())  # datetime.datetime(2024, 1, 15, 14, 30, 0)
```

**Cost:** O(1)

---

### `Second()`

Returns seconds from time expression.

**Parameters:**
- `time_val` (datetime): Date/time value.

**Returns:**
- `int`: Seconds (0-59).

**Example:**
```python
from shortfx.fxVBA.date_functions import Second
from datetime import datetime

print(Second(datetime(2024, 1, 1, 14, 30, 45)))  # 45
```

**Cost:** O(1)

---

### `Time_()`

Returns current system time.

**Returns:**
- `time`: Current time.

**Example:**
```python
from shortfx.fxVBA.date_functions import Time_

print(Time_())  # datetime.time(14, 30, 0)
```

**Cost:** O(1)

---

### `Timer()`

Returns number of seconds elapsed since midnight.

**Returns:**
- `float`: Seconds since midnight.

**Example:**
```python
from shortfx.fxVBA.date_functions import Timer

print(Timer())  # 52200.5
```

**Cost:** O(1)

---

### `TimeSerial()`

Returns Time value passing hour, minutes, and seconds.

**Parameters:**
- `hour` (int): Hour.
- `minute` (int): Minutes.
- `second` (int): Seconds.

**Returns:**
- `time`: Time object.

**Example:**
```python
from shortfx.fxVBA.date_functions import TimeSerial

print(TimeSerial(14, 30, 0))  # datetime.time(14, 30)
```

**Cost:** O(1)

---

### `WeekDay()`

Returns number indicating day of week.

**Parameters:**
- `date_val` (datetime): Date.
- `first_day_of_week` (int): First day of week (0-7). Defaults to 1.

**Returns:**
- `int`: Day of week (1=Sunday, 2=Monday, ...).

**Example:**
```python
from shortfx.fxVBA.date_functions import WeekDay
from datetime import datetime

print(WeekDay(datetime(2024, 1, 1)))  # 2
```

**Cost:** O(1)

---

### `WeekDayName()`

Returns day of week as string.

**Parameters:**
- `weekday_num` (int): Day number (1-7).
- `abbreviate` (bool): If True, returns abbreviation. Defaults to False.
- `first_day_of_week` (int): First day of week. Defaults to 1.

**Returns:**
- `str`: Day name.

**Raises:**
- `ValueError`: If day is not between 1 and 7.

**Example:**
```python
from shortfx.fxVBA.date_functions import WeekDayName

print(WeekDayName(1))  # 'Sunday'
print(WeekDayName(2, True))  # 'Mon'
```

**Cost:** O(1)

---

### `Year()`

Returns year from date.

**Parameters:**
- `date_val` (datetime): Date.

**Returns:**
- `int`: Year.

**Example:**
```python
from shortfx.fxVBA.date_functions import Year
from datetime import datetime

print(Year(datetime(2024, 6, 15)))  # 2024
```

**Cost:** O(1)

---

## Math Functions

### `Abs_()`

Returns absolute value of a number (ignores sign).

**Parameters:**
- `number` (float): Number.

**Returns:**
- `float`: Absolute value.

**Example:**
```python
from shortfx.fxVBA.math_functions import Abs_

print(Abs_(-42))  # 42
print(Abs_(3.14))  # 3.14
```

**Cost:** O(1)

---

### `Atn()`

Returns arc tangent of a number (expressed in radians).

**Parameters:**
- `number` (float): Number.

**Returns:**
- `float`: Arc tangent in radians.

**Example:**
```python
from shortfx.fxVBA.math_functions import Atn

print(Atn(1))  # 0.7853981633974483
```

**Cost:** O(1)

---

### `Cos()`

Returns cosine of an angle.

**Parameters:**
- `number` (float): Angle in radians.

**Returns:**
- `float`: Cosine of angle.

**Example:**
```python
from shortfx.fxVBA.math_functions import Cos

print(Cos(0))  # 1.0
```

**Cost:** O(1)

---

### `Exp()`

Returns base of natural logarithms (e) raised to a power.

**Parameters:**
- `number` (float): Exponent.

**Returns:**
- `float`: e raised to number.

**Example:**
```python
from shortfx.fxVBA.math_functions import Exp

print(Exp(1))  # 2.718281828459045
```

**Cost:** O(1)

---

### `Fix()`

Returns integer part of number, truncating decimals (does not round).

**Parameters:**
- `number` (float): Number.

**Returns:**
- `int`: Integer part.

**Example:**
```python
from shortfx.fxVBA.math_functions import Fix

print(Fix(3.7))  # 3
print(Fix(-3.7))  # -3
```

**Cost:** O(1)

---

### `Int_()`

Returns integer part of number, truncating toward negative infinity.

**Parameters:**
- `number` (float): Number.

**Returns:**
- `int`: Integer part.

**Example:**
```python
from shortfx.fxVBA.math_functions import Int_

print(Int_(3.7))  # 3
print(Int_(-3.7))  # -4
```

**Cost:** O(1)

---

### `Log()`

Returns natural logarithm of a number.

**Parameters:**
- `number` (float): Number (must be positive).

**Returns:**
- `float`: Natural logarithm.

**Raises:**
- `ValueError`: If number <= 0.

**Example:**
```python
from shortfx.fxVBA.math_functions import Log

print(Log(2.718281828459045))  # 1.0
```

**Cost:** O(1)

---

### `Rnd()`

Returns random number between 0 and 1.

**Parameters:**
- `number` (int): Optional parameter (ignored in Python).

**Returns:**
- `float`: Random number [0, 1).

**Example:**
```python
from shortfx.fxVBA.math_functions import Rnd

print(Rnd())  # 0.234567 (random value)
```

**Cost:** O(1)

---

### `Round_()`

Returns number rounded to specified number of decimals.

**Parameters:**
- `number` (float): Number to round.
- `num_digits_after_decimal` (int): Number of decimals. Defaults to 0.

**Returns:**
- `float`: Rounded number.

**Example:**
```python
from shortfx.fxVBA.math_functions import Round_

print(Round_(3.14159, 2))  # 3.14
print(Round_(42.7))  # 43.0
```

**Cost:** O(1)

---

### `Sgn()`

Returns integer indicating sign of number.

**Parameters:**
- `number` (float): Number to evaluate.

**Returns:**
- `int`: 1 if positive, 0 if zero, -1 if negative.

**Example:**
```python
from shortfx.fxVBA.math_functions import Sgn

print(Sgn(42))  # 1
print(Sgn(0))  # 0
print(Sgn(-3.14))  # -1
```

**Cost:** O(1)

---

### `Sin()`

Returns sine of an angle.

**Parameters:**
- `number` (float): Angle in radians.

**Returns:**
- `float`: Sine of angle.

**Example:**
```python
from shortfx.fxVBA.math_functions import Sin

print(Sin(0))  # 0.0
```

**Cost:** O(1)

---

### `Sqr()`

Returns square root of a number.

**Parameters:**
- `number` (float): Number (must be non-negative).

**Returns:**
- `float`: Square root.

**Raises:**
- `ValueError`: If number < 0.

**Example:**
```python
from shortfx.fxVBA.math_functions import Sqr

print(Sqr(16))  # 4.0
print(Sqr(2))  # 1.4142135623730951
```

**Cost:** O(1)

---

### `Tan()`

Returns tangent of an angle.

**Parameters:**
- `number` (float): Angle in radians.

**Returns:**
- `float`: Tangent of angle.

**Example:**
```python
from shortfx.fxVBA.math_functions import Tan

print(Tan(0))  # 0.0
```

**Cost:** O(1)

---

## Logic Functions

### `Choose()`

Selects value from list based on index.

**Parameters:**
- `index_num` (int): Index (1-based) of value to choose.
- `*values` (Any): List of values.

**Returns:**
- `Any`: Value at index_num position or None if out of range.

**Example:**
```python
from shortfx.fxVBA.logic_functions import Choose

print(Choose(2, "rojo", "azul", "verde"))  # 'azul'
print(Choose(1, 10, 20, 30))  # 10
```

**Cost:** O(1)

---

### `IIf()`

Evaluates expression, returns TruePart if true, FalsePart if false.

**Parameters:**
- `expression` (bool): Boolean expression to evaluate.
- `true_part` (Any): Value to return if True.
- `false_part` (Any): Value to return if False.

**Returns:**
- `Any`: true_part or false_part depending on evaluation.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IIf

print(IIf(5 > 3, "mayor", "menor"))  # 'mayor'
print(IIf(True, 100, 200))  # 100
```

**Cost:** O(1)

---

### `IsDate()`

Evaluates if expression is a date.

**Parameters:**
- `expression` (Any): Expression to evaluate.

**Returns:**
- `bool`: True if date, False if not.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsDate
from datetime import datetime

print(IsDate(datetime(2024, 1, 1)))  # True
print(IsDate("2024-01-01"))  # False
print(IsDate(42))  # False
```

**Cost:** O(1)

---

### `IsError()`

Checks if number is an Access error number. In Python, simply checks if it's an exception.

**Parameters:**
- `number` (Any): Value to evaluate.

**Returns:**
- `bool`: True if error/exception.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsError

print(IsError(Exception("test")))  # True
print(IsError(42))  # False
```

**Cost:** O(1)

---

### `IsNull()`

Returns True if expression has null value.

**Parameters:**
- `expression` (Any): Expression to evaluate.

**Returns:**
- `bool`: True if None, False if not.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsNull

print(IsNull(None))  # True
print(IsNull(""))  # False
print(IsNull(0))  # False
```

**Cost:** O(1)

---

### `IsNumeric()`

Returns true if result of evaluating expression is numeric value.

**Parameters:**
- `expression` (Any): Expression to evaluate.

**Returns:**
- `bool`: True if numeric, False if not.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsNumeric

print(IsNumeric(42))  # True
print(IsNumeric("123"))  # True
print(IsNumeric("abc"))  # False
```

**Cost:** O(1)

---

### `Switch()`

Evaluates expression/value pairs, returns value of first true expression.

**Parameters:**
- `*args` (Any): Alternating (expression, value) pairs.

**Returns:**
- `Any`: Value associated with first true expression or None.

**Raises:**
- `ValueError`: If odd number of arguments provided.

**Example:**
```python
from shortfx.fxVBA.logic_functions import Switch

print(Switch(False, "A", True, "B", False, "C"))  # 'B'
print(Switch(1 == 2, "iguales", 1 < 2, "menor", True, "otro"))  # 'menor'
```

**Cost:** O(n) where n is number of pairs

---

### `IsArray()`

Verifies if variable is array (list, tuple).

**Parameters:**
- `variable` (Any): Variable to verify.

**Returns:**
- `bool`: True if array/list, False otherwise.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsArray

print(IsArray([1, 2, 3]))  # True
print(IsArray((1, 2, 3)))  # True
print(IsArray("texto"))  # False
```

**Cost:** O(1)

---

### `IsEmpty()`

Verifies if variable is empty or uninitialized.

**Parameters:**
- `variable` (Any): Variable to verify.

**Returns:**
- `bool`: True if empty, False otherwise.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsEmpty

print(IsEmpty(None))  # True
print(IsEmpty(""))  # True
print(IsEmpty([]))  # True
print(IsEmpty("texto"))  # False
```

**Cost:** O(1)

---

### `IsObject()`

Verifies if variable is object (has attributes/methods).

**Parameters:**
- `variable` (Any): Variable to verify.

**Returns:**
- `bool`: True if object, False otherwise.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsObject

class MiClase:
    pass

obj = MiClase()
print(IsObject(obj))  # True
print(IsObject(42))  # False
```

**Cost:** O(1)

---

### `IsMissing()`

Verifies if optional argument is absent/not provided.

**Parameters:**
- `argument` (Any): Argument to verify.

**Returns:**
- `bool`: True if None (missing), False otherwise.

**Example:**
```python
from shortfx.fxVBA.logic_functions import IsMissing

def funcion(opcional=None):
    return IsMissing(opcional)

print(funcion())  # True
print(funcion(42))  # False
```

**Cost:** O(1)

---

## Financial Functions

### `DDB()`

Calculates depreciation of an asset using double-declining balance method.

**Parameters:**
- `cost` (float): Initial cost of asset.
- `salvage` (float): Value at end of useful life.
- `life` (float): Duration of useful life.
- `period` (float): Period for which depreciation is calculated.
- `factor` (float): Depreciation rate. Defaults to 2.0.

**Returns:**
- `float`: Depreciation for specified period.

**Example:**
```python
from shortfx.fxVBA.financial_functions import DDB

print(DDB(1000, 100, 5, 1))  # 400.0
```

**Cost:** O(1)

---

### `FV()`

Calculates future value of annuity based on periodic constant payments.

**Parameters:**
- `rate` (float): Interest rate per period.
- `nper` (float): Total number of payment periods.
- `pmt` (float): Payment per period.
- `pv` (float): Present value. Defaults to 0.
- `type_` (int): Payment type (0=end of period, 1=beginning). Defaults to 0.

**Returns:**
- `float`: Future value.

**Example:**
```python
from shortfx.fxVBA.financial_functions import FV

print(FV(0.05/12, 12, -100, -1000))  # 2276.28
```

**Cost:** O(1)

---

### `IPmt()`

Returns interest payment for given period of an annuity.

**Parameters:**
- `rate` (float): Interest rate per period.
- `per` (float): Period for which interest is calculated (1 to nper).
- `nper` (float): Total number of periods.
- `pv` (float): Present value.
- `fv` (float): Future value. Defaults to 0.
- `type_` (int): Payment type (0=end, 1=beginning). Defaults to 0.

**Returns:**
- `float`: Interest payment.

**Example:**
```python
from shortfx.fxVBA.financial_functions import IPmt

print(IPmt(0.1/12, 1, 36, 8000))  # -66.67
```

**Cost:** O(1)

---

### `Pmt()`

Calculates payment for annuity based on periodic constant payments.

**Parameters:**
- `rate` (float): Interest rate per period.
- `nper` (float): Total number of periods.
- `pv` (float): Present value.
- `fv` (float): Future value. Defaults to 0.
- `type_` (int): Payment type (0=end, 1=beginning). Defaults to 0.

**Returns:**
- `float`: Payment per period.

**Example:**
```python
from shortfx.fxVBA.financial_functions import Pmt

print(Pmt(0.1/12, 36, 8000))  # -258.14
```

**Cost:** O(1)

---

### `PPmt()`

Returns principal payment for given period of an annuity.

**Parameters:**
- `rate` (float): Interest rate per period.
- `per` (float): Period (1 to nper).
- `nper` (float): Total number of periods.
- `pv` (float): Present value.
- `fv` (float): Future value. Defaults to 0.
- `type_` (int): Payment type (0=end, 1=beginning). Defaults to 0.

**Returns:**
- `float`: Principal payment.

**Example:**
```python
from shortfx.fxVBA.financial_functions import PPmt

print(PPmt(0.1/12, 1, 36, 8000))  # -191.47
```

**Cost:** O(1)

---

### `PV()`

Calculates present value of an annuity.

**Parameters:**
- `rate` (float): Interest rate per period.
- `nper` (float): Total number of periods.
- `pmt_` (float): Payment per period.
- `fv` (float): Future value. Defaults to 0.
- `type_` (int): Payment type (0=end, 1=beginning). Defaults to 0.

**Returns:**
- `float`: Present value.

**Example:**
```python
from shortfx.fxVBA.financial_functions import PV

print(PV(0.08/12, 20*12, -500))  # 59777.15
```

**Cost:** O(1)

---

### `Rate()`

Returns interest rate per period of an annuity.

**Parameters:**
- `nper` (float): Total number of periods.
- `pmt_` (float): Payment per period.
- `pv` (float): Present value.
- `fv` (float): Future value. Defaults to 0.
- `type_` (int): Payment type (0=end, 1=beginning). Defaults to 0.
- `guess` (float): Initial estimate. Defaults to 0.1.

**Returns:**
- `float`: Interest rate per period.

**Example:**
```python
from shortfx.fxVBA.financial_functions import Rate

print(Rate(60, -1000, 50000))  # 0.015
```

**Cost:** O(n) Newton-Raphson iterations

---

### `SLN()`

Calculates straight-line depreciation of an asset for one period.

**Parameters:**
- `cost` (float): Initial cost of asset.
- `salvage` (float): Value at end of useful life.
- `life` (float): Duration of useful life.

**Returns:**
- `float`: Straight-line depreciation.

**Example:**
```python
from shortfx.fxVBA.financial_functions import SLN

print(SLN(10000, 1000, 5))  # 1800.0
```

**Cost:** O(1)

---

### `SYD()`

Calculates sum-of-years' digits depreciation for a period.

**Parameters:**
- `cost` (float): Initial cost of asset.
- `salvage` (float): Value at end of useful life.
- `life` (float): Duration of useful life.
- `period` (float): Period for which to calculate.

**Returns:**
- `float`: Depreciation for the period.

**Example:**
```python
from shortfx.fxVBA.financial_functions import SYD

print(SYD(10000, 1000, 5, 1))  # 3000.0
```

**Cost:** O(1)

---

### `NPV()`

Calculates Net Present Value of cash flows.

**Parameters:**
- `rate` (float): Discount rate per period.
- `values` (List[float]): List of cash flows.

**Returns:**
- `float`: Net present value.

**Example:**
```python
from shortfx.fxVBA.financial_functions import NPV

print(NPV(0.1, [-10000, 3000, 4200, 6800]))  # 1188.44
```

**Cost:** O(n) where n is number of cash flows

---

### `IRR()`

Calculates Internal Rate of Return of cash flows.

**Parameters:**
- `values` (List[float]): List of cash flows (must include at least one negative and one positive value).
- `guess` (float): Initial estimate. Defaults to 0.1.

**Returns:**
- `float`: Internal rate of return.

**Raises:**
- `ValueError`: If doesn't converge or invalid values.

**Example:**
```python
from shortfx.fxVBA.financial_functions import IRR

print(IRR([-10000, 3000, 4200, 6800]))  # 0.1896
```

**Cost:** O(n*iterations) - iterative Newton-Raphson method

---

### `MIRR()`

Calculates Modified Internal Rate of Return.

**Parameters:**
- `values` (List[float]): List of cash flows.
- `finance_rate` (float): Interest rate for negative flows (financing).
- `reinvest_rate` (float): Interest rate for positive flows (reinvestment).

**Returns:**
- `float`: Modified internal rate of return.

**Raises:**
- `ValueError`: If requires at least one negative flow.

**Example:**
```python
from shortfx.fxVBA.financial_functions import MIRR

print(MIRR([-10000, 3000, 4200, 6800], 0.1, 0.12))  # 0.1326
```

**Cost:** O(n) where n is number of cash flows

---

### `NPer()`

Calculates number of periods for investment or loan.

**Parameters:**
- `rate` (float): Interest rate per period.
- `pmt` (float): Payment per period.
- `pv` (float): Present value.
- `fv` (float): Future value. Defaults to 0.0.
- `type_` (int): 0 = payment at end, 1 = payment at beginning. Defaults to 0.

**Returns:**
- `float`: Number of periods.

**Example:**
```python
from shortfx.fxVBA.financial_functions import NPer

print(NPer(0.01, -100, 1000, 0))  # 10.4
```

**Cost:** O(1) with logarithmic calculation

---

## Format Functions

### `Format_()`

Displays expression with determined format.

**Parameters:**
- `expression` (Any): Expression to format.
- `format_str` (str): Format string. Defaults to "".
- `first_day_of_week` (int): First day of week (0-7). Defaults to 0.
- `first_week_of_year` (int): First week of year (0-3). Defaults to 0.

**Returns:**
- `str`: Formatted expression.

**Example:**
```python
from shortfx.fxVBA.format_functions import Format_
from datetime import datetime

print(Format_(datetime(2024, 1, 15), "yyyy-mm-dd"))  # '2024-01-15'
print(Format_(1234.56, "0.00"))  # '1234.56'
```

**Cost:** O(n) where n is format length

---

### `FormatCurrency()`

Returns expression formatted as currency value.

**Parameters:**
- `expression` (float): Number to format.
- `num_decimals` (int): Number of decimals. Defaults to 2.
- `include_leading_digit` (int): Include leading digit (-1=True, 0=False, -2=config). Defaults to -2.
- `use_parens_for_negative` (int): Parentheses for negatives. Defaults to -2.
- `group_digits` (int): Use thousands separators. Defaults to -2.

**Returns:**
- `str`: Value formatted as currency.

**Example:**
```python
from shortfx.fxVBA.format_functions import FormatCurrency

print(FormatCurrency(1234.56))  # '$1,234.56'
print(FormatCurrency(-42.5))  # '($42.50)'
```

**Cost:** O(1)

---

### `FormatDateTime()`

Returns string based on expression, formatted as date.

**Parameters:**
- `expression` (datetime): Date to format.
- `named_format` (int): Format (0=general, 1=long date, 2=short date, 3=long time, 4=short time). Defaults to 0.

**Returns:**
- `str`: Formatted date.

**Example:**
```python
from shortfx.fxVBA.format_functions import FormatDateTime
from datetime import datetime

print(FormatDateTime(datetime(2024, 1, 15, 14, 30), 0))  # '2024-01-15 14:30:00'
print(FormatDateTime(datetime(2024, 1, 15), 2))  # '01/15/2024'
```

**Cost:** O(1)

---

### `FormatNumber()`

Returns expression formatted as number.

**Parameters:**
- `expression` (float): Number to format.
- `num_decimals` (int): Number of decimals. Defaults to 2.
- `include_leading_digit` (int): Include leading digit. Defaults to -2.
- `use_parens_for_negative` (int): Parentheses for negatives. Defaults to -2.
- `group_digits` (int): Use thousands separators. Defaults to -2.

**Returns:**
- `str`: Formatted number.

**Example:**
```python
from shortfx.fxVBA.format_functions import FormatNumber

print(FormatNumber(1234.5678, 2))  # '1,234.57'
print(FormatNumber(-42.5))  # '(42.50)'
```

**Cost:** O(1)

---

### `FormatPercent()`

Returns expression formatted as percentage (multiplied by 100).

**Parameters:**
- `expression` (float): Number to format (0.25 = 25%).
- `num_decimals` (int): Number of decimals. Defaults to 2.
- `include_leading_digit` (int): Include leading digit. Defaults to -2.
- `use_parens_for_negative` (int): Parentheses for negatives. Defaults to -2.
- `group_digits` (int): Use thousands separators. Defaults to -2.

**Returns:**
- `str`: Formatted percentage.

**Example:**
```python
from shortfx.fxVBA.format_functions import FormatPercent

print(FormatPercent(0.25))  # '25.00%'
print(FormatPercent(-0.1234, 1))  # '(12.3%)'
```

**Cost:** O(1)

---

## Miscellaneous Functions

### `AccessError()`

Returns description associated with Access/DAO error.

**Parameters:**
- `error_number` (int): Access/DAO error code.

**Returns:**
- `str`: Error description.

**Raises:**
- `NotImplementedError`: When not running in Access/DAO.

**Example:**
```python
from shortfx.fxVBA.misc_functions import AccessError

# Only available in Microsoft Access
print(AccessError(3024))  # Raises NotImplementedError
```

**Cost:** N/A - Access only

---

### `CurrentUser()`

Returns name of current Access database user.

**Returns:**
- `str`: User name.

**Raises:**
- `NotImplementedError`: When not running in Access.

**Example:**
```python
from shortfx.fxVBA.misc_functions import CurrentUser

# Only available in Microsoft Access
print(CurrentUser())  # Raises NotImplementedError
```

**Cost:** N/A - Access only

---

### `Eval_()`

Interprets/evaluates numeric expression or embedded function. Returns value of reference to Access object.

**Parameters:**
- `expression` (str): VBA/Access expression to evaluate.

**Returns:**
- `Any`: Evaluation result.

**Raises:**
- `NotImplementedError`: When not running in Access.

**Example:**
```python
from shortfx.fxVBA.misc_functions import Eval_

# Only available in Microsoft Access
print(Eval_("Forms!Main!Caption"))  # Raises NotImplementedError
```

**Cost:** N/A - Access only

---

### `Hex_()`

Returns string equivalent to hexadecimal value of number.

**Parameters:**
- `number` (int): Number to convert.

**Returns:**
- `str`: Hexadecimal representation (without 0x prefix).

**Example:**
```python
from shortfx.fxVBA.misc_functions import Hex_

print(Hex_(255))  # 'FF'
print(Hex_(16))  # '10'
```

**Cost:** O(log n) where n is the number

---

### `Oct_()`

Returns string representing octal value of number.

**Parameters:**
- `number` (int): Number to convert.

**Returns:**
- `str`: Octal representation (without 0o prefix).

**Example:**
```python
from shortfx.fxVBA.misc_functions import Oct_

print(Oct_(8))  # '10'
print(Oct_(64))  # '100'
```

**Cost:** O(log n) where n is the number

---

### `SysCmd()`

Executes Access system command.

**Parameters:**
- `action` (int): Access SysCmd action code.
- `argument2` (Optional[int]): Optional integer argument.
- `argument3` (Optional[str]): Optional string argument.

**Returns:**
- `Any`: Result according to action.

**Raises:**
- `NotImplementedError`: When not running in Access.

**Example:**
```python
from shortfx.fxVBA.misc_functions import SysCmd

# Only available in Microsoft Access
print(SysCmd(7))  # Raises NotImplementedError
```

**Cost:** N/A - Access only

---

### `RGB()`

Returns integer value representing RGB color.

**Parameters:**
- `red` (int): Red component (0-255).
- `green` (int): Green component (0-255).
- `blue` (int): Blue component (0-255).

**Returns:**
- `int`: RGB value as integer (VBA format).

**Raises:**
- `ValueError`: If RGB values not between 0 and 255.

**Example:**
```python
from shortfx.fxVBA.misc_functions import RGB

print(RGB(255, 0, 0))  # 255 (Red)
print(RGB(0, 255, 0))  # 65280 (Green)
print(RGB(0, 0, 255))  # 16711680 (Blue)
```

**Cost:** O(1)

---

### `QBColor()`

Returns RGB value corresponding to QuickBasic color code.

**Parameters:**
- `color` (int): QuickBasic color code (0-15).

**Returns:**
- `int`: RGB value.

**Example:**
```python
from shortfx.fxVBA.misc_functions import QBColor

print(QBColor(0))  # 0 (Black)
print(QBColor(4))  # 255 (Red)
print(QBColor(15))  # 16777215 (Bright White)
```

**Cost:** O(1)

---

## System Functions

### BuildCriteria

Construye una cadena de criterio SQL basada en un campo, tipo y expresión.

**Parameters:**
- `field` (str): Nombre del campo para el criterio
- `field_type` (str): Tipo de datos del campo ('Text', 'Date', 'Number')
- `expression` (str): Expresión para el criterio

**Returns:**
- `str`: Cadena de criterio SQL formateada

**Example:**
```python
# Text field
print(BuildCriteria("Name", "Text", "John"))  # "[Name] = 'John'"

# Date field
print(BuildCriteria("BirthDate", "Date", "1990-01-01"))  # "[BirthDate] = #1990-01-01#"

# Number field
print(BuildCriteria("Age", "Number", "25"))  # "[Age] = 25"
```

**Cost:** O(1) string concatenation

---

### Command

Devuelve los argumentos de la línea de comandos.

**Parameters:**
- Ninguno

**Returns:**
- `str`: Argumentos de línea de comandos

**Example:**
```python
args = Command()
print(f"Arguments: {args}")
```

**Cost:** O(n) donde n es la cantidad de argumentos

---

### CurDir

Devuelve el directorio actual para la unidad especificada.

**Parameters:**
- `drive` (Optional[str], default=""): Letra de unidad (opcional)

**Returns:**
- `str`: Ruta del directorio actual

**Example:**
```python
# Current directory
print(CurDir())  # "C:\\Users\\username"

# Specific drive
print(CurDir("D"))  # "D:\\"
```

**Cost:** O(1) llamada al sistema

---

### Dir_

Devuelve el nombre de archivo o directorio que coincide con el patrón especificado.

**Parameters:**
- `pathname` (str, default=""): Patrón de búsqueda (puede incluir comodines)
- `attributes` (int, default=0): Atributos de archivo a incluir

**Returns:**
- `str`: Nombre del archivo/directorio encontrado, cadena vacía si no hay más

**Example:**
```python
# Find first .txt file
filename = Dir_("*.txt")
while filename:
    print(filename)
    filename = Dir_()  # Get next file
```

**Cost:** O(n) donde n es el número de archivos que coinciden

---

### Environ

Devuelve el valor de una variable de entorno por nombre o número.

**Parameters:**
- `var` (Union[str, int]): Nombre o número de la variable de entorno

**Returns:**
- `str`: Valor de la variable de entorno

**Example:**
```python
# By name
print(Environ("USERNAME"))  # "current_user"

# By number
print(Environ(1))  # Primera variable de entorno
```

**Cost:** O(1) para nombre, O(n) para número

---

### EnvironS

Devuelve el valor de una variable de entorno por nombre (solo cadenas).

**Parameters:**
- `name` (str): Nombre de la variable de entorno

**Returns:**
- `str`: Valor de la variable de entorno o cadena vacía si no existe

**Example:**
```python
print(EnvironS("PATH"))  # "/usr/bin:/usr/local/bin..."
print(EnvironS("NONEXISTENT"))  # ""
```

**Cost:** O(1) búsqueda en diccionario

---

### Error

Devuelve el mensaje de error para un número de error especificado.

**Parameters:**
- `errornumber` (int): Número de error VBA

**Returns:**
- `str`: Mensaje de error correspondiente

**Example:**
```python
print(Error(5))  # "Invalid procedure call or argument"
print(Error(11))  # "Division by zero"
print(Error(9999))  # "Unknown error"
```

**Cost:** O(1) búsqueda en diccionario

---

### FileDateTime

Devuelve la fecha y hora de la última modificación de un archivo.

**Parameters:**
- `pathname` (str): Ruta del archivo

**Returns:**
- `datetime`: Fecha/hora de la última modificación

**Example:**
```python
dt = FileDateTime("document.txt")
print(dt)  # 2024-01-15 14:30:25
```

**Cost:** O(1) llamada al sistema

---

### FileLen

Devuelve el tamaño de un archivo en bytes.

**Parameters:**
- `pathname` (str): Ruta del archivo

**Returns:**
- `int`: Tamaño del archivo en bytes

**Example:**
```python
size = FileLen("document.txt")
print(f"Size: {size} bytes")  # Size: 1024 bytes
```

**Cost:** O(1) llamada al sistema

---

### GetAttr_

Devuelve los atributos de un archivo o directorio.

**Parameters:**
- `pathname` (str): Ruta del archivo/directorio

**Returns:**
- `int`: Valor de atributos combinados

**Example:**
```python
attr = GetAttr_("document.txt")
if attr & 1:  # VbReadOnly
    print("File is read-only")
if attr & 2:  # VbHidden
    print("File is hidden")
```

**Cost:** O(1) llamada al sistema

---

### Nz

Devuelve un valor alternativo si la expresión es None/NULL.

**Parameters:**
- `value` (Any): Valor a evaluar
- `value_if_null` (Any, default=""): Valor a devolver si value es None

**Returns:**
- `Any`: value si no es None, sino value_if_null

**Example:**
```python
print(Nz(None, "N/A"))  # "N/A"
print(Nz("Hello", "N/A"))  # "Hello"
print(Nz(None))  # ""
print(Nz(0, -1))  # 0 (cero no es None)
```

**Cost:** O(1) comparación

---

### Partition

Devuelve una cadena que indica dónde cae un número dentro de una serie de rangos.

**Parameters:**
- `number` (int): Número a evaluar
- `start` (int): Inicio del rango
- `stop` (int): Final del rango
- `interval` (int): Tamaño del intervalo

**Returns:**
- `str`: Cadena que describe el rango (formato "low:high")

**Example:**
```python
print(Partition(20, 0, 100, 10))  # " 20: 29"
print(Partition(5, 0, 100, 10))   # "  0:  9"
print(Partition(95, 0, 100, 10))  # " 90: 99"
print(Partition(105, 0, 100, 10)) # "100:   "
```

**Cost:** O(1) cálculo aritmético

---

### TypeName

Devuelve el nombre del tipo de datos de una variable.

**Parameters:**
- `varname` (Any): Variable a evaluar

**Returns:**
- `str`: Nombre del tipo ("Integer", "String", "Boolean", etc.)

**Example:**
```python
print(TypeName(42))        # "Integer"
print(TypeName(3.14))      # "Double"
print(TypeName("Hello"))   # "String"
print(TypeName(True))      # "Boolean"
print(TypeName([1,2,3]))   # "List"
print(TypeName(None))      # "Null"
```

**Cost:** O(1) determinación de tipo

---

### VarType

Devuelve un código que indica el tipo de datos de una variable.

**Parameters:**
- `varname` (Any): Variable a evaluar

**Returns:**
- `int`: Código de tipo VBA (VbVarType)

**Example:**
```python
print(VarType(42))        # 2 (vbInteger)
print(VarType(3.14))      # 5 (vbDouble)
print(VarType("Hello"))   # 8 (vbString)
print(VarType(True))      # 11 (vbBoolean)
print(VarType(None))      # 1 (vbNull)
```

**Cost:** O(1) determinación de tipo

---

## String Functions

### Asc

Retorna código ASCII/Unicode del primer carácter de la cadena.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `int`: Código ASCII/Unicode del primer carácter

**Example:**
```python
print(Asc("A"))     # 65
print(Asc("Hola"))  # 72
```

**Cost:** O(1)

---

### AscB

Retorna código del primer byte de la cadena.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `int`: Código del primer byte

**Example:**
```python
print(AscB("A"))  # 65
```

**Cost:** O(1)

---

### Chr_

Retorna carácter asociado con código de carácter especificado.

**Parameters:**
- `char_code` (int): Código ASCII/Unicode

**Returns:**
- `str`: Carácter correspondiente

**Example:**
```python
print(Chr_(65))  # 'A'
print(Chr_(72))  # 'H'
```

**Cost:** O(1)

---

### ChrS

Retorna carácter asociado con código (versión $, idéntica en Python).

**Parameters:**
- `char_code` (int): Código ASCII/Unicode

**Returns:**
- `str`: Carácter correspondiente

**Example:**
```python
print(ChrS(65))  # 'A'
```

**Cost:** O(1)

---

### ChrW

Retorna carácter Unicode asociado con código especificado.

**Parameters:**
- `char_code` (int): Código Unicode

**Returns:**
- `str`: Carácter Unicode

**Example:**
```python
print(ChrW(8364))  # '€'
```

**Cost:** O(1)

---

### ChrWS

Retorna carácter Unicode (versión $, idéntica en Python).

**Parameters:**
- `char_code` (int): Código Unicode

**Returns:**
- `str`: Carácter Unicode

**Example:**
```python
print(ChrWS(8364))  # '€'
```

**Cost:** O(1)

---

### InStr

Retorna posición de una cadena dentro de otra (1-based).

**Parameters:**
- `start` (int, default=1): Posición inicial (1-based)
- `string1` (str, default=""): Cadena donde buscar
- `string2` (str, default=""): Cadena a buscar
- `compare` (int, default=0): Tipo de comparación (0=binario, 1=texto)

**Returns:**
- `int`: Posición donde se encuentra (1-based) o 0 si no se encuentra

**Example:**
```python
print(InStr(1, "Hola mundo", "mundo"))  # 6
print(InStr(1, "Hola", "x"))            # 0
```

**Cost:** O(n*m) donde n=len(string1), m=len(string2)

---

### InStrRev

Retorna posición de cadena buscando desde el final.

**Parameters:**
- `string1` (str): Cadena donde buscar
- `string2` (str): Cadena a buscar
- `start` (int, default=-1): Posición inicial desde final (-1 = desde el final)
- `compare` (int, default=0): Tipo de comparación (0=binario, 1=texto)

**Returns:**
- `int`: Posición donde se encuentra (1-based) o 0

**Example:**
```python
print(InStrRev("Hola mundo mundo", "mundo"))  # 12
```

**Cost:** O(n*m) donde n=len(string1), m=len(string2)

---

### LCase

Convierte cadena a minúsculas.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena en minúsculas

**Example:**
```python
print(LCase("HOLA"))  # 'hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### LCaseS

Convierte cadena a minúsculas (versión $).

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena en minúsculas

**Example:**
```python
print(LCaseS("HOLA"))  # 'hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### Left

Retorna porción de cadena desde la izquierda.

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de caracteres a extraer

**Returns:**
- `str`: Subcadena desde la izquierda

**Example:**
```python
print(Left("Hola mundo", 4))  # 'Hola'
```

**Cost:** O(n) donde n es length

---

### LeftS

Retorna porción de cadena desde la izquierda (versión $).

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de caracteres a extraer

**Returns:**
- `str`: Subcadena desde la izquierda

**Example:**
```python
print(LeftS("Hola mundo", 4))  # 'Hola'
```

**Cost:** O(n) donde n es length

---

### LeftB

Retorna porción de cadena (en bytes) desde la izquierda.

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de bytes a extraer

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(LeftB("Hola", 4))  # 'Hol'
```

**Cost:** O(n) donde n es length

---

### LeftBS

Retorna porción de cadena en bytes (versión $).

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de bytes a extraer

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(LeftBS("Hola", 4))  # 'Hol'
```

**Cost:** O(n) donde n es length

---

### Len_

Cuenta número de caracteres de una cadena.

**Parameters:**
- `expression` (str): Cadena a medir

**Returns:**
- `int`: Longitud en caracteres

**Example:**
```python
print(Len_("Hola mundo"))  # 10
```

**Cost:** O(1)

---

### LenB

Cuenta número de bytes de una cadena.

**Parameters:**
- `expression` (str): Cadena a medir

**Returns:**
- `int`: Longitud en bytes

**Example:**
```python
print(LenB("Hola"))  # 8
```

**Cost:** O(n) donde n es longitud de la cadena

---

### LTrim

Retorna cadena sin espacios a la izquierda.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena sin espacios a la izquierda

**Example:**
```python
print(LTrim("   Hola"))  # 'Hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### LTrimS

Retorna cadena sin espacios a la izquierda (versión $).

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena sin espacios a la izquierda

**Example:**
```python
print(LTrimS("   Hola"))  # 'Hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### Mid

Retorna fracción de cadena definida por posición inicio y longitud.

**Parameters:**
- `string` (str): Cadena de entrada
- `start` (int): Posición inicial (1-based)
- `length` (int, default=None): Longitud a extraer (None = hasta el final)

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(Mid("Hola mundo", 6, 5))  # 'mundo'
```

**Cost:** O(n) donde n es length

---

### MidS

Retorna fracción de cadena (versión $).

**Parameters:**
- `string` (str): Cadena de entrada
- `start` (int): Posición inicial (1-based)
- `length` (int, default=None): Longitud a extraer

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(MidS("Hola mundo", 6, 5))  # 'mundo'
```

**Cost:** O(n) donde n es length

---

### MidB

Retorna fracción (byte) de cadena.

**Parameters:**
- `string` (str): Cadena de entrada
- `start` (int): Posición inicial en bytes (1-based)
- `length` (int, default=None): Longitud en bytes

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(MidB("Hola", 3, 4))  # 'la'
```

**Cost:** O(n) donde n es length

---

### MidBS

Retorna fracción (byte) de cadena (versión $).

**Parameters:**
- `string` (str): Cadena de entrada
- `start` (int): Posición inicial en bytes
- `length` (int, default=None): Longitud en bytes

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(MidBS("Hola", 3, 4))  # 'la'
```

**Cost:** O(n) donde n es length

---

### Replace

Retorna cadena donde subcadena se reemplaza por otra.

**Parameters:**
- `expression` (str): Cadena original
- `find` (str): Subcadena a buscar
- `replace_with` (str): Subcadena de reemplazo
- `start` (int, default=1): Posición inicial (1-based)
- `count` (int, default=-1): Número de reemplazos (-1 = todos)
- `compare` (int, default=0): Tipo de comparación (0=binario, 1=texto)

**Returns:**
- `str`: Cadena con reemplazos

**Example:**
```python
print(Replace("Hola mundo mundo", "mundo", "Python"))  # 'Hola Python Python'
```

**Cost:** O(n*m) donde n=len(expression), m=número de reemplazos

---

### Right

Retorna porción de cadena desde la derecha.

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de caracteres a extraer

**Returns:**
- `str`: Subcadena desde la derecha

**Example:**
```python
print(Right("Hola mundo", 5))  # 'mundo'
```

**Cost:** O(n) donde n es length

---

### RightS

Retorna porción de cadena desde la derecha (versión $).

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de caracteres a extraer

**Returns:**
- `str`: Subcadena desde la derecha

**Example:**
```python
print(RightS("Hola mundo", 5))  # 'mundo'
```

**Cost:** O(n) donde n es length

---

### RightB

Retorna porción de cadena (en bytes) desde la derecha.

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de bytes a extraer

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(RightB("Hola", 4))  # 'la'
```

**Cost:** O(n) donde n es length

---

### RightBS

Retorna porción de cadena en bytes (versión $).

**Parameters:**
- `string` (str): Cadena de entrada
- `length` (int): Número de bytes a extraer

**Returns:**
- `str`: Subcadena

**Example:**
```python
print(RightBS("Hola", 4))  # 'la'
```

**Cost:** O(n) donde n es length

---

### RTrim

Recorta espacios a la derecha de una cadena.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena sin espacios a la derecha

**Example:**
```python
print(RTrim("Hola   "))  # 'Hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### RTrimS

Recorta espacios a la derecha (versión $).

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena sin espacios a la derecha

**Example:**
```python
print(RTrimS("Hola   "))  # 'Hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### Space

Retorna cadena con número de espacios indicado.

**Parameters:**
- `number` (int): Número de espacios

**Returns:**
- `str`: Cadena con espacios

**Example:**
```python
print(Space(5))  # '     '
```

**Cost:** O(n) donde n es number

---

### Str_

Convierte número en cadena.

**Parameters:**
- `number` (float): Número a convertir

**Returns:**
- `str`: Representación en cadena

**Example:**
```python
print(Str_(42))  # '42'
```

**Cost:** O(1)

---

### StrS

Convierte número en cadena (versión $).

**Parameters:**
- `number` (float): Número a convertir

**Returns:**
- `str`: Representación en cadena

**Example:**
```python
print(StrS(42))  # '42'
```

**Cost:** O(1)

---

### StrComp

Compara dos cadenas y retorna resultado.

**Parameters:**
- `string1` (str): Primera cadena
- `string2` (str): Segunda cadena
- `compare` (int, default=0): Tipo de comparación (0=binario, 1=texto)

**Returns:**
- `int`: -1 si string1<string2, 0 si iguales, 1 si string1>string2

**Example:**
```python
print(StrComp("abc", "ABC", 0))  # 1
print(StrComp("abc", "ABC", 1))  # 0
```

**Cost:** O(n) donde n es longitud mínima de las cadenas

---

### StrConv

Convierte cadena según parámetro de conversión.

**Parameters:**
- `string` (str): Cadena a convertir
- `conversion` (int): Tipo conversión (1=mayús, 2=minús, 3=primera letra mayús, 64=Unicode, 128=desde Unicode)
- `lcid` (int, default=None): ID de configuración regional (opcional)

**Returns:**
- `str`: Cadena convertida

**Example:**
```python
print(StrConv("hola mundo", 1))  # 'HOLA MUNDO'
print(StrConv("HOLA MUNDO", 2))  # 'hola mundo'
print(StrConv("hola mundo", 3))  # 'Hola Mundo'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### String

Retorna carácter o cadena que se repite n veces.

**Parameters:**
- `number` (int): Número de repeticiones
- `character` (str): Carácter o cadena a repetir

**Returns:**
- `str`: Cadena repetida

**Example:**
```python
print(String(5, "x"))    # 'xxxxx'
print(String(3, "AB"))   # 'ABABAB'
```

**Cost:** O(n) donde n es number

---

### StrReverse

Retorna cadena invertida.

**Parameters:**
- `expression` (str): Cadena a invertir

**Returns:**
- `str`: Cadena invertida

**Example:**
```python
print(StrReverse("Hola"))  # 'aloH'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### Trim

Recorta espacios a izquierda y derecha de cadena.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena sin espacios en los extremos

**Example:**
```python
print(Trim("  Hola  "))  # 'Hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### TrimS

Recorta espacios a izquierda y derecha (versión $).

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena sin espacios en los extremos

**Example:**
```python
print(TrimS("  Hola  "))  # 'Hola'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### UCase

Convierte cadena a mayúsculas.

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena en mayúsculas

**Example:**
```python
print(UCase("hola"))  # 'HOLA'
```

**Cost:** O(n) donde n es longitud de la cadena

---

### UCaseS

Convierte cadena a mayúsculas (versión $).

**Parameters:**
- `string` (str): Cadena de entrada

**Returns:**
- `str`: Cadena en mayúsculas

**Example:**
```python
print(UCaseS("hola"))  # 'HOLA'
```

**Cost:** O(n) donde n es longitud de la cadena

---

