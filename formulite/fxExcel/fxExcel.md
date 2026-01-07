# FormuLite - fxExcel Functions Documentation

## Overview

The `fxExcel` module provides Excel-compatible functions for FormuLite. These functions replicate Excel's behavior across multiple categories:
- **Date and Time Functions**: Serial number system and calculation methods
- **Engineering Functions**: Bessel functions, base conversions, bitwise operations, complex numbers, error functions
- **Database Functions**: Statistical and aggregate operations on structured data
- **Financial Functions**: Bond pricing, depreciation, loan payments, yield calculations
- **Information Functions**: Data type validation and error handling
- **Logic Functions**: Logical operations, conditional evaluation, lambda functions
- **Math & Trigonometry Functions**: Mathematical operations, trigonometric functions, rounding, number theory
- **Statistical Functions**: Distributions, correlations, forecasting, regression, confidence intervals
- **Text & Data Functions**: Text manipulation, concatenation, search, replacement, formatting, type conversion

## Module Structure

- **date_formulas.py**: Excel-compatible date and time functions
- **engineering_formulas.py**: Excel-compatible engineering functions
- **database_formulas.py**: Excel-compatible database functions
- **financial_formulas.py**: Excel-compatible financial functions
- **logic_formulas.py**: Excel-compatible logic and conditional functions
- **information_formulas.py**: Excel-compatible information and validation functions
- **math_formulas.py**: Excel-compatible mathematical and trigonometric functions
- **statistic_formulas.py**: Excel-compatible statistical and forecasting functions
- **text_formulas.py**: Excel-compatible text and data manipulation functions

## Table of Contents

- [Function Categories](#function-categories)
  - [Date Functions](#date-functions)
  - [Engineering Functions](#engineering-functions)
  - [Database Functions](#database-functions)
  - [Financial Functions](#financial-functions)
  - [Information Functions](#information-functions)
  - [Logic Functions](#logic-functions)
  - [Math & Trigonometry Functions](#math--trigonometry-functions)
  - [Statistical Functions](#statistical-functions)
  - [Text & Data Functions](#text--data-functions)
- [Function Index](#function-index)
- [Credits](#credits)

---

## Function Categories

### Date Functions
- [DATE](#date) - Returns the serial number of a specific date
- [DATEDIF](#datedif) - Calculates the difference between dates in days, months, or years
- [DATEVALUE](#datevalue) - Converts a date in text format to a serial number
- [DAY](#day) - Converts a serial number to a day of the month
- [DAYS](#days) - Returns the number of days between two dates
- [DAYS360](#days360) - Calculates the number of days between two dates based on a 360-day year
- [EDATE](#edate) - Returns the serial number of a date months before or after
- [EOMONTH](#eomonth) - Returns the serial number of the last day of the month
- [HOUR](#hour) - Converts a serial number to an hour
- [ISOWEEKNUM](#isoweeknum) - Returns the ISO week number
- [MINUTE](#minute) - Converts a serial number to a minute
- [MONTH](#month) - Converts a serial number to a month
- [NETWORKDAYS](#networkdays) - Returns the number of working days between two dates
- [NETWORKDAYS_INTL](#networkdays_intl) - Returns working days between two dates with custom weekend parameters
- [NOW](#now) - Returns the serial number of the current date and time
- [SECOND](#second) - Converts a serial number to a second
- [TIME](#time) - Returns the serial number of a specific time
- [TIMEVALUE](#timevalue) - Converts a time in text format to a serial number
- [TODAY](#today) - Returns the serial number of today's date
- [WEEKDAY](#weekday) - Converts a serial number to a day of the week
- [WEEKNUM](#weeknum) - Converts a serial number to a week number
- [WORKDAY](#workday) - Returns the date after a number of working days
- [WORKDAY_INTL](#workday_intl) - Returns the date after working days with custom weekends
- [YEAR](#year) - Converts a serial number to a year
- [YEARFRAC](#yearfrac) - Returns the fraction of year between two dates
- [excel_serial_to_year](#excel_serial_to_year) - Extracts the year from an Excel-style serial number or datetime
- [excel_serial_to_month](#excel_serial_to_month) - Extracts the month from an Excel-style serial number or datetime
- [excel_serial_to_day](#excel_serial_to_day) - Converts a serial number or datetime to day of the month
- [excel_serial_to_weekday](#excel_serial_to_weekday) - Converts a serial number or datetime to day of the week
- [excel_serial_to_hour](#excel_serial_to_hour) - Extracts the hour component from an Excel-style serial number or datetime
- [excel_serial_to_minute](#excel_serial_to_minute) - Extracts the minute component from an Excel-style serial number or datetime

### Engineering Functions
- [BESSELI](#besseli) - Returns the modified Bessel function In(x)
- [BESSELJ](#besselj) - Returns the Bessel function Jn(x)
- [BESSELK](#besselk) - Returns the modified Bessel function Kn(x)
- [BESSELY](#bessely) - Returns the Bessel function Yn(x)
- [BIN2DEC](#bin2dec) - Converts a binary string to decimal
- [BIN2HEX](#bin2hex) - Converts a binary string to hexadecimal
- [BIN2OCT](#bin2oct) - Converts a binary string to octal
- [DEC2BIN](#dec2bin) - Converts a decimal number to binary
- [DEC2HEX](#dec2hex) - Converts a decimal number to hexadecimal
- [DEC2OCT](#dec2oct) - Converts a decimal number to octal
- [HEX2BIN](#hex2bin) - Converts a hexadecimal string to binary
- [HEX2DEC](#hex2dec) - Converts a hexadecimal string to decimal
- [HEX2OCT](#hex2oct) - Converts a hexadecimal string to octal
- [OCT2BIN](#oct2bin) - Converts an octal string to binary
- [OCT2DEC](#oct2dec) - Converts an octal string to decimal
- [OCT2HEX](#oct2hex) - Converts an octal string to hexadecimal
- [BITAND](#bitand) - Performs a bitwise AND on two numbers
- [BITOR](#bitor) - Performs a bitwise OR on two numbers
- [BITXOR](#bitxor) - Performs a bitwise XOR on two numbers
- [BITLSHIFT](#bitlshift) - Performs a left shift on a number
- [BITRSHIFT](#bitrshift) - Performs a right shift on a number
- [COMPLEX](#complex) - Creates a complex number from real and imaginary coefficients
- [IMABS](#imabs) - Returns the absolute value (modulus) of a complex number
- [IMAGINARY](#imaginary) - Returns the imaginary part of a complex number
- [IMREAL](#imreal) - Returns the real part of a complex number
- [IMARGUMENT](#imargument) - Returns the argument (angle in radians) of a complex number
- [IMCONJUGATE](#imconjugate) - Returns the complex conjugate
- [IMCOS](#imcos) - Cosine of complex number
- [IMCOSH](#imcosh) - Hyperbolic cosine of complex number
- [IMSIN](#imsin) - Sine of complex number
- [IMSINH](#imsinh) - Hyperbolic sine of complex number
- [IMTAN](#imtan) - Tangent of complex number
- [IMCOT](#imcot) - Cotangent of complex number
- [IMCSC](#imcsc) - Cosecant of complex number
- [IMCSCH](#imcsch) - Hyperbolic cosecant of complex number
- [IMSEC](#imsec) - Secant of complex number
- [IMSECH](#imsech) - Hyperbolic secant of complex number
- [IMEXP](#imexp) - Exponential of complex number
- [IMLN](#imln) - Natural logarithm of complex number
- [IMLOG10](#imlog10) - Base-10 logarithm of complex number
- [IMLOG2](#imlog2) - Base-2 logarithm of complex number
- [IMPOWER](#impower) - Returns a complex number raised to a power
- [IMSQRT](#imsqrt) - Returns the square root of a complex number
- [IMDIV](#imdiv) - Returns the quotient of two complex numbers
- [IMPRODUCT](#improduct) - Returns the product of complex numbers
- [IMSUB](#imsub) - Returns the difference between two complex numbers
- [IMSUM](#imsum) - Returns the sum of complex numbers
- [ERF](#erf) - Returns the error function erf(x)
- [ERFC](#erfc) - Returns the complementary error function erfc(x)
- [ERF_PRECISE](#erf_precise) - Precise version of error function
- [ERFC_PRECISE](#erfc_precise) - Precise version of complementary error function
- [CONVERT](#convert) - Converts a number from one measurement unit to another
- [DELTA](#delta) - Tests whether two values are equal
- [GESTEP](#gestep) - Tests whether a number is greater than or equal to a threshold

### Database Functions
- [DCOUNT](#dcount) - Counts cells containing numbers in a database field that match criteria
- [DCOUNTA](#dcounta) - Counts non-empty cells in a database field that match criteria
- [DAVERAGE](#daverage) - Calculates the average of database field values matching criteria
- [DSUM](#dsum) - Sums values from database field that match criteria
- [DPRODUCT](#dproduct) - Multiplies values from database field that match criteria
- [DMAX](#dmax) - Returns the maximum value from database field values matching criteria
- [DMIN](#dmin) - Returns the minimum value from database field values matching criteria
- [DSTDEV](#dstdev) - Calculates the sample standard deviation of database field values matching criteria
- [DSTDEVP](#dstdevp) - Calculates the population standard deviation of database field values matching criteria
- [DVAR](#dvar) - Calculates the sample variance of database field values matching criteria
- [DVARP](#dvarp) - Calculates the population variance of database field values matching criteria
- [DGET](#dget) - Extracts a single value from a database field that matches criteria

### Financial Functions
- [ACCRINT](#accrint) - Return the accrued interest for a security that pays periodic interest
- [ACCRINTM](#accrintm) - Return the accrued interest for a security that pays interest at maturity
- [AMORLINC](#amorlinc) - Calculate depreciation for each accounting period using a depreciation coefficient
- [COUPDAYS](#coupdays) - Return the number of days in the coupon period containing the settlement date
- [COUPDAYBS](#coupdaybs) - Return the number of days from the beginning of the coupon period to the settlement date
- [COUPDAYSNC](#coupdaysnc) - Return the number of days from the settlement date to the next coupon date
- [COUPPCD](#couppcd) - Return the previous coupon date before the settlement date
- [COUPNCD](#coupncd) - Return the next coupon date after the settlement date
- [COUPNUM](#coupnum) - Return the number of coupons payable between settlement and maturity dates
- [CUMIPMT](#cumipmt) - Return the cumulative interest paid on a loan between two periods
- [CUMPRINC](#cumprinc) - Return the cumulative principal paid on a loan between two periods
- [DB](#db) - Calculate depreciation using the fixed-declining balance method
- [DDB](#ddb) - Calculate depreciation using the double-declining balance method
- [DISC](#disc) - Calculate the discount rate for a security
- [DOLLARDE](#dollarde) - Convert a dollar price expressed as a fraction into a decimal dollar price
- [DOLLARFR](#dollarfr) - Convert a decimal dollar price into a fractional dollar price
- [DURATION](#duration) - Return the Macaulay duration for an assumed par value of 100
- [EFFECT](#effect) - Return the effective annual interest rate
- [FV](#fv) - Calculate the future value of an investment
- [FVSCHEDULE](#fvschedule) - Calculate the future value of an initial principal after applying a series of compound interest rates
- [INTRATE](#intrate) - Calculate the interest rate for a fully invested security
- [IPMT](#ipmt) - Return the interest payment for a given period
- [IRR](#irr) - Return the internal rate of return for a series of cash flows
- [ISPMT](#ispmt) - Calculate the interest paid during a specific period of an investment
- [MDURATION](#mduration) - Return the modified duration for an assumed par value of 100
- [MIRR](#mirr) - Return the modified internal rate of return for a series of cash flows
- [NOMINAL](#nominal) - Return the nominal annual interest rate
- [NPER](#nper) - Return the number of periods for an investment
- [NPV](#npv) - Calculate the net present value of an investment
- [ODDFPRICE](#oddfprice) - Calculate the price per $100 face value of a security with an odd first period
- [ODDFYIELD](#oddfyield) - Calculate the yield of a security with an odd first period
- [ODDLPRICE](#oddlprice) - Calculate the price per $100 face value of a security with an odd last period
- [ODDLYIELD](#oddlyield) - Calculate the yield of a security with an odd last period
- [PDURATION](#pduration) - Return the number of periods required for an investment to reach a specified value
- [PMT](#pmt) - Calculate the payment for a loan based on constant payments and a constant interest rate
- [PPMT](#ppmt) - Return the principal payment for a given period
- [PRICE](#price) - Return the price per $100 face value of a security that pays periodic interest
- [PRICEDISC](#pricedisc) - Return the price per $100 face value of a discounted security
- [PRICEMAT](#pricemat) - Return the price per $100 face value of a security that pays interest at maturity
- [PV](#pv) - Calculate the present value of an investment
- [RATE](#rate) - Return the interest rate per period of an annuity
- [RECEIVED](#received) - Calculate the amount received at maturity for a fully invested security
- [RRI](#rri) - Return the equivalent interest rate for the growth of an investment
- [SLN](#sln) - Calculate straight-line depreciation of an asset for one period
- [SYD](#syd) - Calculate the sum-of-years' digits depreciation of an asset for a specified period
- [TBILLEQ](#tbilleq) - Calculate the bond-equivalent yield for a Treasury bill
- [TBILLPRICE](#tbillprice) - Calculate the price per $100 face value for a Treasury bill
- [TBILLYIELD](#tbillyield) - Calculate the yield for a Treasury bill
- [VDB](#vdb) - Calculate the depreciation of an asset using the variable declining balance method
- [XIRR](#xirr) - Return the internal rate of return for a schedule of cash flows
- [XNPV](#xnpv) - Return the net present value for a schedule of cash flows
- [YIELD](#yield) - Return the yield of a security that pays periodic interest
- [YIELDDISC](#yielddisc) - Return the annual yield for a discounted security
- [YIELDMAT](#yieldmat) - Return the annual yield of a security that pays interest at maturity

### Information Functions
- [CELL](#cell) - Return information about the format, location, or contents of a cell
- [INFO](#info) - Return information about the current operating environment
- [ISBLANK](#isblank) - Return TRUE if the value is blank
- [ISERR](#iserr) - Return TRUE if the value is any error value except #N/A
- [ISERROR](#iserror) - Return TRUE if the value is any error value
- [ISEVEN](#iseven) - Return TRUE if the number is even
- [ISLOGICAL](#islogical) - Return TRUE if the value is a logical value
- [ISNA](#isna) - Return TRUE if the value is the #N/A error value
- [ISNONTEXT](#isnontext) - Return TRUE if the value is not text
- [ISNUMBER](#isnumber) - Return TRUE if the value is a number
- [ISODD](#isodd) - Return TRUE if the number is odd
- [ISOMITTED](#isomitted) - Check if a value is missing in a LAMBDA expression
- [ISTEXT](#istext) - Return TRUE if the value is text
- [ERROR.TYPE](#error_type) - Return a number corresponding to an error type

### Logic Functions
- [AND](#and) - Return TRUE if all arguments are TRUE
- [OR](#or) - Return TRUE if any argument is TRUE
- [NOT](#not) - Reverse the logical value of its argument
- [XOR](#xor) - Return a logical exclusive OR of all arguments
- [TRUE](#true) - Return the logical value TRUE
- [FALSE](#false) - Return the logical value FALSE
- [IF](#if) - Perform a logical test and return one value for TRUE and another for FALSE
- [IFS](#ifs) - Check multiple conditions and return the value corresponding to the first TRUE condition
- [IFERROR](#iferror) - Return a value if an expression results in an error
- [IFNA](#ifna) - Return a value if the expression results in #N/A or None
- [SWITCH](#switch) - Evaluate an expression and return a value from a list based on matching values
- [LAMBDA](#lambda) - Create a reusable lambda function with named parameters
- [LET](#let) - Assign names to calculation results and evaluate a final expression
- [BYCOL](#bycol) - Apply a LAMBDA to each column and return an array of results
- [BYROW](#byrow) - Apply a LAMBDA to each row and return an array of results
- [MAP](#map) - Return an array formed by mapping each value to a new value by applying a LAMBDA
- [MAKEARRAY](#makearray) - Return a calculated array of a specified row and column size by applying a LAMBDA

### Math & Trigonometry Functions
- [ABS](#abs) - Returns the absolute value of a number
- [ACOS](#acos) - Returns the arccosine of a number in radians
- [ACOSH](#acosh) - Returns the inverse hyperbolic cosine of a number
- [ACOT](#acot) - Returns the arccotangent of a number in radians
- [ACOTH](#acoth) - Returns the inverse hyperbolic cotangent of a number
- [AGGREGATE](#aggregate) - Returns an aggregate calculation from a list
- [ARABIC](#arabic) - Converts a Roman numeral to an Arabic number
- [ASIN](#asin) - Returns the arcsine of a number in radians
- [ASINH](#asinh) - Returns the inverse hyperbolic sine of a number
- [ATAN](#atan) - Returns the arctangent of a number in radians
- [ATAN2](#atan2) - Returns the arctangent from x and y coordinates
- [ATANH](#atanh) - Returns the inverse hyperbolic tangent of a number
- [AVERAGE](#average) - Returns the average (arithmetic mean) of numbers
- [AVERAGEIF](#averageif) - Returns the average of cells that meet a criterion
- [BASE](#base) - Converts a number to text representation with a given base
- [CEILING](#ceiling) - Rounds a number up to the nearest multiple of significance
- [CEILING_MATH](#ceiling_math) - Rounds a number up to nearest multiple with mode control
- [CEILING_PRECISE](#ceiling_precise) - Rounds a number up to nearest multiple (always away from zero)
- [COMBIN](#combin) - Returns the number of combinations for given items
- [COMBINA](#combina) - Returns the number of combinations with repetitions
- [COS](#cos) - Returns the cosine of an angle in radians
- [COSH](#cosh) - Returns the hyperbolic cosine of a number
- [COT](#cot) - Returns the cotangent of an angle in radians
- [COTH](#coth) - Returns the hyperbolic cotangent of a number
- [CSC](#csc) - Returns the cosecant of an angle in radians
- [CSCH](#csch) - Returns the hyperbolic cosecant of a number
- [DECIMAL](#decimal) - Converts text representation of number in given base to decimal
- [DEGREES](#degrees) - Converts radians to degrees
- [EVEN](#even) - Rounds a number up to the nearest even integer
- [EXP](#exp) - Returns e raised to the power of a number
- [FACT](#fact) - Returns the factorial of a number
- [FACTDOUBLE](#factdouble) - Returns the double factorial of a number
- [FLOOR](#floor) - Rounds a number down to the nearest multiple of significance
- [FLOOR_MATH](#floor_math) - Rounds a number down to nearest multiple with mode control
- [FLOOR_PRECISE](#floor_precise) - Rounds a number down to nearest multiple (always toward zero)
- [GCD](#gcd) - Returns the greatest common divisor of integers
- [INT](#int) - Rounds a number down to the nearest integer
- [ISO_CEILING](#iso_ceiling) - Rounds a number up to nearest multiple (ISO standard)
- [LCM](#lcm) - Returns the least common multiple of integers
- [LN](#ln) - Returns the natural logarithm of a number
- [LOG](#log) - Returns the logarithm of a number to a specified base
- [LOG10](#log10) - Returns the base-10 logarithm of a number
- [MAX](#max) - Returns the largest value in a set of numbers
- [MAXIFS](#maxifs) - Returns the maximum value among cells specified by a criterion
- [MDETERM](#mdeterm) - Returns the matrix determinant of an array
- [MIN](#min) - Returns the smallest value in a set of numbers
- [MINIFS](#minifs) - Returns the minimum value among cells specified by a criterion
- [MINVERSE](#minverse) - Returns the inverse of a square matrix
- [MMULT](#mmult) - Returns the matrix product of two arrays
- [MOD](#mod) - Returns the remainder from division
- [MROUND](#mround) - Rounds a number to the nearest multiple of a specified value
- [MULTINOMIAL](#multinomial) - Returns the multinomial coefficient of a set of numbers
- [MUNIT](#munit) - Returns the unit matrix (identity matrix) for a specified dimension
- [ODD](#odd) - Rounds a number up to the nearest odd integer
- [PRODUCT](#product) - Multiplies all numbers given as arguments
- [QUOTIENT](#quotient) - Returns the integer portion of a division
- [PI](#pi) - Returns the value of pi (π)
- [POWER](#power) - Returns the result of a number raised to a power
- [RADIANS](#radians) - Converts degrees to radians
- [RAND](#rand) - Returns a random number between 0 and 1
- [RANDBETWEEN](#randbetween) - Returns a random integer between specified numbers
- [RANDARRAY](#randarray) - Returns an array of random numbers
- [ROMAN](#roman) - Converts an Arabic number to Roman numeral as text
- [ROUND](#round) - Rounds a number to a specified number of digits
- [ROUNDDOWN](#rounddown) - Rounds a number down (toward zero)
- [ROUNDUP](#roundup) - Rounds a number up (away from zero)
- [SEC](#sec) - Returns the secant of an angle in radians
- [SECH](#sech) - Returns the hyperbolic secant of a number
- [SEQUENCE](#sequence) - Generates a sequence of numbers in an array
- [SERIESSUM](#seriessum) - Returns the sum of a power series
- [SIGN](#sign) - Returns the sign of a number
- [SIN](#sin) - Returns the sine of an angle in radians
- [SINH](#sinh) - Returns the hyperbolic sine of a number
- [SQRT](#sqrt) - Returns the positive square root of a number
- [SQRTPI](#sqrtpi) - Returns the square root of (number * pi)
- [SUBTOTAL](#subtotal) - Returns a subtotal in a list or database
- [SUMPRODUCT](#sumproduct) - Returns the sum of the products of corresponding array components
- [SUMSQ](#sumsq) - Returns the sum of the squares of the arguments
- [SUMX2MY2](#sumx2my2) - Returns the sum of the difference of squares of corresponding values
- [SUMX2PY2](#sumx2py2) - Returns the sum of the sum of squares of corresponding values
- [SUMXMY2](#sumxmy2) - Returns the sum of squares of differences of corresponding values
- [TAN](#tan) - Returns the tangent of an angle in radians
- [TANH](#tanh) - Returns the hyperbolic tangent of a number
- [TRUNC](#trunc) - Truncates a number to an integer by removing decimals

### Statistical Functions
- [AVEDEV](#avedev) - Returns the average of the absolute deviations
- [AVERAGE](#average) - Returns the average (arithmetic mean) of its arguments
- [AVERAGEA](#averagea) - Returns the average of its arguments, including numbers, text, and logical values
- [AVERAGEIF](#averageif) - Returns the average of cells that meet a criterion
- [AVERAGEIFS](#averageifs) - Returns the average of cells that meet multiple criteria
- [BETA_DIST](#beta_dist) - Returns the beta probability distribution function
- [BETA_INV](#beta_inv) - Returns the inverse of the beta cumulative distribution
- [BINOM_DIST](#binom_dist) - Returns the individual term binomial distribution probability
- [BINOM_DIST_RANGE](#binom_dist_range) - Returns the probability of a trial result using binomial distribution
- [BINOM_INV](#binom_inv) - Returns the smallest value for which the cumulative binomial distribution is >= criterion
- [CHISQ_DIST](#chisq_dist) - Returns the chi-squared distribution
- [CHISQ_DIST_RT](#chisq_dist_rt) - Returns the right-tailed probability of the chi-squared distribution
- [CHISQ_INV](#chisq_inv) - Returns the inverse of the left-tailed probability of the chi-squared distribution
- [CHISQ_INV_RT](#chisq_inv_rt) - Returns the inverse of the right-tailed probability of the chi-squared distribution
- [CHISQ_TEST](#chisq_test) - Returns the test for independence (chi-squared test)
- [CONFIDENCE](#confidence) - Returns the confidence interval (backward compatibility alias)
- [CONFIDENCE_NORM](#confidence_norm) - Returns the confidence interval for a population mean (normal distribution)
- [CONFIDENCE_T](#confidence_t) - Returns the confidence interval for a population mean (t-distribution)
- [CORREL](#correl) - Returns the correlation coefficient between two data sets
- [COUNT](#count) - Counts the number of cells that contain numbers
- [COUNTA](#counta) - Counts the number of cells that are not empty
- [COUNTBLANK](#countblank) - Counts empty cells in a range
- [COUNTIF](#countif) - Counts the number of cells that meet a criterion
- [COUNTIFS](#countifs) - Counts cells that meet multiple criteria
- [COVAR](#covar) - Returns covariance (legacy Excel function)
- [COVARIANCE_P](#covariance_p) - Returns population covariance
- [COVARIANCE_S](#covariance_s) - Returns sample covariance
- [DEVSQ](#devsq) - Returns the sum of squares of deviations
- [EXPON_DIST](#expon_dist) - Returns the exponential distribution
- [F_DIST](#f_dist) - Returns the F probability distribution
- [F_DIST_RT](#f_dist_rt) - Returns the right-tailed F probability distribution
- [F_INV](#f_inv) - Returns the inverse of the F probability distribution
- [F_INV_RT](#f_inv_rt) - Returns the inverse of the right-tailed F probability distribution
- [F_TEST](#f_test) - Returns the result of an F-test
- [FISHER](#fisher) - Returns the Fisher transformation
- [FISHERINV](#fisherinv) - Returns the inverse of the Fisher transformation
- [FORECAST](#forecast) - Returns a value along a linear trend (backward compatibility)
- [FORECAST_LINEAR](#forecast_linear) - Returns a value along a linear trend using linear regression
- [FORECAST_ETS](#forecast_ets) - Returns a forecasted value based on exponential smoothing
- [FORECAST_ETS_CONFINT](#forecast_ets_confint) - Returns a confidence interval for the forecast
- [FORECAST_ETS_SEASONALITY](#forecast_ets_seasonality) - Returns the detected seasonality length
- [FORECAST_ETS_STAT](#forecast_ets_stat) - Returns statistical values for ETS forecast
- [FREQUENCY](#frequency) - Returns a frequency distribution as a vertical array
- [GAMMA](#gamma) - Returns the gamma function value
- [GAMMALN](#gammaln) - Returns the natural logarithm of the gamma function
- [GAMMALN_PRECISE](#gammaln_precise) - Returns the natural logarithm of the gamma function (precise version)
- [GAMMA_DIST](#gamma_dist) - Returns the gamma distribution
- [GAMMA_INV](#gamma_inv) - Returns the inverse of the gamma cumulative distribution
- [GAUSS](#gauss) - Returns 0.5 less than the standard normal cumulative distribution
- [GEOMEAN](#geomean) - Returns the geometric mean of an array of positive numbers
- [GROWTH](#growth) - Returns values along an exponential trend
- [HARMEAN](#harmean) - Returns the harmonic mean of a data set
- [HYPGEOM_DIST](#hypgeom_dist) - Returns the hypergeometric distribution
- [INTERCEPT](#intercept) - Returns the intercept of the linear regression line
- [KURT](#kurt) - Returns the kurtosis of a data set
- [LARGE](#large) - Returns the k-th largest value in a data set
- [LINEST](#linest) - Returns statistics for a linear trend
- [LOGEST](#logest) - Returns parameters of an exponential trend
- [LOGNORM_DIST](#lognorm_dist) - Returns the lognormal distribution
- [LOGNORM_INV](#lognorm_inv) - Returns the inverse of the lognormal cumulative distribution
- [MAX](#max) - Returns the largest value in a set of values
- [MAXA](#maxa) - Returns the largest value in a set of values (includes text and logical values)
- [MAXIFS](#maxifs) - Returns the maximum value among cells specified by a given set of conditions
- [MEDIAN](#median) - Returns the median of the given numbers
- [MIN](#min) - Returns the smallest value in a set of values
- [MINA](#mina) - Returns the smallest value in a set of values (includes text and logical values)
- [MINIFS](#minifs) - Returns the minimum value among cells specified by a given set of conditions
- [MODE](#mode) - Returns the most common value in a data set (backward compatibility)
- [MODE_MULT](#mode_mult) - Returns a vertical array of the most frequently occurring values
- [MODE_SNGL](#mode_sngl) - Returns the most common value in a data set
- [NEGBINOM_DIST](#negbinom_dist) - Returns the negative binomial distribution
- [NORM_DIST](#norm_dist) - Returns the normal cumulative distribution
- [NORM_INV](#norm_inv) - Returns the inverse of the normal cumulative distribution
- [NORM_S_DIST](#norm_s_dist) - Returns the standard normal cumulative distribution
- [NORM_S_INV](#norm_s_inv) - Returns the inverse of the standard normal cumulative distribution
- [PERCENTILE](#percentile) - Returns the k-th percentile of values in a range (backward compatibility)
- [PERCENTILE_EXC](#percentile_exc) - Returns the k-th percentile of values (k in range 0..1, exclusive)
- [PERCENTILE_INC](#percentile_inc) - Returns the k-th percentile of values in a range
- [PERCENTRANK](#percentrank) - Returns the percentage rank of a value (backward compatibility)
- [PERCENTRANK_EXC](#percentrank_exc) - Returns the rank of a value as a percentage (0 to 1, exclusive)
- [PERCENTRANK_INC](#percentrank_inc) - Returns the percentage rank of a value in a data set
- [PERMUT](#permut) - Returns the number of permutations for a given number of objects
- [PERMUTATIONA](#permutationa) - Returns the number of permutations with repetitions
- [PHI](#phi) - Returns the value of the density function for a standard normal distribution
- [POISSON_DIST](#poisson_dist) - Returns the Poisson distribution
- [SKEW](#skew) - Returns the skewness of a distribution
- [SKEW_P](#skew_p) - Returns the skewness of a distribution based on a population
- [SLOPE](#slope) - Returns the slope of the linear regression line
- [SMALL](#small) - Returns the k-th smallest value in a data set
- [STANDARDIZE](#standardize) - Returns a normalized value
- [STDEV](#stdev) - Calculates standard deviation based on a sample (backward compatibility)
- [STDEV_P](#stdev_p) - Calculates standard deviation based on the entire population
- [STDEV_S](#stdev_s) - Calculates standard deviation based on a sample
- [STDEVA](#stdeva) - Calculates standard deviation based on a sample (includes text and logical values)
- [STDEVPA](#stdevpa) - Calculates standard deviation based on the entire population (includes text and logical values)
- [STEYX](#steyx) - Returns the standard error of the predicted y-value for each x in the regression
- [T_DIST](#t_dist) - Returns the percentage points (probability) for the Student t-distribution
- [T_DIST_2T](#t_dist_2t) - Returns the percentage points (probability) for the Student t-distribution (two-tailed)
- [T_DIST_RT](#t_dist_rt) - Returns the Student t-distribution (right-tailed)
- [T_INV](#t_inv) - Returns the t-value of the Student t-distribution as a function of the probability and degrees of freedom
- [T_INV_2T](#t_inv_2t) - Returns the inverse of the Student t-distribution (two-tailed)
- [T_TEST](#t_test) - Returns the probability associated with a Student's t-test
- [TRIMMEAN](#trimmean) - Returns the mean of the interior of a data set
- [VAR](#var) - Calculates variance based on a sample (backward compatibility)
- [VAR_P](#var_p) - Calculates variance based on the entire population
- [VAR_S](#var_s) - Calculates variance based on a sample
- [VARA](#vara) - Calculates variance based on a sample (includes text and logical values)
- [VARPA](#varpa) - Calculates variance based on the entire population (includes text and logical values)
- [WEIBULL_DIST](#weibull_dist) - Returns the Weibull distribution
- [Z_TEST](#z_test) - Returns the one-tailed probability-value of a z-test

### Text & Data Functions
- [ASC](#asc) - Converts full-width characters to half-width characters
- [BAHTTEXT](#bahttext) - Converts a number to Thai Baht currency format
- [CHAR](#char) - Returns the character specified by the code number
- [CLEAN](#clean) - Removes all nonprintable characters from text
- [CODE](#code) - Returns a numeric code for the first character in a text string
- [CONCAT](#concat) - Combines text from multiple ranges and/or strings
- [CONCATENATE](#concatenate) - Joins several text strings into one text string
- [DOLLAR](#dollar) - Converts a number to text using currency format ($)
- [EXACT](#exact) - Checks whether two text strings are exactly the same
- [FIND](#find) - Finds one text string within another (case-sensitive)
- [FINDB](#findb) - Finds text within another based on bytes (case-sensitive)
- [FIXED](#fixed) - Formats a number as text with a fixed number of decimals
- [LEFT](#left) - Returns the leftmost characters from a text string
- [LEFTB](#leftb) - Returns the leftmost characters based on number of bytes
- [LEN](#len) - Returns the number of characters in a text string
- [LENB](#lenb) - Returns the number of bytes in text
- [LOWER](#lower) - Converts text to lowercase
- [MID](#mid) - Returns characters from the middle of a text string
- [MIDB](#midb) - Returns characters from the middle based on bytes
- [NUMBERVALUE](#numbervalue) - Converts text to number in a locale-independent manner
- [PROPER](#proper) - Capitalizes the first letter in each word of a text string
- [REGEXEXTRACT](#regexextract) - Extracts strings within text that match a regex pattern
- [REGEXREPLACE](#regexreplace) - Replaces strings that match a regex pattern
- [REGEXTEST](#regextest) - Tests whether text matches a regex pattern
- [REPLACE](#replace) - Replaces part of a text string with a different text string
- [REPLACEB](#replaceb) - Replaces part of text based on bytes
- [REPT](#rept) - Repeats text a given number of times
- [RIGHT](#right) - Returns the rightmost characters from a text string
- [RIGHTB](#rightb) - Returns the rightmost characters based on number of bytes
- [SEARCH](#search) - Finds one text string within another (case-insensitive)
- [SEARCHB](#searchb) - Finds text within another based on bytes (case-insensitive)
- [SUBSTITUTE](#substitute) - Substitutes new text for old text in a text string
- [T](#t) - Converts its argument to text
- [TEXT](#text) - Formats a number and converts it to text
- [TEXTAFTER](#textafter) - Returns text that occurs after a given character or substring
- [TEXTBEFORE](#textbefore) - Returns text that occurs before a given character or substring
- [TEXTJOIN](#textjoin) - Combines text from multiple ranges with a delimiter
- [TEXTSPLIT](#textsplit) - Splits text into rows and columns using delimiters
- [TRIM](#trim) - Removes all spaces from text except single spaces between words
- [UNICHAR](#unichar) - Returns the Unicode character referenced by a numeric value
- [UNICODE](#unicode) - Returns the number (code point) of the first character
- [UPPER](#upper) - Converts text to uppercase
- [VALUE](#value) - Converts text that represents a number to a number
- [VALUETOTEXT](#valuetotext) - Returns text from any specified value

---

## Function Index

**A**
- [ABS](#abs) - Returns the absolute value of a number
- [ACCRINT](#accrint) - Return the accrued interest for a security that pays periodic interest
- [ACCRINTM](#accrintm) - Return the accrued interest for a security that pays interest at maturity
- [ACOS](#acos) - Returns the arccosine of a number in radians
- [ACOSH](#acosh) - Returns the inverse hyperbolic cosine of a number
- [ACOT](#acot) - Returns the arccotangent of a number in radians
- [ACOTH](#acoth) - Returns the inverse hyperbolic cotangent of a number
- [AGGREGATE](#aggregate) - Returns an aggregate calculation from a list
- [AND](#and) - Return TRUE if all arguments are TRUE
- [ARABIC](#arabic) - Converts a Roman numeral to an Arabic number
- [ASC](#asc) - Converts full-width characters to half-width characters
- [ASIN](#asin) - Returns the arcsine of a number in radians
- [ASINH](#asinh) - Returns the inverse hyperbolic sine of a number
- [ATAN](#atan) - Returns the arctangent of a number in radians
- [ATAN2](#atan2) - Returns the arctangent from x and y coordinates
- [ATANH](#atanh) - Returns the inverse hyperbolic tangent of a number
- [AVERAGE](#average) - Returns the average (arithmetic mean) of numbers
- [AVERAGEA](#averagea) - Returns the average of its arguments (including text and logical values)
- [AVERAGEIF](#averageif) - Returns the average of cells that meet a criterion
- [AVERAGEIFS](#averageifs) - Returns the average of cells that meet multiple criteria
- [AVEDEV](#avedev) - Returns the average of the absolute deviations

**B**
- [BAHTTEXT](#bahttext) - Converts a number to Thai Baht currency format
- [BASE](#base) - Converts a number to text representation with a given base
- [BESSELI](#besseli) - Returns the modified Bessel function In(x)
- [BESSELJ](#besselj) - Returns the Bessel function Jn(x)
- [BESSELK](#besselk) - Returns the modified Bessel function Kn(x)
- [BESSELY](#bessely) - Returns the Bessel function Yn(x)
- [BETA_DIST](#beta_dist) - Returns the beta probability distribution function
- [BETA_INV](#beta_inv) - Returns the inverse of the beta cumulative distribution
- [BIN2DEC](#bin2dec) - Converts a binary string to decimal
- [BIN2HEX](#bin2hex) - Converts a binary string to hexadecimal
- [BIN2OCT](#bin2oct) - Converts a binary string to octal
- [BINOM_DIST](#binom_dist) - Returns the individual term binomial distribution probability
- [BINOM_DIST_RANGE](#binom_dist_range) - Returns the probability of a trial result
- [BINOM_INV](#binom_inv) - Returns the smallest value for which cumulative binomial >= criterion
- [BITAND](#bitand) - Performs a bitwise AND on two numbers
- [BITLSHIFT](#bitlshift) - Performs a left shift on a number
- [BITOR](#bitor) - Performs a bitwise OR on two numbers
- [BITRSHIFT](#bitrshift) - Performs a right shift on a number
- [BITXOR](#bitxor) - Performs a bitwise XOR on two numbers
- [BYCOL](#bycol) - Apply a LAMBDA to each column and return an array of results
- [BYROW](#byrow) - Apply a LAMBDA to each row and return an array of results

**C**
- [CEILING](#ceiling) - Rounds a number up to the nearest multiple of significance
- [CEILING_MATH](#ceiling_math) - Rounds a number up to nearest multiple with mode control
- [CEILING_PRECISE](#ceiling_precise) - Rounds a number up to nearest multiple (always away from zero)
- [CELL](#cell) - Return information about the format, location, or contents of a cell
- [CHAR](#char) - Returns the character specified by the code number
- [CHISQ_DIST](#chisq_dist) - Returns the chi-squared distribution
- [CHISQ_DIST_RT](#chisq_dist_rt) - Returns the right-tailed probability of chi-squared distribution
- [CHISQ_INV](#chisq_inv) - Returns the inverse of the left-tailed chi-squared distribution
- [CHISQ_INV_RT](#chisq_inv_rt) - Returns the inverse of the right-tailed chi-squared distribution
- [CHISQ_TEST](#chisq_test) - Returns the test for independence (chi-squared test)
- [CLEAN](#clean) - Removes all nonprintable characters from text
- [CODE](#code) - Returns a numeric code for the first character in a text string
- [COMBIN](#combin) - Returns the number of combinations for given items
- [COMBINA](#combina) - Returns the number of combinations with repetitions
- [COMPLEX](#complex) - Creates a complex number from real and imaginary coefficients
- [CONCAT](#concat) - Combines text from multiple ranges and/or strings
- [CONCATENATE](#concatenate) - Joins several text strings into one text string
- [CONFIDENCE](#confidence) - Returns the confidence interval (backward compatibility)
- [CONFIDENCE_NORM](#confidence_norm) - Returns the confidence interval (normal distribution)
- [CONFIDENCE_T](#confidence_t) - Returns the confidence interval (t-distribution)
- [CONVERT](#convert) - Converts a number from one measurement unit to another
- [CORREL](#correl) - Returns the correlation coefficient between two data sets
- [COS](#cos) - Returns the cosine of an angle in radians
- [COSH](#cosh) - Returns the hyperbolic cosine of a number
- [COT](#cot) - Returns the cotangent of an angle in radians
- [COTH](#coth) - Returns the hyperbolic cotangent of a number
- [COUNT](#count) - Counts the number of cells that contain numbers
- [COUNTA](#counta) - Counts the number of cells that are not empty
- [COUNTBLANK](#countblank) - Counts empty cells in a range
- [COUNTIF](#countif) - Counts the number of cells that meet a criterion
- [COUNTIFS](#countifs) - Counts cells that meet multiple criteria
- [COUPDAYBS](#coupdaybs) - Return the number of days from the beginning of the coupon period to the settlement date
- [COUPDAYS](#coupdays) - Return the number of days in the coupon period containing the settlement date
- [COUPDAYSNC](#coupdaysnc) - Return the number of days from the settlement date to the next coupon date
- [COUPNCD](#coupncd) - Return the next coupon date after the settlement date
- [COUPNUM](#coupnum) - Return the number of coupons payable between settlement and maturity dates
- [COUPPCD](#couppcd) - Return the previous coupon date before the settlement date
- [COVAR](#covar) - Returns covariance (legacy Excel function)
- [COVARIANCE_P](#covariance_p) - Returns population covariance
- [COVARIANCE_S](#covariance_s) - Returns sample covariance
- [CSC](#csc) - Returns the cosecant of an angle in radians
- [CSCH](#csch) - Returns the hyperbolic cosecant of a number
- [CUMPRINC](#cumprinc) - Return the cumulative principal paid on a loan between two periods

**D**
- [DATE](#date) - Returns the serial number of a specific date
- [DATEDIF](#datedif) - Calculates the difference between dates in days, months, or years
- [DATEVALUE](#datevalue) - Converts a date in text format to a serial number
- [DAVERAGE](#daverage) - Calculates the average of database field values matching criteria
- [DAY](#day) - Converts a serial number to a day of the month
- [DAYS](#days) - Returns the number of days between two dates
- [DAYS360](#days360) - Calculates the number of days between two dates based on a 360-day year
- [DCOUNT](#dcount) - Counts cells containing numbers in a database field that match criteria
- [DCOUNTA](#dcounta) - Counts non-empty cells in a database field that match criteria
- [DDB](#ddb) - Calculate depreciation using the double-declining balance method
- [DEC2BIN](#dec2bin) - Converts a decimal number to binary
- [DEC2HEX](#dec2hex) - Converts a decimal number to hexadecimal
- [DEC2OCT](#dec2oct) - Converts a decimal number to octal
- [DECIMAL](#decimal) - Converts text representation of number in given base to decimal
- [DEGREES](#degrees) - Converts radians to degrees
- [DELTA](#delta) - Tests whether two values are equal
- [DEVSQ](#devsq) - Returns the sum of squared deviations
- [DGET](#dget) - Extracts a single value from a database field that matches criteria
- [DMAX](#dmax) - Returns the maximum value from database field values matching criteria
- [DMIN](#dmin) - Returns the minimum value from database field values matching criteria
- [DOLLAR](#dollar) - Converts a number to text using currency format ($)
- [DPRODUCT](#dproduct) - Multiplies values from database field that match criteria
- [DSTDEV](#dstdev) - Calculates the sample standard deviation of database field values matching criteria
- [DSTDEVP](#dstdevp) - Calculates the population standard deviation of database field values matching criteria
- [DSUM](#dsum) - Sums values from database field that match criteria
- [DURATION](#duration) - Return the Macaulay duration for an assumed par value of 100
- [DVAR](#dvar) - Calculates the sample variance of database field values matching criteria
- [DVARP](#dvarp) - Calculates the population variance of database field values matching criteria

**E**
- [EDATE](#edate) - Returns the serial number of a date months before or after
- [EOMONTH](#eomonth) - Returns the serial number of the last day of the month
- [ERF](#erf) - Returns the error function erf(x)
- [ERF_PRECISE](#erf_precise) - Precise version of error function
- [ERFC](#erfc) - Returns the complementary error function erfc(x)
- [ERFC_PRECISE](#erfc_precise) - Precise version of complementary error function
- [ERROR.TYPE](#error_type) - Return a number corresponding to an error type
- [EVEN](#even) - Rounds a number up to the nearest even integer
- [EXACT](#exact) - Checks whether two text strings are exactly the same
- [excel_serial_to_day](#excel_serial_to_day) - Converts a serial number or datetime to day of the month
- [excel_serial_to_hour](#excel_serial_to_hour) - Extracts the hour component from an Excel-style serial number or datetime
- [excel_serial_to_minute](#excel_serial_to_minute) - Extracts the minute component from an Excel-style serial number or datetime
- [excel_serial_to_month](#excel_serial_to_month) - Extracts the month from an Excel-style serial number or datetime
- [excel_serial_to_weekday](#excel_serial_to_weekday) - Converts a serial number or datetime to day of the week
- [excel_serial_to_year](#excel_serial_to_year) - Extracts the year from an Excel-style serial number or datetime
- [EXP](#exp) - Returns e raised to the power of a number
- [EXPON_DIST](#expon_dist) - Returns the exponential distribution

**F**
- [F_DIST](#f_dist) - Returns the F probability distribution
- [F_DIST_RT](#f_dist_rt) - Returns the right-tailed F probability distribution
- [F_INV](#f_inv) - Returns the inverse of the F probability distribution
- [F_INV_RT](#f_inv_rt) - Returns the inverse of the right-tailed F probability distribution
- [F_TEST](#f_test) - Returns the result of an F-test
- [FACT](#fact) - Returns the factorial of a number
- [FACTDOUBLE](#factdouble) - Returns the double factorial of a number
- [FALSE](#false) - Return the logical value FALSE
- [FIND](#find) - Finds one text string within another (case-sensitive)
- [FINDB](#findb) - Finds text within another based on bytes (case-sensitive)
- [FISHER](#fisher) - Returns the Fisher transformation
- [FISHERINV](#fisherinv) - Returns the inverse of the Fisher transformation
- [FIXED](#fixed) - Formats a number as text with a fixed number of decimals
- [FLOOR](#floor) - Rounds a number down to the nearest multiple of significance
- [FLOOR_MATH](#floor_math) - Rounds a number down to nearest multiple with mode control
- [FLOOR_PRECISE](#floor_precise) - Rounds a number down to nearest multiple (always toward zero)
- [FORECAST](#forecast) - Returns a linear forecast value (legacy function)
- [FORECAST_ETS](#forecast_ets) - Returns exponential smoothing forecast
- [FORECAST_ETS_CONFINT](#forecast_ets_confint) - Returns confidence interval for ETS forecast
- [FORECAST_ETS_SEASONALITY](#forecast_ets_seasonality) - Detects seasonality length
- [FORECAST_ETS_STAT](#forecast_ets_stat) - Returns statistical metrics for ETS
- [FORECAST_LINEAR](#forecast_linear) - Returns a linear forecast value
- [FREQUENCY](#frequency) - Returns frequency distribution

**G**
- [GAMMA](#gamma) - Returns the gamma function value
- [GAMMA_DIST](#gamma_dist) - Returns the gamma distribution
- [GAMMA_INV](#gamma_inv) - Returns the inverse of the gamma cumulative distribution
- [GAMMALN](#gammaln) - Returns the natural logarithm of gamma function
- [GAMMALN_PRECISE](#gammaln_precise) - Returns the natural logarithm of gamma (precise)
- [GAUSS](#gauss) - Returns standard normal distribution minus 0.5
- [GCD](#gcd) - Returns the greatest common divisor of integers
- [GEOMEAN](#geomean) - Returns the geometric mean
- [GESTEP](#gestep) - Tests whether a number is greater than or equal to a threshold
- [GROWTH](#growth) - Calculates exponential trend values

**H**
- [HARMEAN](#harmean) - Returns the harmonic mean
- [HEX2BIN](#hex2bin) - Converts a hexadecimal string to binary
- [HEX2DEC](#hex2dec) - Converts a hexadecimal string to decimal
- [HEX2OCT](#hex2oct) - Converts a hexadecimal string to octal
- [HOUR](#hour) - Converts a serial number to an hour
- [HYPGEOM_DIST](#hypgeom_dist) - Returns the hypergeometric distribution

**I**
- [IF](#if) - Perform a logical test and return one value for TRUE and another for FALSE
- [IFERROR](#iferror) - Return a value if an expression results in an error
- [IFNA](#ifna) - Return a value if the expression results in #N/A or None
- [IFS](#ifs) - Check multiple conditions and return the value corresponding to the first TRUE condition
- [IMABS](#imabs) - Returns the absolute value (modulus) of a complex number
- [IMAGINARY](#imaginary) - Returns the imaginary part of a complex number
- [IMARGUMENT](#imargument) - Returns the argument (angle in radians) of a complex number
- [IMCONJUGATE](#imconjugate) - Returns the complex conjugate
- [IMCOS](#imcos) - Cosine of complex number
- [IMCOSH](#imcosh) - Hyperbolic cosine of complex number
- [IMCOT](#imcot) - Cotangent of complex number
- [IMCSC](#imcsc) - Cosecant of complex number
- [IMCSCH](#imcsch) - Hyperbolic cosecant of complex number
- [IMDIV](#imdiv) - Returns the quotient of two complex numbers
- [IMEXP](#imexp) - Exponential of complex number
- [IMLN](#imln) - Natural logarithm of complex number
- [IMLOG10](#imlog10) - Base-10 logarithm of complex number
- [IMLOG2](#imlog2) - Base-2 logarithm of complex number
- [IMPOWER](#impower) - Returns a complex number raised to a power
- [IMPRODUCT](#improduct) - Returns the product of complex numbers
- [IMREAL](#imreal) - Returns the real part of a complex number
- [IMSEC](#imsec) - Secant of complex number
- [IMSECH](#imsech) - Hyperbolic secant of complex number
- [IMSIN](#imsin) - Sine of complex number
- [IMSINH](#imsinh) - Hyperbolic sine of complex number
- [IMSQRT](#imsqrt) - Returns the square root of a complex number
- [IMSUB](#imsub) - Returns the difference between two complex numbers
- [IMSUM](#imsum) - Returns the sum of complex numbers
- [IMTAN](#imtan) - Tangent of complex number
- [INFO](#info) - Return information about the current operating environment
- [INT](#int) - Rounds a number down to the nearest integer
- [INTERCEPT](#intercept) - Returns the Y-intercept of linear regression
- [ISBLANK](#isblank) - Return TRUE if the value is blank
- [ISERR](#iserr) - Return TRUE if the value is any error value except #N/A
- [ISERROR](#iserror) - Return TRUE if the value is any error value
- [ISEVEN](#iseven) - Return TRUE if the number is even
- [ISLOGICAL](#islogical) - Return TRUE if the value is a logical value
- [ISNA](#isna) - Return TRUE if the value is the #N/A error value
- [ISNONTEXT](#isnontext) - Return TRUE if the value is not text
- [ISNUMBER](#isnumber) - Return TRUE if the value is a number
- [ISODD](#isodd) - Return TRUE if the number is odd
- [ISOMITTED](#isomitted) - Check if a value is missing in a LAMBDA expression
- [ISO_CEILING](#iso_ceiling) - Rounds a number up to nearest multiple (ISO standard)
- [ISOWEEKNUM](#isoweeknum) - Returns the ISO week number
- [ISTEXT](#istext) - Return TRUE if the value is text

**K**
- [KURT](#kurt) - Returns the kurtosis of a dataset

**L**
- [LAMBDA](#lambda) - Create a reusable lambda function with named parameters
- [LARGE](#large) - Returns the kth largest value
- [LCM](#lcm) - Returns the least common multiple of integers
- [LEFT](#left) - Returns the leftmost characters from a text string
- [LEN](#len) - Returns the number of characters in a text string
- [LET](#let) - Assign names to calculation results and evaluate a final expression
- [LINEST](#linest) - Returns linear regression parameters (slope, intercept)
- [LN](#ln) - Returns the natural logarithm of a number
- [LOG](#log) - Returns the logarithm of a number to a specified base
- [LOG10](#log10) - Returns the base-10 logarithm of a number
- [LOGNORM_DIST](#lognorm_dist) - Returns the log-normal cumulative distribution
- [LOGNORM_INV](#lognorm_inv) - Returns the inverse of log-normal distribution
- [LOGEST](#logest) - Returns exponential regression parameters
- [LOWER](#lower) - Converts text to lowercase

**M**
- [MAKEARRAY](#makearray) - Return a calculated array of a specified row and column size by applying a LAMBDA
- [MAP](#map) - Return an array formed by mapping each value to a new value by applying a LAMBDA
- [MAX](#max) - Returns the largest value in a set of numbers
- [MAXA](#maxa) - Returns maximum value including text and logical values
- [MAXIFS](#maxifs) - Returns the maximum value among cells specified by a criterion
- [MDETERM](#mdeterm) - Returns the matrix determinant of an array
- [MDURATION](#mduration) - Return the modified duration for an assumed par value of 100
- [MEDIAN](#median) - Returns the median of the given numbers
- [MID](#mid) - Returns characters from the middle of a text string
- [MIN](#min) - Returns the smallest value in a set of numbers
- [MINA](#mina) - Returns the smallest value in a set of values (includes text and logical values)
- [MINIFS](#minifs) - Returns the minimum value among cells specified by a criterion
- [MINUTE](#minute) - Converts a serial number to a minute
- [MINVERSE](#minverse) - Returns the inverse of a square matrix
- [MOD](#mod) - Returns the remainder from division
- [MODE](#mode) - Returns the most common value in a data set (backward compatibility)
- [MODE_MULT](#mode_mult) - Returns a vertical array of the most frequently occurring values
- [MODE_SNGL](#mode_sngl) - Returns the most common value in a data set
- [MONTH](#month) - Converts a serial number to a month

**N**
- [NEGBINOM_DIST](#negbinom_dist) - Returns the negative binomial distribution
- [NETWORKDAYS](#networkdays) - Returns the number of working days between two dates
- [NETWORKDAYS_INTL](#networkdays_intl) - Returns working days between two dates with custom weekend parameters
- [NORM_DIST](#norm_dist) - Returns the normal cumulative distribution
- [NORM_INV](#norm_inv) - Returns the inverse of the normal cumulative distribution
- [NORM_S_DIST](#norm_s_dist) - Returns the standard normal cumulative distribution
- [NORM_S_INV](#norm_s_inv) - Returns the inverse of the standard normal cumulative distribution
- [NOT](#not) - Reverse the logical value of its argument
- [NOW](#now) - Returns the serial number of the current date and time

**O**
- [OCT2BIN](#oct2bin) - Converts an octal string to binary
- [OCT2DEC](#oct2dec) - Converts an octal string to decimal
- [OCT2HEX](#oct2hex) - Converts an octal string to hexadecimal
- [ODD](#odd) - Rounds a number up to the nearest odd integer
- [OR](#or) - Return TRUE if any argument is TRUE

**P**
- [PERCENTILE](#percentile) - Returns the k-th percentile of values in a range (backward compatibility)
- [PERCENTILE_EXC](#percentile_exc) - Returns the k-th percentile of values (k in range 0..1, exclusive)
- [PERCENTILE_INC](#percentile_inc) - Returns the k-th percentile of values in a range
- [PERCENTRANK](#percentrank) - Returns the percentage rank of a value (backward compatibility)
- [PERCENTRANK_EXC](#percentrank_exc) - Returns the rank of a value as a percentage (0 to 1, exclusive)
- [PERCENTRANK_INC](#percentrank_inc) - Returns the percentage rank of a value in a data set
- [PERMUT](#permut) - Returns the number of permutations for a given number of objects
- [PERMUTATIONA](#permutationa) - Returns the number of permutations with repetitions
- [PHI](#phi) - Returns the value of the density function for a standard normal distribution
- [PI](#pi) - Returns the value of pi (π)
- [POISSON_DIST](#poisson_dist) - Returns the Poisson distribution
- [POWER](#power) - Returns the result of a number raised to a power
- [PPMT](#ppmt) - Return the principal payment for a given period
- [PRICE](#price) - Return the price per $100 face value of a security that pays periodic interest
- [PRICEDISC](#pricedisc) - Return the price per $100 face value of a discounted security
- [PRICEMAT](#pricemat) - Return the price per $100 face value of a security that pays interest at maturity
- [PROPER](#proper) - Capitalizes the first letter in each word of a text string

**Q**

**R**
- [RADIANS](#radians) - Converts degrees to radians
- [REPLACE](#replace) - Replaces part of a text string with a different text string
- [REPT](#rept) - Repeats text a given number of times
- [RIGHT](#right) - Returns the rightmost characters from a text string
- [ROMAN](#roman) - Converts an Arabic number to Roman numeral as text
- [ROUND](#round) - Rounds a number to a specified number of digits
- [ROUNDDOWN](#rounddown) - Rounds a number down (toward zero)
- [ROUNDUP](#roundup) - Rounds a number up (away from zero)

**S**
- [SEARCH](#search) - Finds one text string within another (case-insensitive)
- [SEC](#sec) - Returns the secant of an angle in radians
- [SECH](#sech) - Returns the hyperbolic secant of a number
- [SECOND](#second) - Converts a serial number to a second
- [SIGN](#sign) - Returns the sign of a number
- [SIN](#sin) - Returns the sine of an angle in radians
- [SINH](#sinh) - Returns the hyperbolic sine of a number
- [SKEW](#skew) - Returns the skewness of a distribution
- [SKEW_P](#skew_p) - Returns the skewness of a distribution based on a population
- [SLN](#sln) - Calculate straight-line depreciation of an asset for one period
- [SLOPE](#slope) - Returns the slope of linear regression line
- [SMALL](#small) - Returns the k-th smallest value in a data set
- [SQRT](#sqrt) - Returns the positive square root of a number
- [SQRTPI](#sqrtpi) - Returns the square root of (number * pi)
- [STANDARDIZE](#standardize) - Returns a normalized value
- [STDEV](#stdev) - Calculates standard deviation based on a sample (backward compatibility)
- [STDEV_P](#stdev_p) - Calculates standard deviation based on the entire population
- [STDEV_S](#stdev_s) - Calculates standard deviation based on a sample
- [STDEVA](#stdeva) - Calculates standard deviation based on a sample (includes text and logical values)
- [STDEVPA](#stdevpa) - Calculates standard deviation based on the entire population (includes text and logical values)
- [STEYX](#steyx) - Returns the standard error of the predicted y-value for each x in the regression
- [SUBSTITUTE](#substitute) - Substitutes new text for old text in a text string
- [SUM](#sum) - Returns the sum of numbers
- [SUMIF](#sumif) - Sums numbers that meet a specified criterion
- [SWITCH](#switch) - Evaluate an expression and return a value from a list based on matching values

**T**
- [T_DIST](#t_dist) - Returns the percentage points (probability) for the Student t-distribution
- [T_DIST_2T](#t_dist_2t) - Returns the percentage points (probability) for the Student t-distribution (two-tailed)
- [T_DIST_RT](#t_dist_rt) - Returns the Student t-distribution (right-tailed)
- [T_INV](#t_inv) - Returns the t-value of the Student t-distribution as a function of the probability and degrees of freedom
- [T_INV_2T](#t_inv_2t) - Returns the inverse of the Student t-distribution (two-tailed)
- [T_TEST](#t_test) - Returns the probability associated with a Student's t-test
- [TAN](#tan) - Returns the tangent of an angle in radians
- [TANH](#tanh) - Returns the hyperbolic tangent of a number
- [TEXT](#text) - Formats a number and converts it to text
- [TEXTJOIN](#textjoin) - Combines text from multiple ranges with a delimiter
- [TIME](#time) - Returns the serial number of a specific time
- [TIMEVALUE](#timevalue) - Converts a time in text format to a serial number
- [TODAY](#today) - Returns the serial number of today's date
- [TRIM](#trim) - Removes all spaces from text except single spaces between words
- [TRIMMEAN](#trimmean) - Returns the mean of the interior of a data set
- [TRUE](#true) - Return the logical value TRUE
- [TRUNC](#trunc) - Truncates a number to an integer by removing decimals

**U**
- [UPPER](#upper) - Converts text to uppercase

**V**
- [VALUE](#value) - Converts text that represents a number to a number
- [VAR](#var) - Calculates variance based on a sample (backward compatibility)
- [VAR_P](#var_p) - Calculates variance based on the entire population
- [VAR_S](#var_s) - Calculates variance based on a sample
- [VARA](#vara) - Calculates variance based on a sample (includes text and logical values)
- [VARPA](#varpa) - Calculates variance based on the entire population (includes text and logical values)

**W**
- [WEEKDAY](#weekday) - Converts a serial number to a day of the week
- [WEEKNUM](#weeknum) - Converts a serial number to a week number
- [WEIBULL_DIST](#weibull_dist) - Returns the Weibull distribution
- [WORKDAY](#workday) - Returns the date after a number of working days
- [WORKDAY_INTL](#workday_intl) - Returns the date after working days with custom weekends

**X**
- [XIRR](#xirr) - Return the internal rate of return for a schedule of cash flows
- [XNPV](#xnpv) - Return the net present value for a schedule of cash flows
- [XOR](#xor) - Return a logical exclusive OR of all arguments

**Y**
- [YEAR](#year) - Converts a serial number to a year
- [YEARFRAC](#yearfrac) - Returns the fraction of year between two dates

**Z**
- [Z_TEST](#z_test) - Returns the one-tailed probability-value of a z-test
- [YIELD](#yield) - Return the yield of a security that pays periodic interest
- [YIELDDISC](#yielddisc) - Return the annual yield for a discounted security
- [YIELDMAT](#yieldmat) - Return the annual yield of a security that pays interest at maturity

**Z**

---

## Credits

This documentation was generated using the FormuLite framework. Function implementations are based on Excel's documented behavior and compatibility standards.

---

## Date Functions

### `DAYS()`

Returns the number of days between two dates.

**Parameters:**
- `end_date` (datetime): End date.
- `start_date` (datetime): Start date.

**Returns:**
- `int`: Number of days between the dates.

**Ejemplo:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import DAYS

start = datetime(2025, 1, 1)
end = datetime(2025, 1, 15)
print(DAYS(end, start))  # 14
```

**Cost:** O(1)

---

### `DAYS360()`

Calculates the number of days between two dates based on a 360-day year.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `method` (bool): False for US method, True for European method. Defaults to False.

**Returns:**
- `int`: Number of days based on 360-day year.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import DAYS360

start = datetime(2025, 1, 30)
end = datetime(2025, 2, 28)
print(DAYS360(start, end))  # 28 (US method)
print(DAYS360(start, end, method=True))  # 28 (European method)
```

**Cost:** O(1)

---

### `NETWORKDAYS()`

Returns the number of working days between two dates.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `holidays` (Optional[List[datetime]]): List of holiday dates. Defaults to None.

**Returns:**
- `int`: Number of working days.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import NETWORKDAYS

start = datetime(2025, 1, 1)
end = datetime(2025, 1, 15)
print(NETWORKDAYS(start, end))  # 11 (excluding weekends)

# With holidays
holidays = [datetime(2025, 1, 6)]
print(NETWORKDAYS(start, end, holidays))  # 10
```

**Cost:** O(1)

---

### `NETWORKDAYS_INTL()`

Returns working days between two dates with custom weekend parameters.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `weekend` (Union[int, str]): Weekend code (1-7) or bit string. Defaults to 1.
- `holidays` (Optional[List[datetime]]): List of holiday dates.

**Returns:**
- `int`: Number of working days.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import NETWORKDAYS_INTL

start = datetime(2025, 1, 1)
end = datetime(2025, 1, 15)

# Weekend Saturday-Sunday (code 1)
print(NETWORKDAYS_INTL(start, end, weekend=1))  # 11

# Weekend Sunday-Monday (code 2)
print(NETWORKDAYS_INTL(start, end, weekend=2))  # 11
```

**Cost:** O(1)

---

### `EDATE()`

Returns the serial number of a date months before or after.

**Parameters:**
- `start_date` (Union[datetime, float]): Start date or serial number.
- `months` (int): Number of months to add (positive) or subtract (negative).

**Returns:**
- `float`: Serial number of the resulting date.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import EDATE

start = datetime(2025, 1, 31)
# 3 months later
print(EDATE(start, 3))  # April 30, 2025

# 2 months earlier
print(EDATE(start, -2))  # November 30, 2024
```

**Cost:** O(1)

---

### `EOMONTH()`

Returns the serial number of the last day of the month.

**Parameters:**
- `start_date` (Union[datetime, float]): Start date or serial number.
- `months` (int): Number of months to add or subtract.

**Returns:**
- `float`: Serial number of the last day of the month.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import EOMONTH

start = datetime(2025, 1, 15)
# End of current month
print(EOMONTH(start, 0))  # January 31, 2025

# End of 3 months later
print(EOMONTH(start, 3))  # April 30, 2025
```

**Cost:** O(1)

---

### `YEARFRAC()`

Returns the fraction of year between two dates.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `basis` (int): Calculation basis (0 = US 30/360, others = Actual/Actual). Defaults to 0.

**Returns:**
- `float`: Year fraction.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import YEARFRAC

start = datetime(2025, 1, 1)
end = datetime(2025, 7, 1)
print(YEARFRAC(start, end))  # ~0.5 (half year)
```

**Cost:** O(1)

---

### `ISOWEEKNUM()`

Returns the ISO week number.

**Parameters:**
- `date` (datetime): Date to get the week number for.

**Returns:**
- `int`: ISO week number.

**Ejemplo:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import ISOWEEKNUM

date = datetime(2025, 6, 11)
print(ISOWEEKNUM(date))  # 24
```

**Cost:** O(1)

---

### `DATEDIF()`

Calculates the difference between dates in days, months, or years.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `unit` (str): Difference unit: "Y" (years), "M" (months), "D" (days).

**Returns:**
- `int`: Difference in the specified unit.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import DATEDIF

start = datetime(2020, 1, 1)
end = datetime(2025, 6, 15)

print(DATEDIF(start, end, "Y"))  # 5 (years)
print(DATEDIF(start, end, "M"))  # 65 (months)
print(DATEDIF(start, end, "D"))  # 1991 (days)
```

**Cost:** O(1)

---

### `WORKDAY()`

Returns the date after a number of working days.

**Parameters:**
- `start_date` (Union[float, datetime]): Start date.
- `days` (int): Number of working days to add.
- `holidays` (Optional[List[datetime]]): List of holidays.

**Returns:**
- `float`: Serial number of the resulting date.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import WORKDAY

start = datetime(2025, 1, 1)
# 10 working days later
result = WORKDAY(start, 10)
print(result)
```

**Cost:** O(1)

---

### `WORKDAY_INTL()`

Returns the date after working days with custom weekends.

**Parameters:**
- `start_date` (Union[float, datetime]): Start date.
- `days` (int): Number of working days.
- `weekend` (Union[int, str]): Weekend code. Defaults to 1.
- `holidays` (Optional[List[datetime]]): List of holidays.

**Returns:**
- `float`: Serial number of the resulting date.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import WORKDAY_INTL

start = datetime(2025, 1, 1)
# 10 working days with weekend Sunday-Monday
result = WORKDAY_INTL(start, 10, weekend=2)
print(result)
```

**Cost:** O(1)

---

### `excel_serial_to_year()`

Extracts the year from an Excel-style serial number or a datetime object. Equivalent to Excel's YEAR function.

**Parameters:**
- `serial_number` (Union[float, datetime]): Date value as Excel serial number or datetime.

**Returns:**
- `int`: The year as an integer.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_year

# With Excel serial number (44361 = June 15, 2021)
print(excel_serial_to_year(44361.0))  # 2021

# With datetime
print(excel_serial_to_year(datetime(2023, 10, 26)))  # 2023
```

**Cost:** O(1)

---

### `excel_serial_to_month()`

Extracts the month from an Excel-style serial number or a datetime object. Equivalent to Excel's MONTH function.

**Parameters:**
- `serial_number` (Union[float, datetime]): Date value as Excel serial number or datetime.

**Returns:**
- `int`: The month (1-12) as an integer.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_month

# With Excel serial number
print(excel_serial_to_month(44361.0))  # 6

# With datetime
print(excel_serial_to_month(datetime(2023, 10, 26)))  # 10
```

**Cost:** O(1)

---

### `excel_serial_to_weekday()`

Converts a serial number or datetime to day of the week. Equivalent to Excel's WEEKDAY function.

**Parameters:**
- `serial_number` (Union[float, datetime]): Date value.
- `return_type` (int, optional): Return type (1, 2, or 3). Defaults to 1.
  - 1: Sunday=1, Monday=2, ..., Saturday=7
  - 2: Monday=1, Tuesday=2, ..., Sunday=7
  - 3: Monday=0, Tuesday=1, ..., Sunday=6

**Returns:**
- `int`: The day of the week according to the return type.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_weekday

# Tuesday, June 15, 2021
print(excel_serial_to_weekday(44361.0, return_type=1))  # 3

# Thursday, October 26, 2023
print(excel_serial_to_weekday(datetime(2023, 10, 26), return_type=2))  # 4

# Sunday, October 29, 2023
print(excel_serial_to_weekday(datetime(2023, 10, 29), return_type=3))  # 6
```

**Cost:** O(1)

---

### `excel_serial_to_day()`

Converts a serial number or datetime to day of the month. Equivalent to Excel's DAY function.

**Parameters:**
- `serial_number` (Union[int, float, datetime]): Date represented as Excel serial number or datetime.

**Returns:**
- `int`: The day of the month (1-31).

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_day

# With serial number
print(excel_serial_to_day(44361))  # 15

# With datetime
print(excel_serial_to_day(datetime(2023, 10, 26)))  # 26
```

**Cost:** O(1)

---

### `excel_serial_to_hour()`

Extracts the hour component from an Excel-style serial number or datetime. Equivalent to Excel's HOUR function.

**Parameters:**
- `serial_number` (Union[float, datetime]): Date/time value.

**Returns:**
- `int`: The hour (0-23) as an integer.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_hour

# Represents 2021-06-15 18:30:45
print(excel_serial_to_hour(44361.771354166667))  # 18

# With datetime
print(excel_serial_to_hour(datetime(2023, 10, 26, 9, 15, 30)))  # 9
```

**Cost:** O(1)

---

### `excel_serial_to_minute()`

Extracts the minute component from an Excel-style serial number or datetime. Equivalent to Excel's MINUTE function.

**Parameters:**
- `serial_number` (Union[float, datetime]): Date/time value.

**Returns:**
- `int`: The minutes (0-59) as an integer.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_minute

# With datetime
print(excel_serial_to_minute(datetime(2023, 10, 26, 9, 15, 30)))  # 15
```

**Cost:** O(1)

---

## Excel Compatibility Notes

Functions in the fxExcel module are designed to emulate Excel's behavior, including:
- **Serial number system**: Days since 1899-12-30
- **30/360 calculation methods**: US and European methods for day count
- **Working day functions**: Customizable weekend definitions
- **Locale-independent**: Consistent results across different systems

### Serial Number System

Excel represents dates as serial numbers, where:
- January 1, 1900 = 1
- Each whole number represents one day
- Fractional parts represent time

```python
from datetime import datetime
from formulite.fxExcel.date_formulas import excel_serial_to_day

# 44361 represents June 15, 2021
print(excel_serial_to_day(44361))  # 15
```

### Weekend Codes

Functions like `DIAS_LAB_INTL` and `WORKDAY_INTL` support weekend codes:
- 1: Saturday-Sunday
- 2: Sunday-Monday
- 3: Monday-Tuesday
- 4: Tuesday-Wednesday
- 5: Wednesday-Thursday
- 6: Thursday-Friday
- 7: Friday-Saturday

---

## Engineering Functions

### Bessel Functions

#### `BESSELI()`

Returns the modified Bessel function In(x).

**Parameters:**
- `n` (Union[int, float]): Order of the Bessel function.
- `x` (Union[int, float]): Value at which to evaluate.

**Returns:**
- `float`: Modified Bessel function value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BESSELI

BESSELI(1, 1.5)  # 0.981666428
```

**Cost:** O(1)

---

#### `BESSELJ()`

Returns the Bessel function Jn(x).

**Parameters:**
- `n` (Union[int, float]): Order of the Bessel function.
- `x` (Union[int, float]): Value at which to evaluate.

**Returns:**
- `float`: Bessel function value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BESSELJ

BESSELJ(1, 1.5)  # 0.557936507
```

**Cost:** O(1)

---

#### `BESSELK()`

Returns the modified Bessel function Kn(x).

**Parameters:**
- `n` (Union[int, float]): Order of the Bessel function.
- `x` (Union[int, float]): Value at which to evaluate (must be positive).

**Returns:**
- `float`: Modified Bessel function value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BESSELK

BESSELK(1, 1.5)  # 0.277387804
```

**Cost:** O(1)

---

#### `BESSELY()`

Returns the Bessel function Yn(x).

**Parameters:**
- `n` (Union[int, float]): Order of the Bessel function.
- `x` (Union[int, float]): Value at which to evaluate (must be positive).

**Returns:**
- `float`: Bessel function value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BESSELY

BESSELY(1, 1.5)  # -0.412308627
```

**Cost:** O(1)

---

### Base Conversion Functions

#### `BIN2DEC()`

Converts a binary string to decimal.

**Parameters:**
- `binary_str` (str): Binary string.

**Returns:**
- `int`: Decimal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BIN2DEC

BIN2DEC("1010")  # 10
```

**Cost:** O(n)

---

#### `BIN2HEX()`

Converts a binary string to hexadecimal.

**Parameters:**
- `binary_str` (str): Binary string.

**Returns:**
- `str`: Hexadecimal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BIN2HEX

BIN2HEX("1010")  # 'A'
```

**Cost:** O(n)

---

#### `BIN2OCT()`

Converts a binary string to octal.

**Parameters:**
- `binary_str` (str): Binary string.

**Returns:**
- `str`: Octal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BIN2OCT

BIN2OCT("1010")  # '12'
```

**Cost:** O(n)

---

#### `DEC2BIN()`

Converts a decimal number to binary.

**Parameters:**
- `decimal` (int): Decimal number.

**Returns:**
- `str`: Binary representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import DEC2BIN

DEC2BIN(10)  # '1010'
```

**Cost:** O(log n)

---

#### `DEC2HEX()`

Converts a decimal number to hexadecimal.

**Parameters:**
- `decimal` (int): Decimal number.

**Returns:**
- `str`: Hexadecimal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import DEC2HEX

DEC2HEX(255)  # 'FF'
```

**Cost:** O(log n)

---

#### `DEC2OCT()`

Converts a decimal number to octal.

**Parameters:**
- `decimal` (int): Decimal number.

**Returns:**
- `str`: Octal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import DEC2OCT

DEC2OCT(8)  # '10'
```

**Cost:** O(log n)

---

#### `HEX2BIN()`

Converts a hexadecimal string to binary.

**Parameters:**
- `hex_str` (str): Hexadecimal string.

**Returns:**
- `str`: Binary representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import HEX2BIN

HEX2BIN("A")  # '1010'
```

**Cost:** O(n)

---

#### `HEX2DEC()`

Converts a hexadecimal string to decimal.

**Parameters:**
- `hex_str` (str): Hexadecimal string.

**Returns:**
- `int`: Decimal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import HEX2DEC

HEX2DEC("FF")  # 255
```

**Cost:** O(n)

---

#### `HEX2OCT()`

Converts a hexadecimal string to octal.

**Parameters:**
- `hex_str` (str): Hexadecimal string.

**Returns:**
- `str`: Octal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import HEX2OCT

HEX2OCT("A")  # '12'
```

**Cost:** O(n)

---

#### `OCT2BIN()`

Converts an octal string to binary.

**Parameters:**
- `octal_str` (str): Octal string.

**Returns:**
- `str`: Binary representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import OCT2BIN

OCT2BIN("12")  # '1010'
```

**Cost:** O(n)

---

#### `OCT2DEC()`

Converts an octal string to decimal.

**Parameters:**
- `octal_str` (str): Octal string.

**Returns:**
- `int`: Decimal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import OCT2DEC

OCT2DEC("12")  # 10
```

**Cost:** O(n)

---

#### `OCT2HEX()`

Converts an octal string to hexadecimal.

**Parameters:**
- `octal_str` (str): Octal string.

**Returns:**
- `str`: Hexadecimal representation.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import OCT2HEX

OCT2HEX("12")  # 'A'
```

**Cost:** O(n)

---

### Bitwise Operations

#### `BITAND()`

Performs a bitwise AND on two numbers.

**Parameters:**
- `number1` (int): First number.
- `number2` (int): Second number.

**Returns:**
- `int`: Result of bitwise AND.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BITAND

BITAND(5, 3)  # 1
```

**Cost:** O(1)

---

#### `BITOR()`

Performs a bitwise OR on two numbers.

**Parameters:**
- `number1` (int): First number.
- `number2` (int): Second number.

**Returns:**
- `int`: Result of bitwise OR.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BITOR

BITOR(5, 3)  # 7
```

**Cost:** O(1)

---

#### `BITXOR()`

Performs a bitwise XOR on two numbers.

**Parameters:**
- `number1` (int): First number.
- `number2` (int): Second number.

**Returns:**
- `int`: Result of bitwise XOR.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BITXOR

BITXOR(5, 3)  # 6
```

**Cost:** O(1)

---

#### `BITLSHIFT()`

Performs a left shift on a number.

**Parameters:**
- `number` (int): Number to shift.
- `shift` (int): Number of bits to shift left.

**Returns:**
- `int`: Result of left shift.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BITLSHIFT

BITLSHIFT(2, 2)  # 8
```

**Cost:** O(1)

---

#### `BITRSHIFT()`

Performs a right shift on a number.

**Parameters:**
- `number` (int): Number to shift.
- `shift` (int): Number of bits to shift right.

**Returns:**
- `int`: Result of right shift.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import BITRSHIFT

BITRSHIFT(8, 2)  # 2
```

**Cost:** O(1)

---

### Complex Number Functions

#### `COMPLEX()`

Creates a complex number from real and imaginary coefficients.

**Parameters:**
- `real` (Union[int, float]): Real coefficient.
- `imag` (Union[int, float]): Imaginary coefficient.
- `suffix` (str): Suffix ("i" or "j"). Defaults to "i".

**Returns:**
- `complex`: Complex number.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import COMPLEX

COMPLEX(3, 4)  # (3+4j)
```

**Cost:** O(1)

---

#### `IMABS()`

Returns the absolute value (modulus) of a complex number.

**Parameters:**
- `complex_num` (complex): Complex number.

**Returns:**
- `float`: Absolute value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMABS

IMABS(3+4j)  # 5.0
```

**Cost:** O(1)

---

#### `IMAGINARY()`

Returns the imaginary part of a complex number.

**Parameters:**
- `complex_num` (complex): Complex number.

**Returns:**
- `float`: Imaginary part.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMAGINARY

IMAGINARY(3+4j)  # 4.0
```

**Cost:** O(1)

---

#### `IMARGUMENT()`

Returns the argument (angle in radians) of a complex number.

**Parameters:**
- `complex_num` (complex): Complex number.

**Returns:**
- `float`: Argument in radians.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMARGUMENT

round(IMARGUMENT(3+4j), 4)  # 0.9273
```

**Cost:** O(1)

---

#### `IMCONJUGATE()`

Returns the complex conjugate.

**Parameters:**
- `complex_num` (complex): Complex number.

**Returns:**
- `complex`: Complex conjugate.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMCONJUGATE

IMCONJUGATE(3+4j)  # (3-4j)
```

**Cost:** O(1)

---

#### `IMCOS()`, `IMCOSH()`, `IMCOT()`, `IMCSC()`, `IMCSCH()`

Trigonometric and hyperbolic functions for complex numbers.

**Cost:** O(1) each

---

#### `IMDIV()`

Returns the quotient of two complex numbers.

**Parameters:**
- `complex_num1` (complex): Numerator.
- `complex_num2` (complex): Denominator.

**Returns:**
- `complex`: Quotient.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMDIV

IMDIV(6+8j, 2+0j)  # (3+4j)
```

**Cost:** O(1)

---

#### `IMEXP()`, `IMLN()`, `IMLOG10()`, `IMLOG2()`

Exponential and logarithmic functions for complex numbers.

**Cost:** O(1) each

---

#### `IMPOWER()`

Returns a complex number raised to a power.

**Parameters:**
- `complex_num` (complex): Base.
- `n` (Union[int, float]): Exponent.

**Returns:**
- `complex`: Result.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMPOWER

IMPOWER(2+3j, 2)  # (-5+12j)
```

**Cost:** O(1)

---

#### `IMPRODUCT()`

Returns the product of complex numbers.

**Parameters:**
- `*complex_nums` (complex): Variable number of complex numbers.

**Returns:**
- `complex`: Product.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMPRODUCT

IMPRODUCT(2+3j, 1+2j)  # (-4+7j)
```

**Cost:** O(n)

---

#### `IMREAL()`

Returns the real part of a complex number.

**Parameters:**
- `complex_num` (complex): Complex number.

**Returns:**
- `float`: Real part.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMREAL

IMREAL(3+4j)  # 3.0
```

**Cost:** O(1)

---

#### `IMSEC()`, `IMSECH()`, `IMSIN()`, `IMSINH()`, `IMTAN()`

Additional trigonometric functions for complex numbers.

**Cost:** O(1) each

---

#### `IMSQRT()`

Returns the square root of a complex number.

**Parameters:**
- `complex_num` (complex): Complex number.

**Returns:**
- `complex`: Square root.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMSQRT

IMSQRT(-1)  # 1j
```

**Cost:** O(1)

---

#### `IMSUB()`

Returns the difference between two complex numbers.

**Parameters:**
- `complex_num1` (complex): First number.
- `complex_num2` (complex): Second number.

**Returns:**
- `complex`: Difference.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMSUB

IMSUB(5+6j, 2+3j)  # (3+3j)
```

**Cost:** O(1)

---

#### `IMSUM()`

Returns the sum of complex numbers.

**Parameters:**
- `*complex_nums` (complex): Variable number of complex numbers.

**Returns:**
- `complex`: Sum.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import IMSUM

IMSUM(2+3j, 1+2j, 3+4j)  # (6+9j)
```

**Cost:** O(n)

---

### Error Functions

#### `ERF()`

Returns the error function erf(x).

**Parameters:**
- `x` (Union[int, float]): Value.

**Returns:**
- `float`: Error function value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import ERF

round(ERF(1), 5)  # 0.84270
```

**Cost:** O(1)

---

#### `ERFC()`

Returns the complementary error function erfc(x).

**Parameters:**
- `x` (Union[int, float]): Value.

**Returns:**
- `float`: Complementary error function value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import ERFC

round(ERFC(1), 5)  # 0.15730
```

**Cost:** O(1)

---

#### `ERF_PRECISE()`, `ERFC_PRECISE()`

Precise versions of error functions.

**Cost:** O(1) each

---

### Other Engineering Functions

#### `CONVERT()`

Converts a number from one measurement unit to another.

**Parameters:**
- `number` (Union[int, float]): Value to convert.
- `from_unit` (str): Source unit.
- `to_unit` (str): Target unit.

**Returns:**
- `float`: Converted value.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import CONVERT

CONVERT(100, 'cm', 'm')  # 1.0
CONVERT(1, 'kg', 'g')  # 1000.0
```

**Cost:** O(1)

---

#### `DELTA()`

Tests whether two values are equal.

**Parameters:**
- `value1` (Union[int, float]): First value.
- `value2` (Union[int, float]): Second value. Defaults to 0.

**Returns:**
- `int`: 1 if equal, 0 otherwise.

**Example:**
```python
from formulite.fxExcel.engineering_formulas import DELTA

DELTA(5, 5)  # 1
DELTA(5, 3)  # 0
```

**Cost:** O(1)

---

#### `GESTEP()`

Tests whether a number is greater than or equal to a threshold.

**Parameters:**
- `number` (Union[int, float]): Number to test.
- `threshold` (Union[int, float]): Threshold. Defaults to 0.

**Returns:**
- `int`: 1 if number >= threshold, 0 otherwise.
Database Functions

Database functions perform statistical and aggregate operations on structured data (lists of dictionaries). All functions accept optional criteria for filtering records.

### `DCOUNT()`

Counts cells containing numbers in a database field that match criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to count.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `int`: Count of numeric values matching criteria.

**Example:**
```python
from formulite.fxExcel.database_formulas import DCOUNT

db = [
    {'Name': 'Alice', 'Age': 30, 'Salary': 50000},
    {'Name': 'Bob', 'Age': 25, 'Salary': 45000},
    {'Name': 'Carol', 'Age': 35, 'Salary': 60000}
]

DCOUNT(db, 'Age', None)  # 3
DCOUNT(db, 'Age', {'Age': {'operator': '>', 'value': 25}})  # 2
```

**Cost:** O(n)

---

### `DCOUNTA()`

Counts non-empty cells in a database field that match criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to count.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `int`: Count of non-empty values matching criteria.

**Example:**
```python
from formulite.fxExcel.database_formulas import DCOUNTA

db = [
    {'Name': 'Alice', 'Age': 30},
    {'Name': 'Bob', 'Age': None},
    {'Name': 'Carol', 'Age': 35}
]

DCOUNTA(db, 'Age', None)  # 2
```

**Cost:** O(n)

---

### `DAVERAGE()`

Calculates the average of database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to average.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `float`: Average value, 0 if no values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DAVERAGE

db = [
    {'Product': 'A', 'Sales': 100},
    {'Product': 'B', 'Sales': 200},
    {'Product': 'A', 'Sales': 150}
]

DAVERAGE(db, 'Sales', None)  # 150.0
DAVERAGE(db, 'Sales', {'Product': 'A'})  # 125.0
```

**Cost:** O(n)

---

### `DGET()`

Extracts a single value from a database field that matches criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to extract.
- `criteria` (Dict[str, Any]): Dictionary with filtering criteria.

**Returns:**
- `Any`: Field value from the matching record, None if not found.

**Example:**
```python
from formulite.fxExcel.database_formulas import DGET

db = [
    {'Name': 'Alice', 'Age': 30},
    {'Name': 'Bob', 'Age': 25}
]

DGET(db, 'Age', {'Name': 'Alice'})  # 30
```

**Cost:** O(n)

---

### `DMAX()`

Returns the maximum value from database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to analyze.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `Union[int, float, None]`: Maximum value, None if no values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DMAX

db = [
    {'Product': 'A', 'Price': 10},
    {'Product': 'B', 'Price': 20},
    {'Product': 'A', 'Price': 15}
]

DMAX(db, 'Price', None)  # 20
DMAX(db, 'Price', {'Product': 'A'})  # 15
```

**Cost:** O(n)

---

### `DMIN()`

Returns the minimum value from database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to analyze.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `Union[int, float, None]`: Minimum value, None if no values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DMIN

db = [
    {'Product': 'A', 'Price': 10},
    {'Product': 'B', 'Price': 20},
    {'Product': 'A', 'Price': 15}
]

DMIN(db, 'Price', None)  # 10
DMIN(db, 'Price', {'Product': 'A'})  # 10
```

**Cost:** O(n)

---

### `DPRODUCT()`

Multiplies values from database field that match criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to multiply.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `Union[int, float]`: Product of values, 0 if no values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DPRODUCT

db = [
    {'Value': 2},
    {'Value': 3},
    {'Value': 4}
]

DPRODUCT(db, 'Value', None)  # 24
```

**Cost:** O(n)

---

### `DSTDEV()`

Calculates the sample standard deviation of database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to analyze.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `float`: Sample standard deviation, 0 if less than 2 values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DSTDEV

db = [
    {'Value': 10},
    {'Value': 20},
    {'Value': 30}
]

DSTDEV(db, 'Value', None)  # 10.0
```

**Cost:** O(n)

---

### `DSTDEVP()`

Calculates the population standard deviation of database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to analyze.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `float`: Population standard deviation, 0 if no values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DSTDEVP

db = [
    {'Value': 10},
    {'Value': 20},
    {'Value': 30}
]

round(DSTDEVP(db, 'Value', None), 2)  # 8.16
```

**Cost:** O(n)

---

### `DSUM()`

Sums values from database field that match criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to sum.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `Union[int, float]`: Sum of values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DSUM

db = [
    {'Category': 'A', 'Amount': 100},
    {'Category': 'B', 'Amount': 200},
    {'Category': 'A', 'Amount': 150}
]

DSUM(db, 'Amount', None)  # 450
DSUM(db, 'Amount', {'Category': 'A'})  # 250
```

**Cost:** O(n)

---

### `DVAR()`

Calculates the sample variance of database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to analyze.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `float`: Sample variance, 0 if less than 2 values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DVAR

db = [
    {'Value': 10},
    {'Value': 20},
    {'Value': 30}
]

DVAR(db, 'Value', None)  # 100.0
```

**Cost:** O(n)

---

### `DVARP()`

Calculates the population variance of database field values matching criteria.

**Parameters:**
- `database` (List[Dict[str, Any]]): List of dictionaries representing database records.
- `field` (str): Field name to analyze.
- `criteria` (Optional[Dict[str, Any]]): Optional dictionary with filtering criteria.

**Returns:**
- `float`: Population variance, 0 if no values.

**Example:**
```python
from formulite.fxExcel.database_formulas import DVARP

db = [
    {'Value': 10},
    {'Value': 20},
    {'Value': 30}
]

round(DVARP(db, 'Value', None), 2)  # 66.67
```

**Cost:** O(n)

---

## Financial Functions

Financial functions perform calculations for investments, loans, bonds, and securities.

### Depreciation Functions

#### `SLN()`

Calculate straight-line depreciation of an asset for one period.

**Parameters:**
- `cost` (Union[int, float]): Initial cost of the asset.
- `salvage` (Union[int, float]): Salvage value at the end of useful life.
- `life` (Union[int, float]): Number of periods over which the asset is depreciated.

**Returns:**
- `float`: Straight-line depreciation per period.

**Example:**
```python
from formulite.fxExcel.financial_formulas import SLN

SLN(30000, 7500, 10)  # 2250.0
```

**Cost:** O(1)

---

#### `DDB()`

Calculate depreciation using the double-declining balance method.

**Parameters:**
- `cost` (Union[int, float]): Initial cost of the asset.
- `salvage` (Union[int, float]): Salvage value at the end of useful life.
- `life` (Union[int, float]): Number of periods over which the asset is depreciated.
- `period` (int): Period for which to calculate depreciation.
- `factor` (Union[int, float]): Rate at which the balance declines (default 2).

**Returns:**
- `float`: Depreciation for the specified period.

**Example:**
```python
from formulite.fxExcel.financial_formulas import DDB

DDB(2400, 300, 10, 1)  # 480.0
```

**Cost:** O(n) where n is the period number

---

### Bond/Coupon Functions

#### `COUPDAYS()`

Return the number of days in the coupon period containing the settlement date.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).

**Returns:**
- `int`: Number of days in the coupon period.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import COUPDAYS

COUPDAYS(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)  # 181
```

**Cost:** O(1)

---

#### `COUPDAYBS()`

Return the number of days from the beginning of the coupon period to the settlement date.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).

**Returns:**
- `int`: Number of days from period start to settlement.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import COUPDAYBS

COUPDAYBS(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)  # 71
```

**Cost:** O(1)

---

#### `COUPDAYSNC()`

Return the number of days from the settlement date to the next coupon date.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).

**Returns:**
- `int`: Number of days from settlement to next coupon.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import COUPDAYSNC

COUPDAYSNC(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)  # 110
```

**Cost:** O(1)

---

#### `COUPPCD()`

Return the previous coupon date before the settlement date.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).

**Returns:**
- `datetime`: Previous coupon date.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import COUPPCD

COUPPCD(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
# datetime(2024, 11, 15, 0, 0)
```

**Cost:** O(k) where k is the number of coupons

---

#### `COUPNCD()`

Return the next coupon date after the settlement date.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).

**Returns:**
- `datetime`: Next coupon date.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import COUPNCD

COUPNCD(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
# datetime(2025, 5, 15, 0, 0)
```

**Cost:** O(k) where k is the number of coupons

---

#### `COUPNUM()`

Return the number of coupons payable between settlement and maturity dates.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).

**Returns:**
- `int`: Number of coupons remaining.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import COUPNUM

COUPNUM(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)  # 4
```

**Cost:** O(n) where n is the number of remaining coupons

---

### Duration Functions

#### `DURATION()`

Return the Macaulay duration for an assumed par value of 100.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `coupon` (float): Annual coupon rate.
- `yld` (float): Annual yield.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Macaulay duration.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import DURATION

DURATION(datetime(2025, 1, 1), datetime(2030, 1, 1), 0.08, 0.09, 2)  # ~4.2
```

**Cost:** O(n) where n is the number of coupons

---

#### `MDURATION()`

Return the modified duration for an assumed par value of 100.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `coupon` (float): Annual coupon rate.
- `yld` (float): Annual yield.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Modified duration.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import MDURATION

MDURATION(datetime(2025, 1, 1), datetime(2030, 1, 1), 0.08, 0.09, 2)  # ~4.0
```

**Cost:** O(n) where n is the number of coupons

---

### Accrued Interest Functions

#### `ACCRINT()`

Return the accrued interest for a security that pays periodic interest.

**Parameters:**
- `issue` (datetime): Issue date.
- `first_interest` (datetime): First interest date.
- `settlement` (datetime): Settlement date.
- `rate` (float): Annual coupon rate.
- `par` (Union[int, float]): Par value of the security.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Accrued interest.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import ACCRINT

ACCRINT(datetime(2025, 1, 1), datetime(2025, 7, 1), datetime(2025, 4, 1), 0.08, 1000, 2)  # 20.0
```

**Cost:** O(1)

---

#### `ACCRINTM()`

Return the accrued interest for a security that pays interest at maturity.

**Parameters:**
- `issue` (datetime): Issue date.
- `settlement` (datetime): Maturity date.
- `rate` (float): Annual coupon rate.
- `par` (Union[int, float]): Par value of the security.
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Accrued interest.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import ACCRINTM

ACCRINTM(datetime(2025, 1, 1), datetime(2025, 12, 31), 0.08, 1000)  # 80.0
```

**Cost:** O(1)

---

### Pricing Functions

#### `PRICE()`

Return the price per $100 face value of a security that pays periodic interest.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `rate` (float): Annual coupon rate.
- `yld` (float): Annual yield.
- `redemption` (Union[int, float]): Redemption value per $100 face value.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Price per $100 face value.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import PRICE

PRICE(datetime(2025, 2, 15), datetime(2032, 11, 15), 0.0575, 0.065, 100, 2)  # ~92.89
```

**Cost:** O(n) where n is the number of coupons

---

#### `PRICEDISC()`

Return the price per $100 face value of a discounted security.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `discount` (float): Security's discount rate.
- `redemption` (Union[int, float]): Redemption value per $100 face value.
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Price per $100 face value.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import PRICEDISC

PRICEDISC(datetime(2025, 2, 16), datetime(2025, 3, 1), 0.0525, 100)  # ~99.79
```

**Cost:** O(1)

---

#### `PRICEMAT()`

Return the price per $100 face value of a security that pays interest at maturity.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `issue` (datetime): Issue date.
- `rate` (float): Interest rate at date of issue.
- `yld` (float): Annual yield.
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Price per $100 face value.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import PRICEMAT

PRICEMAT(datetime(2025, 2, 15), datetime(2025, 4, 13), datetime(2024, 11, 11), 0.061, 0.061)  # ~99.98
```

**Cost:** O(1)

---

### Yield Functions

#### `YIELD()`

Return the yield of a security that pays periodic interest.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `rate` (float): Annual coupon rate.
- `pr` (Union[int, float]): Price per $100 face value.
- `redemption` (Union[int, float]): Redemption value per $100 face value.
- `frequency` (int): Number of coupon payments per year (1, 2, or 4).
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Annual yield.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import YIELD

YIELD(datetime(2025, 2, 15), datetime(2032, 11, 15), 0.0575, 95.04, 100, 2)  # ~0.065
```

**Cost:** O(n*m) where n is iterations and m is number of coupons

---

#### `YIELDDISC()`

Return the annual yield for a discounted security.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `pr` (Union[int, float]): Price per $100 face value.
- `redemption` (Union[int, float]): Redemption value per $100 face value.
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Annual yield.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import YIELDDISC

YIELDDISC(datetime(2025, 2, 16), datetime(2025, 3, 1), 99.795, 100)  # ~0.0525
```

**Cost:** O(1)

---

#### `YIELDMAT()`

Return the annual yield of a security that pays interest at maturity.

**Parameters:**
- `settlement` (datetime): Settlement date.
- `maturity` (datetime): Maturity date.
- `issue` (datetime): Issue date.
- `rate` (float): Interest rate at date of issue.
- `pr` (Union[int, float]): Price per $100 face value.
- `basis` (int): Day count basis (0=30/360, 1=actual/actual).

**Returns:**
- `float`: Annual yield.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import YIELDMAT

YIELDMAT(datetime(2025, 3, 15), datetime(2025, 11, 3), datetime(2024, 11, 8), 0.0625, 100.0123)  # ~0.0609
```

**Cost:** O(1)

---

### Loan Payment Functions

#### `CUMPRINC()`

Return the cumulative principal paid on a loan between two periods.

**Parameters:**
- `rate` (float): Interest rate per period.
- `nper` (int): Total number of payment periods.
- `pv` (Union[int, float]): Present value (loan amount).
- `start_period` (int): First period in the calculation (1-based).
- `end_period` (int): Last period in the calculation.
- `type` (int): Payment timing (0=end of period, 1=beginning of period).

**Returns:**
- `float`: Cumulative principal paid.

**Example:**
```python
from formulite.fxExcel.financial_formulas import CUMPRINC

CUMPRINC(0.09/12, 30*12, 125000, 1, 12, 0)  # ~-934.11
```

**Cost:** O(n) where n is the number of periods

---

#### `PPMT()`

Return the principal payment for a given period.

**Parameters:**
- `rate` (float): Interest rate per period.
- `per` (int): Period for which to calculate payment (1-based).
- `nper` (int): Total number of payment periods.
- `pv` (Union[int, float]): Present value (loan amount).
- `fv` (Union[int, float]): Future value (default 0).
- `type` (int): Payment timing (0=end of period, 1=beginning of period).

**Returns:**
- `float`: Principal payment for the period.

**Example:**
```python
from formulite.fxExcel.financial_formulas import PPMT

PPMT(0.08/12, 1, 10*12, 10000)  # ~-75.62
```

**Cost:** O(1)

---

### Cash Flow Functions

#### `XIRR()`

Return the internal rate of return for a schedule of cash flows.

**Parameters:**
- `values` (List[Union[int, float]]): Series of cash flows.
- `dates` (List[datetime]): Schedule of payment dates.
- `guess` (float): Initial guess for the rate (default 0.1).

**Returns:**
- `float`: Internal rate of return.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import XIRR

values = [-10000, 2750, 4250, 3250, 2750]
dates = [datetime(2008, 1, 1), datetime(2008, 3, 1), 
         datetime(2008, 10, 30), datetime(2009, 2, 15), datetime(2009, 4, 1)]
round(XIRR(values, dates), 4)  # 0.3733
```

**Cost:** O(n*m) where n is iterations and m is the number of cash flows

---

#### `XNPV()`

Return the net present value for a schedule of cash flows.
Information Functions

Information functions provide cell and system information, data type validation, and error handling.

### Cell & System Information

#### `CELL()`

Return information about the format, location, or contents of a cell.

**Note:** Not available in Excel for the Web.

**Parameters:**
- `info_type` (str): Type of information ("address", "col", "row", "contents", "type").
- `reference` (Any): Cell reference (optional).

**Returns:**
- `Any`: Requested cell information.

**Example:**
```python
from formulite.fxExcel.information_formulas import CELL

CELL("type", 42)  # 'v' (value)
CELL("type", "text")  # 'l' (label)
CELL("type", None)  # 'b' (blank)
```

**Cost:** O(1)

---

#### `INFO()`

Return information about the current operating environment.

**Note:** Not available in Excel for the Web.

**Parameters:**
- `type_text` (str): Type of information ("system", "release", "numfile", "osversion").

**Returns:**
- `Any`: Requested system information.

**Example:**
```python
from formulite.fxExcel.information_formulas import INFO

INFO("system")  # 'win32' or 'darwin' or 'linux'
```

**Cost:** O(1)

---

### Type Checking Functions (IS Functions)

#### `ISBLANK()`

Return TRUE if the value is blank.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if blank, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISBLANK

ISBLANK(None)  # True
ISBLANK("")  # True
ISBLANK("text")  # False
```

**Cost:** O(1)

---

#### `ISERR()`

Return TRUE if the value is any error value except #N/A.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if error (except #N/A), False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISERR

ISERR(ValueError())  # True
ISERR("#N/A")  # False
```

**Cost:** O(1)

---

#### `ISERROR()`

Return TRUE if the value is any error value.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if any error, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISERROR

ISERROR(ValueError())  # True
ISERROR(42)  # False
```

**Cost:** O(1)

---

#### `ISEVEN()`

Return TRUE if the number is even.

**Parameters:**
- `number` (Union[int, float]): Number to test.

**Returns:**
- `bool`: True if even, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISEVEN

ISEVEN(4)  # True
ISEVEN(3)  # False
```

**Cost:** O(1)

---

#### `ISLOGICAL()`

Return TRUE if the value is a logical value.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if boolean, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISLOGICAL

ISLOGICAL(True)  # True
ISLOGICAL(1)  # False
```

**Cost:** O(1)

---

#### `ISNA()`

Return TRUE if the value is the #N/A error value.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if #N/A, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISNA

ISNA("#N/A")  # True
ISNA(ValueError())  # False
```

**Cost:** O(1)

---

#### `ISNONTEXT()`

Return TRUE if the value is not text.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if not text, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISNONTEXT

ISNONTEXT(42)  # True
ISNONTEXT("text")  # False
```

**Cost:** O(1)

---

#### `ISNUMBER()`

Return TRUE if the value is a number.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if numeric, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISNUMBER

ISNUMBER(42)  # True
ISNUMBER(3.14)  # True
ISNUMBER("42")  # False
```

**Cost:** O(1)

---

#### `ISODD()`

Return TRUE if the number is odd.

**Parameters:**
- `number` (Union[int, float]): Number to test.

**Returns:**
- `bool`: True if odd, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISODD

ISODD(3)  # True
ISODD(4)  # False
```

**Cost:** O(1)

---

#### `ISOMITTED()`

Check if a value is missing in a LAMBDA expression.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if omitted, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISOMITTED
import inspect

ISOMITTED(inspect.Parameter.empty)  # True
ISOMITTED(42)  # False
```

**Cost:** O(1)

---

#### `ISTEXT()`

Return TRUE if the value is text.

**Parameters:**
- `value` (Any): Value to test.

**Returns:**
- `bool`: True if text, False otherwise.

**Example:**
```python
from formulite.fxExcel.information_formulas import ISTEXT

ISTEXT("hello")  # True
ISTEXT(42)  # False
```

**Cost:** O(1)

---

### Error Handling Functions

#### `ERROR.TYPE()`

Return a number corresponding to an error type.

**Parameters:**
- `error_val` (Any): Error value to analyze.

**Returns:**
- `Optional[int]`: Error number (1-7), or None if not an error.
  - 1: #NULL!
  - 2: #DIV/0!
  - 3: #VALUE!
  - 4: #REF!
  - 5: #NAME?
  - 6: #NUM!
  - 7: #N/A

**Example:**
```python
from formulite.fxExcel.information_formulas import ERROR_TYPE

ERROR_TYPE(ZeroDivisionError())  # 2
ERROR_TYPE(ValueError())  # 3
ERROR_TYPE(42)  # None
```

**Cost:** O(1)

---

## Logic Functions

Logic functions perform logical operations, conditional evaluation, and lambda calculations.

### Basic Logic Functions

#### `AND()`

Return TRUE if all arguments are TRUE.

**Parameters:**
- `*args` (Any): Logical values to evaluate.

**Returns:**
- `bool`: True if all arguments are True, False otherwise.

**Example:**
```python
from formulite.fxExcel.logic_formulas import AND

AND(True, True, True)  # True
AND(True, False, True)  # False
AND(5 > 3, 10 < 20)  # True
```

**Cost:** O(n) where n is the number of arguments

---

#### `OR()`

Return TRUE if any argument is TRUE.

**Parameters:**
- `*args` (Any): Logical values to evaluate.

**Returns:**
- `bool`: True if any argument is True, False otherwise.

**Example:**
```python
from formulite.fxExcel.logic_formulas import OR

OR(False, True, False)  # True
OR(False, False, False)  # False
OR(5 < 3, 10 > 20, 2 == 2)  # True
```

**Cost:** O(n) where n is the number of arguments

---

#### `NOT()`

Reverse the logical value of its argument.

**Parameters:**
- `value` (Any): Logical value to invert.

**Returns:**
- `bool`: Inverted logical value.

**Example:**
```python
from formulite.fxExcel.logic_formulas import NOT

NOT(True)  # False
NOT(False)  # True
NOT(5 > 10)  # True
```

**Cost:** O(1)

---

#### `XOR()`

Return a logical exclusive OR of all arguments.

**Parameters:**
- `*args` (Any): Logical values to evaluate.

**Returns:**
- `bool`: True if an odd number of arguments are True, False otherwise.

**Example:**
```python
from formulite.fxExcel.logic_formulas import XOR

XOR(True, False, False)  # True (1 True)
XOR(True, True, False)  # False (2 Trues)
XOR(True, True, True)  # True (3 Trues)
```

**Cost:** O(n) where n is the number of arguments

---

#### `TRUE()`

Return the logical value TRUE.

**Returns:**
- `bool`: True

**Example:**
```python
from formulite.fxExcel.logic_formulas import TRUE

TRUE()  # True
```

**Cost:** O(1)

---

#### `FALSE()`

Return the logical value FALSE.

**Returns:**
- `bool`: False

**Example:**
```python
from formulite.fxExcel.logic_formulas import FALSE

FALSE()  # False
```

**Cost:** O(1)

---

### Conditional Functions

#### `IF()`

Perform a logical test and return one value for TRUE and another for FALSE.

**Parameters:**
- `logical_test` (Any): Condition to evaluate.
- `value_if_true` (Any): Value to return if condition is True.
- `value_if_false` (Any): Value to return if condition is False (optional).

**Returns:**
- `Any`: value_if_true if test is True, otherwise value_if_false.

**Example:**
```python
from formulite.fxExcel.logic_formulas import IF

IF(10 > 5, "Yes", "No")  # 'Yes'
IF(3 < 2, "Yes", "No")  # 'No'
IF(100 >= 100, "Pass", "Fail")  # 'Pass'
```

**Cost:** O(1)

---

#### `IFS()`

Check multiple conditions and return the value corresponding to the first TRUE condition.

**Parameters:**
- `*args` (Any): Pairs of condition and value (cond1, val1, cond2, val2, ..., default).

**Returns:**
- `Any`: Value corresponding to the first True condition, or default value.

**Raises:**
- `ValueError`: If number of arguments is even (missing default value).

**Example:**
```python
from formulite.fxExcel.logic_formulas import IFS

score = 85
IFS(
    score >= 90, "A",
    score >= 80, "B",
    score >= 70, "C",
    "F"
)  # 'B'
```

**Cost:** O(n) where n is the number of condition pairs

---

#### `IFERROR()`

Return a value if an expression results in an error, otherwise return the expression result.

**Parameters:**
- `value` (Union[Callable, Any]): Expression to evaluate (callable) or direct value.
- `value_if_error` (Any): Value to return if error occurs.

**Returns:**
- `Any`: Result of expression or value_if_error if error occurs.

**Example:**
```python
from formulite.fxExcel.logic_formulas import IFERROR

IFERROR(lambda: 10 / 2, "Error")  # 5.0
IFERROR(lambda: 10 / 0, "Error")  # 'Error'
IFERROR(lambda: int("abc"), 0)  # 0
```

**Cost:** O(1)

---

#### `IFNA()`

Return a value if the expression results in #N/A or None, otherwise return the expression result.

**Parameters:**
- `value` (Union[Callable, Any]): Expression to evaluate (callable) or direct value.
- `value_if_na` (Any): Value to return if result is None or #N/A.

**Returns:**
- `Any`: Result of expression or value_if_na if result is None.

**Example:**
```python
from formulite.fxExcel.logic_formulas import IFNA

IFNA(lambda: None, "N/A")  # 'N/A'
IFNA(lambda: 42, "N/A")  # 42
IFNA("#N/A", "Not Available")  # 'Not Available'
```

**Cost:** O(1)

---

### Lambda Functions

#### `LAMBDA()`

Create a reusable lambda function with named parameters.

**Parameters:**
- `*args` (Any): Parameter names for the lambda.
- `expression` (Optional[Callable]): Lambda expression as a callable function.

**Returns:**
- `Callable`: Lambda function that can be called with specified arguments.

**Raises:**
- `ValueError`: If 'expression' argument is missing.

**Example:**
```python
from formulite.fxExcel.logic_formulas import LAMBDA

add = LAMBDA(expression=lambda x, y: x + y)
add(5, 3)  # 8

multiply = LAMBDA(expression=lambda a, b, c: a * b * c)
multiply(2, 3, 4)  # 24
```

**Cost:** O(1)

---

#### `LET()`

Assign names to calculation results and evaluate a final expression.

**Parameters:**
- `**kwargs` (Any): Name-value pairs where the last pair must be 'expression' with the function to evaluate.

**Returns:**
- `Any`: Result of the final expression using the assigned names.

**Raises:**
- `ValueError`: If 'expression' argument is missing.

**Example:**
```python
from formulite.fxExcel.logic_formulas import LET

LET(x=5, y=3, expression=lambda x, y: x + y)  # 8
LET(
    price=100,
    tax_rate=0.15,
    expression=lambda price, tax_rate: price * (1 + tax_rate)
)  # 115.0
```

**Cost:** O(1)

---

#### `BYCOL()`

Apply a LAMBDA to each column and return an array of results.

**Parameters:**
- `array` (List[List[Any]]): List of lists (matrix) where each sublist is a row.
- `lambda_func` (Callable[[List[Any]], Any]): Lambda function that takes a list (column) as argument.

**Returns:**
- `List[Any]`: Results of applying lambda_func to each column.

**Example:**
```python
from formulite.fxExcel.logic_formulas import BYCOL

matrix = [[1, 2, 3], [4, 5, 6]]
BYCOL(matrix, lambda col: sum(col))  # [5, 7, 9]
BYCOL(matrix, lambda col: max(col))  # [4, 5, 6]
```

**Cost:** O(r * c) where r is rows and c is columns

---

#### `BYROW()`

Apply a LAMBDA to each row and return an array of results.

**Parameters:**
- `array` (List[List[Any]]): List of lists (matrix) where each sublist is a row.
- `lambda_func` (Callable[[List[Any]], Any]): Lambda function that takes a list (row) as argument.

**Returns:**
- `List[Any]`: Results of applying lambda_func to each row.

**Example:**
```python
from formulite.fxExcel.logic_formulas import BYROW

matrix = [[1, 2, 3], [4, 5, 6]]
BYROW(matrix, lambda row: sum(row))  # [6, 15]
BYROW(matrix, lambda row: max(row))  # [3, 6]
```

**Cost:** O(r) where r is the number of rows

---

## 
**Parameters:**
- `rate` (float): Discount rate to apply.
- `values` (List[Union[int, float]]): Series of cash flows.
- `dates` (List[datetime]): Schedule of payment dates.

**Returns:**
- `float`: Net present value.

**Example:**
```python
from datetime import datetime
from formulite.fxExcel.financial_formulas import XNPV

values = [-10000, 2750, 4250, 3250, 2750]
dates = [datetime(2008, 1, 1), datetime(2008, 3, 1), 
         datetime(2008, 10, 30), datetime(2009, 2, 15), datetime(2009, 4, 1)]
round(XNPV(0.09, values, dates), 2)  # 2086.65
```

**Cost:** O(n) where n is the number of cash flows

---

## Statistical Functions

### `CORREL()`

Returns the correlation coefficient between two datasets.

**Parameters:**
- `data1` (List[float]): First dataset
- `data2` (List[float]): Second dataset

**Returns:**
- `float`: Correlation coefficient between -1 and 1

**Example:**
```python
from formulite.fxExcel.statistic_formulas import CORREL

data1 = [3, 2, 4, 5, 6]
data2 = [9, 7, 12, 15, 17]
print(CORREL(data1, data2))  # 0.997
```

**Cost:** O(n)

---

### `COUNT()`

Counts the number of numeric values in a list.

**Parameters:**
- `*args` (Union[float, int]): Values to count

**Returns:**
- `int`: Count of numeric values

**Example:**
```python
from formulite.fxExcel.statistic_formulas import COUNT

print(COUNT(1, 2, "text", 3, None, 4))  # 4
```

**Cost:** O(n)

---

### `COUNTA()`

Counts all non-None values in a list.

**Parameters:**
- `*args` (Any): Values to count

**Returns:**
- `int`: Count of non-None values

**Example:**
```python
from formulite.fxExcel.statistic_formulas import COUNTA

print(COUNTA(1, 2, "text", 3, None, 4))  # 5
```

**Cost:** O(n)

---

### `COUNTIF()`

Counts cells in range that meet a criterion.

**Parameters:**
- `rango` (List[Any]): Range of values
- `criterio` (Any): Criterion to match (supports operators: >, <, >=, <=, =)

**Returns:**
- `int`: Count of matching values

**Example:**
```python
from formulite.fxExcel.statistic_formulas import COUNTIF

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(COUNTIF(data, ">5"))  # 5
print(COUNTIF(data, 5))  # 1
```

**Cost:** O(n)

---

### `COUNTBLANK()`

Counts blank (None or empty string) cells in a range.

**Parameters:**
- `rango` (List[Any]): Range to check

**Returns:**
- `int`: Count of blank cells

**Example:**
```python
from formulite.fxExcel.statistic_formulas import countblank

data = [1, None, "", 2, None, 3]
print(countblank(data))  # 3
```

**Cost:** O(n)

---

### `COVARIANCE_P()`

Returns the population covariance.

**Parameters:**
- `data1` (List[float]): First dataset
- `data2` (List[float]): Second dataset

**Returns:**
- `float`: Population covariance

**Example:**
```python
from formulite.fxExcel.statistic_formulas import covariance_p

data1 = [3, 2, 4, 5, 6]
data2 = [9, 7, 12, 15, 17]
print(covariance_p(data1, data2))  # 5.2
```

**Cost:** O(n)

---

### `KURT()`

Returns the kurtosis of a dataset (excess kurtosis using Fisher's definition).

**Parameters:**
- `data` (List[float]): Dataset

**Returns:**
- `float`: Kurtosis value

**Example:**
```python
from formulite.fxExcel.statistic_formulas import KURT

data = [3, 4, 5, 2, 3, 4, 5, 6, 4, 7]
print(KURT(data))  # -0.1518
```

**Cost:** O(n)

---

### `BETA_DIST()`

Returns the beta cumulative distribution function.

**Parameters:**
- `x` (float): Value at which to evaluate
- `alpha` (float): First shape parameter
- `beta` (float): Second shape parameter
- `a` (float, optional): Lower bound (default: 0)
- `b` (float, optional): Upper bound (default: 1)

**Returns:**
- `float`: Cumulative probability

**Example:**
```python
from formulite.fxExcel.statistic_formulas import BETA_DIST

print(BETA_DIST(0.5, 2, 3))  # 0.6875
```

**Cost:** O(1)

---

### `BINOM_DIST()`

Returns the binomial distribution probability.

**Parameters:**
- `k` (int): Number of successes
- `n` (int): Number of trials
- `p` (float): Probability of success

**Returns:**
- `float`: Probability mass

**Example:**
```python
from formulite.fxExcel.statistic_formulas import BINOM_DIST

print(BINOM_DIST(6, 10, 0.5))  # 0.205
```

**Cost:** O(1)

---

### `LINEST()`

Returns linear regression parameters (slope and intercept).

**Parameters:**
- `known_y` (List[float]): Known y-values
- `known_x` (List[float], optional): Known x-values (defaults to 1, 2, 3, ...)

**Returns:**
- `tuple`: (slope, intercept)

**Example:**
```python
from formulite.fxExcel.statistic_formulas import LINEST

y = [1, 2, 3, 4, 5]
slope, intercept = LINEST(y)
print(f"Slope: {slope}, Intercept: {intercept}")  # Slope: 1.0, Intercept: 1.0
```

**Cost:** O(n)

---

### `FISHER()`

Returns the Fisher transformation.

**Parameters:**
- `r` (float): Correlation coefficient (-1 < r < 1)

**Returns:**
- `float`: Fisher transformation value

**Example:**
```python
from formulite.fxExcel.statistic_formulas import fisher

print(fisher(0.75))  # 0.9730
```

**Cost:** O(1)

---

### `FORECAST_LINEAR()`

Returns a linear forecast value.

**Parameters:**
- `x` (float): Value for which to forecast
- `known_y` (List[float]): Known y-values
- `known_x` (List[float], optional): Known x-values

**Returns:**
- `float`: Forecasted value

**Example:**
```python
from formulite.fxExcel.statistic_formulas import forecast_linear

y = [6, 7, 9, 15, 21]
x_vals = [1, 2, 3, 4, 5]
print(forecast_linear(6, y, x_vals))  # 27.0
```

**Cost:** O(n)

---

### `FREQUENCY()`

Returns frequency distribution.

**Parameters:**
- `data` (List[float]): Data array
- `bins` (List[float]): Bin edges

**Returns:**
- `List[int]`: Frequency counts for each bin

**Example:**
```python
from formulite.fxExcel.statistic_formulas import FREQUENCY

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bins = [3, 6, 9]
print(FREQUENCY(data, bins))  # [2, 3, 3]
```

**Cost:** O(n log n)

---

### `GAMMA()`

Returns the gamma function value.

**Parameters:**
- `x` (float): Input value

**Returns:**
- `float`: Gamma(x)

**Example:**
```python
from formulite.fxExcel.statistic_formulas import gamma

print(gamma(5))  # 24.0 (equivalent to 4!)
```

**Cost:** O(1)

---

### `CONFIDENCE_T()`

Returns confidence interval for population mean using t-distribution.

**Parameters:**
- `data` (List[float]): Sample data
- `alpha` (float, optional): Significance level (default: 0.05)

**Returns:**
- `tuple`: (lower_bound, upper_bound)

**Example:**
```python
from formulite.fxExcel.statistic_formulas import CONFIDENCE_T

data = [10, 12, 14, 16, 18, 20]
lower, upper = CONFIDENCE_T(data)
print(f"95% CI: ({lower:.2f}, {upper:.2f})")
```

**Cost:** O(n)

---

### `LARGE()`

Returns the kth largest value.

**Parameters:**
- `data` (List[float]): Dataset
- `k` (int): Position (1 = largest, 2 = second largest, etc.)

**Returns:**
- `float`: Kth largest value

**Example:**
```python
from formulite.fxExcel.statistic_formulas import LARGE

data = [3, 4, 5, 2, 3, 4, 6, 4, 7]
print(LARGE(data, 3))  # 5 (third largest)
```

**Cost:** O(n log n)

---

### `HARMEAN()`

Returns the harmonic mean.

**Parameters:**
- `data` (List[float]): Dataset (all values must be non-zero)

**Returns:**
- `float`: Harmonic mean

**Example:**
```python
from formulite.fxExcel.statistic_formulas import HARMEAN

data = [4, 5, 8, 7, 11, 4, 3]
print(HARMEAN(data))  # 5.028
```

**Cost:** O(n)

---

### `GEOMEAN()`

Returns the geometric mean.

**Parameters:**
- `data` (List[float]): Dataset (all values must be positive)

**Returns:**
- `float`: Geometric mean

**Example:**
```python
from formulite.fxExcel.statistic_formulas import GEOMEAN

data = [4, 5, 8, 7, 11, 4, 3]
print(GEOMEAN(data))  # 5.476
```

**Cost:** O(n)

---

## Text & Data Functions

### `CONCATENATE()`

Joins several text strings into one text string.

**Description:**
Concatenates multiple strings into a single text string. Similar to the & operator. CONCATENATE does not provide delimiters or ignore empty arguments.

**Parameters:**
- `*args`: Text strings to be joined. Can accept multiple arguments.

**Returns:**
- `str`: The concatenated text string.

**Example:**
```python
from formulite.fxExcel.text_formulas import CONCATENATE

print(CONCATENATE("Hello", " ", "World"))  # 'Hello World'
print(CONCATENATE("Value: ", 100))  # 'Value: 100'
print(CONCATENATE("A", "B", "C", "D"))  # 'ABCD'
```

**Cost:** O(n), where n is the total length of all strings.

---

### `CONCAT()`

Alias for CONCATENATE (Excel 2016+ name).

**Description:**
CONCAT is an alias for CONCATENATE. In Excel, CONCAT supports array ranges, but in this Python library both names refer to the same function since there are no Excel ranges.

**Parameters:**
- `*args`: Text strings or values to be joined.

**Returns:**
- `str`: The concatenated text string.

**Example:**
```python
from formulite.fxExcel.text_formulas import CONCAT

print(CONCAT("Sun", "flower"))  # 'Sunflower'
print(CONCAT("Zip code: ", 90210))  # 'Zip code: 90210'
```

**Cost:** O(n), where n is the total length of all strings.

**Note:** CONCAT and CONCATENATE are identical in this library.

---

### `TEXTJOIN()`

Combines text from multiple ranges with a delimiter.

**Description:**
Joins text strings using a delimiter and can optionally ignore empty strings. More powerful than CONCATENATE as it allows a delimiter between values.

**Parameters:**
- `delimiter`: Text string to use as separator between values.
- `ignore_empty`: If True, ignores empty cells/strings.
- `*args`: Text values to join.

**Returns:**
- `str`: The joined text string with delimiters.

**Example:**
```python
from formulite.fxExcel.text_formulas import TEXTJOIN

print(TEXTJOIN(", ", True, "Red", "", "Blue", "Green"))  # 'Red, Blue, Green'
print(TEXTJOIN("-", False, 2024, 1, 15))  # '2024-1-15'
print(TEXTJOIN(" ", True, "Hello", None, "World"))  # 'Hello World'
```

**Cost:** O(n), where n is the total length of all strings and delimiter.

---

### `LEFT()`

Returns the leftmost characters from a text string.

**Description:**
Extracts a specified number of characters from the start of a text string. Similar to Excel's LEFT function.

**Parameters:**
- `text`: Text string containing the characters to extract.
- `num_chars`: Number of characters to extract (default: 1).

**Returns:**
- `str`: The leftmost characters from the text string.

**Example:**
```python
from formulite.fxExcel.text_formulas import LEFT

print(LEFT("Sale Price", 4))  # 'Sale'
print(LEFT("Sweden"))  # 'S'
print(LEFT("Quarterly Report", 9))  # 'Quarterly'
```

**Cost:** O(k), where k is num_chars.

---

### `RIGHT()`

Returns the rightmost characters from a text string.

**Description:**
Extracts a specified number of characters from the end of a text string. Similar to Excel's RIGHT function.

**Parameters:**
- `text`: Text string containing the characters to extract.
- `num_chars`: Number of characters to extract (default: 1).

**Returns:**
- `str`: The rightmost characters from the text string.

**Example:**
```python
from formulite.fxExcel.text_formulas import RIGHT

print(RIGHT("Sale Price", 5))  # 'Price'
print(RIGHT("Stock Number"))  # 'r'
print(RIGHT("2024-Q1", 2))  # 'Q1'
```

**Cost:** O(k), where k is num_chars.

---

### `MID()`

Returns characters from the middle of a text string.

**Description:**
Extracts a substring from a text string given a starting position and length. Uses 1-based indexing like Excel (first character is position 1).

**Parameters:**
- `text`: Text string containing the characters to extract.
- `start_num`: Position of the first character (1-based indexing).
- `num_chars`: Number of characters to extract.

**Returns:**
- `str`: The extracted substring.

**Example:**
```python
from formulite.fxExcel.text_formulas import MID

print(MID("Fluid Flow", 1, 5))  # 'Fluid'
print(MID("Fluid Flow", 7, 4))  # 'Flow'
print(MID("Quarterly Report 2024", 11, 6))  # 'Report'
```

**Cost:** O(k), where k is num_chars.

---

### `LEN()`

Returns the number of characters in a text string.

**Description:**
Counts the total number of characters including spaces. Similar to Excel's LEN function.

**Parameters:**
- `text`: Text string whose length you want to find.

**Returns:**
- `int`: The number of characters in the text.

**Example:**
```python
from formulite.fxExcel.text_formulas import LEN

print(LEN("Phoenix, AZ"))  # 11
print(LEN(""))  # 0
print(LEN("  spaces  "))  # 10
```

**Cost:** O(1) for most implementations, O(n) for Unicode grapheme counting.

---

### `FIND()`

Finds one text string within another (case-sensitive).

**Description:**
Returns the starting position of find_text within within_text. FIND is case-sensitive and doesn't allow wildcard characters. Uses 1-based indexing like Excel.

**Parameters:**
- `find_text`: The text you want to find.
- `within_text`: The text containing the text you want to find.
- `start_num`: The character position to start searching (default: 1).

**Returns:**
- `int`: The position of the first character of find_text (1-based).

**Example:**
```python
from formulite.fxExcel.text_formulas import FIND

print(FIND("M", "Miriam McGovern"))  # 1
print(FIND("m", "Miriam McGovern"))  # 6
print(FIND("M", "Miriam McGovern", 3))  # 8
```

**Cost:** O(n*m), where n is length of within_text and m is length of find_text.

---

### `SEARCH()`

Finds one text string within another (case-insensitive).

**Description:**
Returns the starting position of find_text within within_text. SEARCH is case-insensitive and allows wildcard characters (? and *). Uses 1-based indexing like Excel.

**Parameters:**
- `find_text`: The text you want to find (can use ? and * wildcards).
- `within_text`: The text containing the text you want to find.
- `start_num`: The character position to start searching (default: 1).

**Returns:**
- `int`: The position of the first character of find_text (1-based).

**Example:**
```python
from formulite.fxExcel.text_formulas import SEARCH

print(SEARCH("e", "Statements", 6))  # 7
print(SEARCH("margin", "Profit Margin"))  # 8
print(SEARCH("M", "miriam mcgovern"))  # 1
```

**Cost:** O(n*m), where n is length of within_text and m is length of find_text.

---

### `SUBSTITUTE()`

Substitutes new text for old text in a text string.

**Description:**
Replaces existing text with new text in a string. If instance_num is specified, only that occurrence is replaced; otherwise all occurrences are replaced.

**Parameters:**
- `text`: The text in which you want to substitute characters.
- `old_text`: The text you want to replace.
- `new_text`: The text you want to replace old_text with.
- `instance_num`: Which occurrence to replace (optional, default: all).

**Returns:**
- `str`: The text with substitutions made.

**Example:**
```python
from formulite.fxExcel.text_formulas import SUBSTITUTE

print(SUBSTITUTE("Sales Data", "Sales", "Cost"))  # 'Cost Data'
print(SUBSTITUTE("Quarter 1, 2023", "1", "2", 1))  # 'Quarter 2, 2023'
print(SUBSTITUTE("apple apple", "apple", "orange"))  # 'orange orange'
```

**Cost:** O(n), where n is the length of the text.

---

### `REPLACE()`

Replaces part of a text string with a different text string.

**Description:**
Replaces a specified number of characters at a specific position. Uses 1-based indexing like Excel.

**Parameters:**
- `old_text`: Text in which you want to replace characters.
- `start_num`: Position of the first character to replace (1-based).
- `num_chars`: Number of characters to replace.
- `new_text`: Text that will replace characters in old_text.

**Returns:**
- `str`: The text with replacements made.

**Example:**
```python
from formulite.fxExcel.text_formulas import REPLACE

print(REPLACE("abcdefghijk", 6, 5, "*"))  # 'abcde*k'
print(REPLACE("2024", 3, 2, "25"))  # '2025'
print(REPLACE("XYZ123", 4, 3, "456"))  # 'XYZ456'
```

**Cost:** O(n), where n is the length of old_text.

---

### `UPPER()`

Converts text to uppercase.

**Description:**
Converts all lowercase letters in a text string to uppercase. Numbers and punctuation are not affected.

**Parameters:**
- `text`: The text you want to convert to uppercase.

**Returns:**
- `str`: The text converted to uppercase.

**Example:**
```python
from formulite.fxExcel.text_formulas import UPPER

print(UPPER("total"))  # 'TOTAL'
print(UPPER("E. E. Cummings"))  # 'E. E. CUMMINGS'
print(UPPER("Yield-12%"))  # 'YIELD-12%'
```

**Cost:** O(n), where n is the length of the text.

---

### `LOWER()`

Converts text to lowercase.

**Description:**
Converts all uppercase letters in a text string to lowercase. Numbers and punctuation are not affected.

**Parameters:**
- `text`: The text you want to convert to lowercase.

**Returns:**
- `str`: The text converted to lowercase.

**Example:**
```python
from formulite.fxExcel.text_formulas import LOWER

print(LOWER("E. E. Cummings"))  # 'e. e. cummings'
print(LOWER("PAID IN FULL"))  # 'paid in full'
print(LOWER("ABC-123"))  # 'abc-123'
```

**Cost:** O(n), where n is the length of the text.

---

### `PROPER()`

Capitalizes the first letter in each word of a text string.

**Description:**
Converts a text string to proper case: the first letter in each word is uppercase, and all other letters are lowercase.

**Parameters:**
- `text`: Text to convert to proper case.

**Returns:**
- `str`: The text in proper case.

**Example:**
```python
from formulite.fxExcel.text_formulas import PROPER

print(PROPER("this is a TITLE"))  # 'This Is A Title'
print(PROPER("2-way street"))  # '2-Way Street'
print(PROPER("76BudGet"))  # '76Budget'
```

**Cost:** O(n), where n is the length of the text.

---

### `TRIM()`

Removes all spaces from text except single spaces between words.

**Description:**
Removes leading and trailing spaces, and reduces multiple spaces between words to a single space.

**Parameters:**
- `text`: The text from which you want spaces removed.

**Returns:**
- `str`: The text with extra spaces removed.

**Example:**
```python
from formulite.fxExcel.text_formulas import TRIM

print(TRIM("  First Quarter   Earnings  "))  # 'First Quarter Earnings'
print(TRIM("Hello     World"))  # 'Hello World'
print(TRIM("   text   "))  # 'text'
```

**Cost:** O(n), where n is the length of the text.

---

### `CLEAN()`

Removes all nonprintable characters from text.

**Description:**
Removes characters with ASCII values 0-31 (nonprintable characters). Useful for cleaning text imported from other applications.

**Parameters:**
- `text`: Text from which you want to remove nonprintable characters.

**Returns:**
- `str`: The cleaned text.

**Example:**
```python
from formulite.fxExcel.text_formulas import CLEAN

print(CLEAN("Monthly Report\\n\\r\\t2024"))  # 'Monthly Report2024'
print(CLEAN("Hello\\x00World"))  # 'HelloWorld'
```

**Cost:** O(n), where n is the length of the text.

---

### `CHAR()`

Returns the character specified by the code number.

**Description:**
Converts a number into a character according to the Unicode character set. Similar to Excel's CHAR function.

**Parameters:**
- `number`: A number between 1 and 1114111 (Unicode code point).

**Returns:**
- `str`: The character corresponding to the code number.

**Example:**
```python
from formulite.fxExcel.text_formulas import CHAR

print(CHAR(65))  # 'A'
print(CHAR(97))  # 'a'
print(CHAR(33))  # '!'
```

**Cost:** O(1), constant time operation.

---

### `CODE()`

Returns a numeric code for the first character in a text string.

**Description:**
Returns the Unicode code point value of the first character. Similar to Excel's CODE function.

**Parameters:**
- `text`: The text for which you want the code of the first character.

**Returns:**
- `int`: The numeric code for the first character.

**Example:**
```python
from formulite.fxExcel.text_formulas import CODE

print(CODE("A"))  # 65
print(CODE("Apple"))  # 65
print(CODE("!"))  # 33
```

**Cost:** O(1), constant time operation.

---

### `EXACT()`

Checks whether two text strings are exactly the same.

**Description:**
Compares two text strings and returns True if they are exactly the same (case-sensitive), False otherwise.

**Parameters:**
- `text1`: The first text string.
- `text2`: The second text string.

**Returns:**
- `bool`: True if the strings are identical, False otherwise.

**Example:**
```python
from formulite.fxExcel.text_formulas import EXACT

print(EXACT("Word", "word"))  # False
print(EXACT("Word", "Word"))  # True
print(EXACT("abc", "abc"))  # True
```

**Cost:** O(n), where n is the length of the strings.

---

### `REPT()`

Repeats text a given number of times.

**Description:**
Returns text repeated a specified number of times. Use REPT to fill a cell with a number of instances of a text string.

**Parameters:**
- `text`: The text you want to repeat.
- `number_times`: A positive number specifying the number of times to repeat.

**Returns:**
- `str`: The repeated text.

**Example:**
```python
from formulite.fxExcel.text_formulas import REPT

print(REPT("*-", 3))  # '*-*-*-'
print(REPT("=", 5))  # '====='
print(REPT("AB", 2))  # 'ABAB'
```

**Cost:** O(n*m), where n is the length of text and m is number_times.

---

### `TEXT()`

Formats a number and converts it to text.

**Description:**
Converts a value to text in a specified number format. Simplified version supporting basic formats.

**Parameters:**
- `value`: A numeric value to format.
- `format_text`: A number format as a text string (e.g., "0.00", "#,##0").

**Returns:**
- `str`: The formatted text.

**Example:**
```python
from formulite.fxExcel.text_formulas import TEXT

print(TEXT(1234.567, "0.00"))  # '1234.57'
print(TEXT(0.285, "0.0%"))  # '28.5%'
print(TEXT(1234, "#,##0"))  # '1,234'
```

**Cost:** O(n), where n is the length of the formatted output.

**Note:** This is a simplified implementation. Full Excel TEXT function supports complex formatting codes.

---

### `VALUE()`

Converts text that represents a number to a number.

**Description:**
Converts a text string that represents a number to a numeric value. Handles integers, floats, percentages, and basic formatting.

**Parameters:**
- `text`: The text to convert to a number.

**Returns:**
- `Union[int, float]`: The numeric value.

**Example:**
```python
from formulite.fxExcel.text_formulas import VALUE

print(VALUE("$1,000"))  # 1000.0
print(VALUE("16:48:00"))  # 0.7
print(VALUE("123.45"))  # 123.45
```

**Cost:** O(n), where n is the length of the text.

**Note:** This is a simplified implementation. Full Excel VALUE function handles dates, times, and regional formats.

---

## Credits

FormuLite - fxExcel Module
Copyright (c) 2025 DatamanEdge

