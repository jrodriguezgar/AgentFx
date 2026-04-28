"""
Access Date and Time Functions Module.

Description
    Funciones de fecha y hora compatibles con VBA/Access.
"""

from datetime import datetime, date, time, timedelta

from shortfx.fxDate.date_operations import (
    add_months as _core_add_months,
    add_years as _core_add_years,
    month_name as _core_month_name,
    parts_to_date as _core_parts_to_date,
    parts_to_time as _core_parts_to_time,
    weekday_number as _core_weekday_number,
    date_part as _core_date_part,
    diff_time as _core_diff_time,
)
from shortfx.fxDate.date_sys import (
    current_datetime as _core_current_datetime,
    seconds_since_midnight as _core_seconds_since_midnight,
)

__all__ = [
    "Date_",
    "DateAdd",
    "DateDiff",
    "DatePart",
    "DateSerial",
    "Day",
    "Hour",
    "Minute",
    "Month",
    "MonthName",
    "Now",
    "Second",
    "Time_",
    "Timer",
    "TimeSerial",
    "WeekDay",
    "WeekDayName",
    "Year",
]


def Date_() -> date:
    """
    Description
        Retorna fecha actual del sistema.

    Returns
        date: Fecha actual.

    Usage Example
        >>> date_()
        datetime.date(2024, 1, 15)

    Cost
        O(1)
    """
    return datetime.now().date()


def DateAdd(interval: str, number: float, date_val: datetime) -> datetime:
    """
    Description
        Agrega intervalo de tiempo a una fecha.

    Args
        interval: Tipo de intervalo (yyyy, q, m, y, d, w, ww, h, n, s).
        number: Cantidad de intervalos a agregar.
        date_val: Fecha base.

    Returns
        datetime: Nueva fecha.

    Usage Example
        >>> dateadd("d", 5, datetime(2024, 1, 1))
        datetime.datetime(2024, 1, 6, 0, 0)

    Cost
        O(1)
    """
    if not isinstance(date_val, datetime):
        if isinstance(date_val, date):
            date_val = datetime.combine(date_val, time.min)

    if interval == "yyyy":
        return _core_add_years(date_val, int(number))
    elif interval == "q":
        return _core_add_months(date_val, int(number) * 3)
    elif interval == "m":
        return _core_add_months(date_val, int(number))
    elif interval in ("y", "d", "w"):
        return date_val + timedelta(days=int(number))
    elif interval == "ww":
        return date_val + timedelta(weeks=int(number))
    elif interval == "h":
        return date_val + timedelta(hours=number)
    elif interval == "n":
        return date_val + timedelta(minutes=number)
    elif interval == "s":
        return date_val + timedelta(seconds=number)
    else:
        raise ValueError(f"Intervalo inválido: {interval}")


def DateDiff(
    interval: str,
    date1: datetime,
    date2: datetime,
    first_day_of_week: int = 0,
    first_week_of_year: int = 0
) -> int:
    """
    Description
        Calcula diferencia entre dos fechas según intervalo.

    Args
        interval: Tipo de intervalo (yyyy, q, m, d, ww, h, n, s).
        date1: Fecha inicial.
        date2: Fecha final.
        first_day_of_week: Primer día de semana (0-7).
        first_week_of_year: Primera semana del año (0-3).

    Returns
        int: Diferencia en el intervalo especificado.

    Usage Example
        >>> datediff("d", datetime(2024, 1, 1), datetime(2024, 1, 10))
        9

    Cost
        O(1)
    """
    if not isinstance(date1, datetime):
        date1 = datetime.combine(date1, time.min)

    if not isinstance(date2, datetime):
        date2 = datetime.combine(date2, time.min)

    if interval == "yyyy":
        return date2.year - date1.year
    elif interval == "q":
        return ((date2.year - date1.year) * 4) + ((date2.month - 1) // 3 - (date1.month - 1) // 3)
    elif interval == "m":
        return (date2.year - date1.year) * 12 + (date2.month - date1.month)
    elif interval in ("y", "d"):
        return _core_diff_time(date1, date2, "days")
    elif interval == "ww":
        return _core_diff_time(date1, date2, "weeks")
    elif interval == "h":
        return _core_diff_time(date1, date2, "hours")
    elif interval == "n":
        return _core_diff_time(date1, date2, "minutes")
    elif interval == "s":
        return _core_diff_time(date1, date2, "seconds")
    else:
        raise ValueError(f"Intervalo inválido: {interval}")


def DatePart(
    interval: str,
    date_val: datetime,
    first_day_of_week: int = 0,
    first_week_of_year: int = 0
) -> int:
    """
    Description
        Extrae parte específica de una fecha.

    Args
        interval: Tipo de intervalo (yyyy, q, m, y, d, w, ww, h, n, s).
        date_val: Fecha a analizar.
        first_day_of_week: Primer día de semana.
        first_week_of_year: Primera semana del año.

    Returns
        int: Parte de fecha solicitada.

    Usage Example
        >>> datepart("m", datetime(2024, 6, 15))
        6

    Cost
        O(1)
    """
    return _core_date_part(interval, date_val, first_day_of_week, first_week_of_year)


def DateSerial(year: int, month: int, day: int) -> date:
    """
    Description
        Retorna fecha compuesta por año, mes y día indicados.

    Args
        year: Año.
        month: Mes.
        day: Día (0 = último día mes anterior).

    Returns
        date: Objeto fecha.

    Usage Example
        >>> dateserial(2024, 6, 15)
        datetime.date(2024, 6, 15)

    Cost
        O(1)
    """
    return _core_parts_to_date(year, month, day)


def Day(date_val: datetime) -> int:
    """
    Description
        Extrae día de una fecha.

    Args
        date_val: Fecha.

    Returns
        int: Número de día.

    Usage Example
        >>> day(datetime(2024, 6, 15))
        15

    Cost
        O(1)
    """
    if isinstance(date_val, datetime):
        return date_val.day
    return date_val.day


def Hour(time_val: datetime) -> int:
    """
    Description
        Retorna hora de una expresión DateTime.

    Args
        time_val: Valor de fecha/hora.

    Returns
        int: Hora (0-23).

    Usage Example
        >>> hour(datetime(2024, 1, 1, 14, 30))
        14

    Cost
        O(1)
    """
    return time_val.hour


def Minute(time_val: datetime) -> int:
    """
    Description
        Retorna minutos de una expresión de tiempo.

    Args
        time_val: Valor de fecha/hora.

    Returns
        int: Minutos (0-59).

    Usage Example
        >>> minute(datetime(2024, 1, 1, 14, 30))
        30

    Cost
        O(1)
    """
    return time_val.minute


def Month(date_val: datetime) -> int:
    """
    Description
        Retorna número de mes de una fecha.

    Args
        date_val: Fecha.

    Returns
        int: Mes (1-12).

    Usage Example
        >>> month(datetime(2024, 6, 15))
        6

    Cost
        O(1)
    """
    if isinstance(date_val, datetime):
        return date_val.month
    return date_val.month


def MonthName(month_num: int, abbreviate: bool = False) -> str:
    """
    Description
        Retorna nombre de mes.

    Args
        month_num: Número de mes (1-12).
        abbreviate: Si True, retorna abreviatura.

    Returns
        str: Nombre del mes.

    Usage Example
        >>> monthname(1)
        'January'
        >>> monthname(1, True)
        'Jan'

    Cost
        O(1)
    """
    from datetime import datetime as _dt
    ref = _dt(2000, month_num, 1)
    return _core_month_name(ref, language='en')[:3] if abbreviate else _core_month_name(ref, language='en')


def Now() -> datetime:
    """
    Description
        Retorna fecha y hora actuales del sistema.

    Returns
        datetime: Fecha y hora actuales.

    Usage Example
        >>> now()
        datetime.datetime(2024, 1, 15, 14, 30, 0)

    Cost
        O(1)
    """
    return _core_current_datetime()


def Second(time_val: datetime) -> int:
    """
    Description
        Retorna segundos de una expresión de tiempo.

    Args
        time_val: Valor de fecha/hora.

    Returns
        int: Segundos (0-59).

    Usage Example
        >>> second(datetime(2024, 1, 1, 14, 30, 45))
        45

    Cost
        O(1)
    """
    return time_val.second


def Time_() -> time:
    """
    Description
        Retorna hora actual del sistema.

    Returns
        time: Hora actual.

    Usage Example
        >>> time_()
        datetime.time(14, 30, 0)

    Cost
        O(1)
    """
    return datetime.now().time()


def Timer() -> float:
    """
    Description
        Retorna número de segundos transcurridos desde medianoche.

    Returns
        float: Segundos desde medianoche.

    Usage Example
        >>> timer()
        52200.5

    Cost
        O(1)
    """
    return _core_seconds_since_midnight()


def TimeSerial(hour: int, minute: int, second: int) -> time:
    """
    Description
        Retorna valor tipo Time pasando hora, minutos y segundos.

    Args
        hour: Hora.
        minute: Minutos.
        second: Segundos.

    Returns
        time: Objeto hora.

    Usage Example
        >>> timeserial(14, 30, 0)
        datetime.time(14, 30)

    Cost
        O(1)
    """
    return _core_parts_to_time(hour, minute, second)


def WeekDay(date_val: datetime, first_day_of_week: int = 1) -> int:
    """
    Description
        Retorna número indicando día de la semana.

    Args
        date_val: Fecha.
        first_day_of_week: Primer día semana (0-7).

    Returns
        int: Día de semana (1=domingo, 2=lunes, ...).

    Usage Example
        >>> weekday(datetime(2024, 1, 1))
        2

    Cost
        O(1)
    """
    return _core_weekday_number(date_val, start_day='anglo') + 1


def WeekDayName(
    weekday_num: int,
    abbreviate: bool = False,
    first_day_of_week: int = 1
) -> str:
    """
    Description
        Retorna día de semana como cadena.

    Args
        weekday_num: Número de día (1-7).
        abbreviate: Si True, retorna abreviatura.
        first_day_of_week: Primer día semana.

    Returns
        str: Nombre del día.

    Usage Example
        >>> weekdayname(1)
        'Sunday'
        >>> weekdayname(2, True)
        'Mon'

    Cost
        O(1)
    """
    days_full = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days_abbr = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    if not 1 <= weekday_num <= 7:
        raise ValueError("Día debe estar entre 1 y 7")
    
    if abbreviate:
        return days_abbr[weekday_num - 1]
    return days_full[weekday_num - 1]


def Year(date_val: datetime) -> int:
    """
    Description
        Retorna año de una fecha.

    Args
        date_val: Fecha.

    Returns
        int: Año.

    Usage Example
        >>> year(datetime(2024, 6, 15))
        2024

    Cost
        O(1)
    """
    if isinstance(date_val, datetime):
        return date_val.year
    return date_val.year


