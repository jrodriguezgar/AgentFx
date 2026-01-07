"""
Access Date and Time Functions Module.

Description
    Funciones de fecha y hora compatibles con VBA/Access.
"""

from datetime import datetime, date, time, timedelta
from typing import Optional

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
        return date_val.replace(year=date_val.year + int(number))
    elif interval == "q":
        return date_val + timedelta(days=int(number * 91.25))
    elif interval == "m":
        month = date_val.month + int(number)
        year = date_val.year + (month - 1) // 12
        month = ((month - 1) % 12) + 1
        return date_val.replace(year=year, month=month)
    elif interval in ("y", "d"):
        return date_val + timedelta(days=int(number))
    elif interval == "w":
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
    
    delta = date2 - date1
    
    if interval == "yyyy":
        return date2.year - date1.year
    elif interval == "q":
        return ((date2.year - date1.year) * 4) + ((date2.month - 1) // 3 - (date1.month - 1) // 3)
    elif interval == "m":
        return (date2.year - date1.year) * 12 + (date2.month - date1.month)
    elif interval in ("y", "d"):
        return delta.days
    elif interval == "ww":
        return delta.days // 7
    elif interval == "h":
        return int(delta.total_seconds() // 3600)
    elif interval == "n":
        return int(delta.total_seconds() // 60)
    elif interval == "s":
        return int(delta.total_seconds())
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
    if not isinstance(date_val, datetime):
        date_val = datetime.combine(date_val, time.min)
    
    if interval == "yyyy":
        return date_val.year
    elif interval == "q":
        return (date_val.month - 1) // 3 + 1
    elif interval == "m":
        return date_val.month
    elif interval == "y":
        return date_val.timetuple().tm_yday
    elif interval == "d":
        return date_val.day
    elif interval == "w":
        return date_val.isoweekday() % 7 + 1
    elif interval == "ww":
        return date_val.isocalendar()[1]
    elif interval == "h":
        return date_val.hour
    elif interval == "n":
        return date_val.minute
    elif interval == "s":
        return date_val.second
    else:
        raise ValueError(f"Intervalo inválido: {interval}")


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
    if day == 0:
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
        day = (date(year, month + 1, 1) - timedelta(days=1)).day if month < 12 else 31
    
    return date(year, month, day)


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
    months_full = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    months_abbr = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    
    if not 1 <= month_num <= 12:
        raise ValueError("Mes debe estar entre 1 y 12")
    
    if abbreviate:
        return months_abbr[month_num - 1]
    return months_full[month_num - 1]


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
    return datetime.now()


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
    now = datetime.now()
    midnight = datetime.combine(now.date(), time.min)
    return (now - midnight).total_seconds()


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
    return time(hour % 24, minute % 60, second % 60)


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
    if isinstance(date_val, datetime):
        day_num = date_val.isoweekday()
    else:
        day_num = date_val.isoweekday()
    
    return (day_num % 7) + 1


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
