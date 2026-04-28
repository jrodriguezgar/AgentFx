"""
Date Operations Module.

This module provides comprehensive date and time manipulation utilities for
Python applications. It includes functions for date validation, calculations,
conversions, and formatting operations.

Key Features:
    - Date validation and type checking
    - Weekday and month operations with locale support
    - Date arithmetic (adding/subtracting time units)
    - Business day calculations
    - Quarter and season operations
    - Random date/time generation
    - Date range operations and intervals

Dependencies:
    - datetime: Core date/time functionality
    - calendar: Calendar-related operations
    - locale: Internationalization support
    - zoneinfo: Timezone support (Python 3.9+)

Example:
    >>> from datetime import datetime
    >>> from date_operations import is_valid_date, add_time_to_date
    >>> is_valid_date("2025-01-15")
    True
    >>> add_time_to_date(datetime(2025, 1, 15), 30, 'days')
    datetime.datetime(2025, 2, 14, 0, 0)
"""

from datetime import date, time, datetime, timedelta, timezone
from typing import Union,Literal,List, Tuple, Optional, Set, Dict, Any
import calendar
import locale
import random
import zoneinfo # Requires Python 3.9+ for ZoneInfo
import math

try:
    from shortfx.fxString.string_convertions import string_to_date, string_to_datetime
except ImportError:
    from .date_convertions import datetime_to_date as string_to_date  # type: ignore[assignment]
    string_to_datetime = None  # type: ignore[assignment]


def is_date_type(value: Any) -> bool:
    """Checks if an object is a date/time type (date, datetime, or time).
    
    Description:
        Verifies if a value is one of Python's date/time types before
        performing operations, preventing type errors.
    
    Args:
        value (Any): The value to check.
    
    Returns:
        bool: True if value is date, datetime, or time; False otherwise.
    
    Usage Example:
        >>> from datetime import date, datetime, time
        >>> from shortfx.fxDate.date_operations import is_date_type
        >>> is_date_type(datetime(2026, 1, 3))
        True
        >>> is_date_type(date(2026, 1, 3))
        True
        >>> is_date_type(time(10, 30, 0))
        True
        >>> is_date_type("2026-01-03")
        False
        >>> is_date_type(None)
        False
    
    Cost: O(1)
    """
    return isinstance(value, (date, datetime, time))


def is_valid_date(date_input: Any, date_format: str = "%Y-%m-%d") -> bool:
    """Validates if input is a valid date (datetime object or parseable string).
    
    Description:
        Checks whether the input is a valid date. Accepts datetime objects
        or strings that can be parsed with the specified format. Ensures
        inputs represent actual dates before use in date operations.
    
    Args:
        date_input (Any): The parameter to validate (datetime object or string).
        date_format (str): Expected format if date_input is a string.
                          Defaults to "%Y-%m-%d".
    
    Returns:
        bool: True if date_input is valid date, False otherwise.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxDate.date_operations import is_valid_date
        >>> is_valid_date(datetime(2026, 1, 3))
        True
        >>> is_valid_date("2026-01-03")
        True
        >>> is_valid_date("03/01/2026", "%d/%m/%Y")
        True
        >>> is_valid_date("2026-13-01")  # Invalid month
        False
        >>> is_valid_date("not-a-date")
        False
    
    Cost: O(1)
    """
    # If the input is already a date or datetime object, it's valid.
    if is_date_type(date_input):
        return True

    # If the input is a string, attempt to parse it into a datetime object.
    # A ValueError will be raised if the string does not match the format
    # or if it represents an invalid date (e.g., February 30th).
    if isinstance(date_input, str):
        try:
            datetime.strptime(date_input, date_format)
            return True
        except ValueError:
            # Catching ValueError allows us to gracefully handle strings that
            # are not valid dates according to the specified format.
            return False

    # If the input is neither a date type nor a string, it's not a valid date.
    return False


def weekday_number(date_input: datetime, start_day: str = 'european') -> int:
    """
    Retrieves the day of the week as a number for a given date, supporting
    both European (Monday=0) and US (Sunday=0) conventions.

    This function leverages the `datetime.weekday()` method, which by default
    returns Monday as 0 and Sunday as 6. It then adjusts this value if the
    'anglo' convention is specified to ensure Sunday is 0.

    Args:
        date_input (datetime): The date for which to get the weekday number.
        start_day (str): Specifies the starting day convention.
                         Accepted values are 'european' (Monday=0) or 'anglo' (Sunday=0).
                         Defaults to 'european'.

    Returns:
        int: The day of the week as an integer (e.g., 0 for Monday in 'european',
             0 for Sunday in 'anglo').

    Raises:
        TypeError: If 'date_input' is not a datetime object.
        ValueError: If 'start_day' is not 'european' or 'anglo'.

    Example:
        >>> from datetime import datetime
        >>> date_to_check_thursday = datetime(2023, 10, 26) # A Thursday
        >>> weekday_number(date_to_check_thursday, start_day='european')
        3
        >>> weekday_number(date_to_check_thursday, start_day='anglo')
        4
        >>> date_to_check_sunday = datetime(2023, 10, 29) # A Sunday
        >>> weekday_number(date_to_check_sunday, start_day='european')
        6
        >>> weekday_number(date_to_check_sunday, start_day='anglo')
        0

    **Cost:** O(1), constant time for date arithmetic operations.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    if start_day not in ['european', 'anglo']:
        raise ValueError("Invalid value for 'start_day'. Must be 'european' or 'anglo'.")

    # .weekday() returns Monday=0, ..., Sunday=6. This is the European standard.
    weekday_index = date_input.weekday()

    # Adjust for US convention if requested: Sunday=0, ..., Saturday=6
    if start_day == 'anglo':
        # Shift the index so that Sunday (originally 6) becomes 0,
        # Monday (originally 0) becomes 1, and so on.
        return (weekday_index + 1) % 7
    return weekday_index


def weekday_name(date_input: datetime, language: str = 'en') -> str:
    """Gets the name of the day of the week for a given date in the specified language.

    This function leverages your operating system's installed locales to provide
    weekday names in various languages. The availability of a specific language (locale)
    depends entirely on what is configured and installed on your operating system.
    For example, 'es' for Spanish, 'fr' for French, 'de' for German, etc.

    Args:
        date_input (datetime): The datetime object for which to get the weekday name.
        language (str, optional): The two-letter ISO 639-1 language code (e.g., 'en', 'es', 'fr', 'de').
                                  Defaults to 'en'.

    Returns:
        str: The full name of the day of the week (e.g., 'Thursday', 'Jueves', 'Donnerstag').
             Note: Capitalization might vary based on the specific locale installed on your system.

    Raises:
        TypeError: If 'date_input' is not a datetime object.
        ValueError: If the specified 'language' cannot be set as a locale on your system.
                    This usually means the corresponding language pack is not installed or
                    the locale name is not recognized by your OS.

    Example:
        >>> from datetime import datetime
        >>> date_to_check = datetime(2023, 10, 26) # A Thursday

        >>> # Example for English (always available)
        >>> weekday_name(date_to_check, 'en')
        'Thursday'

        >>> # Example for Spanish (requires 'es' or 'es_ES.UTF-8' locale installed on your system)
        >>> try:
        >>>     weekday_name(date_to_check, 'es')
        >>> except ValueError as e:
        >>>     print(f"Could not get Spanish weekday name: {e}")
        # Expected output (if locale installed): 'jueves' or 'Jueves'

        >>> # Example for German (requires 'de' or 'de_DE.UTF-8' locale installed on your system)
        >>> try:
        >>>     weekday_name(date_to_check, 'de')
        >>> except ValueError as e:
        >>>     print(f"Could not get German weekday name: {e}")
        # Expected output (if locale installed): 'Donnerstag'

    **Cost:** O(1), constant time for locale operations and string formatting.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Store the current locale settings to restore them later, preventing side effects.
    original_locale = locale.getlocale(locale.LC_TIME)

    try:
        # Attempt to set the locale based on the provided language code.
        # Python's setlocale is quite flexible; it often tries common variations
        # like 'en_US.UTF-8' if just 'en' is provided, depending on the OS.
        locale.setlocale(locale.LC_TIME, language + '.UTF-8')
    except locale.Error:
        # Fallback: try setting without the .UTF-8 suffix.
        try:
            locale.setlocale(locale.LC_TIME, language)
        except locale.Error:
            # If both attempts fail, raise a ValueError, explaining the dependency on system locales.
            raise ValueError(
                f"Unable to set locale for language '{language}'. "
                "This typically means the required language pack is not installed on your operating system, "
                "or the locale name is different. "
                "On Linux/macOS, you can check available locales using 'locale -a'. "
                "On Windows, locales are managed via 'Control Panel -> Region'."
            )

    try:
        # Use strftime with the '%A' format code to get the full weekday name
        # in the currently active locale.
        weekday_name = date_input.strftime('%A')
        return weekday_name
    finally:
        # Crucially, always restore the original locale to ensure other parts
        # of your program or other functions using locale behave as expected.
        locale.setlocale(locale.LC_TIME, original_locale)


def first_day_of_week(date_input: Union[datetime, str], week_start_day: int = 0) -> datetime:
    """Calculates the first day of the week for a given date, allowing customization of the week's starting day.

    Problema/Necesidad del Usuario: Es necesario encontrar el primer día de la semana
    para una fecha dada, donde la definición de "primer día" puede variar (ej. Lunes o Domingo).
    Esto es común en calendarios, informes y agregación de datos.

    Objetivos del Producto: Proporcionar una función flexible que permita al usuario
    especificar el día que se considera el inicio de la semana, facilitando
    cálculos y visualizaciones consistentes con diferentes convenciones.

    Descripción: Dada una fecha y un día de inicio de semana (por defecto Lunes),
    esta función devuelve un objeto `datetime` que representa el primer día de la
    semana que contiene la fecha dada. El día de inicio de semana se especifica
    como un entero (0=Lunes, 1=Martes, ..., 6=Domingo). La fecha devuelta tendrá
    su componente de tiempo establecido a medianoche (00:00:00).

    Args:
        date_input (Union[datetime, str]): La fecha para la cual se desea encontrar
                                            el primer día de la semana. Puede ser un
                                            objeto `datetime` o una cadena de fecha.
        week_start_day (int, optional): Un entero que representa el día que se
                                         considera el inicio de la semana (0=Lunes,
                                         1=Martes, ..., 6=Domingo). Por defecto es 0 (Lunes).

    Returns:
        datetime: Un objeto `datetime` que representa el primer día de la semana
                  que contiene la fecha dada, con la hora fijada a medianoche.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o una cadena,
                   o si 'week_start_day' no es un entero.
        ValueError: Si 'week_start_day' no está entre 0 y 6,
                    o si la cadena de fecha no puede ser parseada.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Obtener el primer día de la semana (Lunes por defecto) para el 15 de junio de 2025 (Domingo)
        >>> first_day_of_week(datetime(2025, 6, 15))
        datetime.datetime(2025, 6, 9, 0, 0) # El lunes de esa semana es el 9 de junio

        >>> # Ejemplo 2: Obtener el primer día de la semana (Domingo) para el 15 de junio de 2025
        >>> first_day_of_week(datetime(2025, 6, 15), week_start_day=6)
        datetime.datetime(2025, 6, 15, 0, 0) # El domingo de esa semana es el 15 de junio

        >>> # Ejemplo 3: Usando una cadena de fecha
        >>> first_day_of_week("2025-06-15", week_start_day=0)
        datetime.datetime(2025, 6, 9, 0, 0)

        >>> # Ejemplo 4: Día de inicio de semana inválido (levantará ValueError)
        >>> try:
        >>>     first_day_of_week(datetime(2025, 6, 15), week_start_day=7)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: week_start_day must be between 0 (Monday) and 6 (Sunday).

    **Cost:** O(1), constant time for date arithmetic operations.
    """
    # Función auxiliar interna para parsear la entrada de fecha (datetime o string)
    def _parse_date_input_internal(date_val: Union[datetime, str]) -> datetime:
        if isinstance(date_val, str):
            # Asumimos que si la fecha es una cadena, el formato ya se conoce
            # y no se necesita un argumento input_format. Si se necesitara,
            # se agregaría como en otros ejemplos.
            return datetime.fromisoformat(date_val)
        elif isinstance(date_val, datetime):
            return date_val
        else:
            raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # 1. Validación de entradas
    if not isinstance(week_start_day, int):
        raise TypeError("Input 'week_start_day' must be an integer.")
    if not (0 <= week_start_day <= 6):
        raise ValueError("week_start_day must be between 0 (Monday) and 6 (Sunday).")

    # 2. Parsear la fecha de entrada
    parsed_date = _parse_date_input_internal(date_input)

    # 3. Calcular el primer día de la semana
    # `parsed_date.weekday()` devuelve un entero donde 0 es Lunes y 6 es Domingo.
    # Necesitamos encontrar la diferencia entre el día actual y el día de inicio de la semana.
    # Si el día actual es anterior al día de inicio de semana, necesitamos "retroceder"
    # hasta el día de inicio de la semana de la semana anterior.
    days_since_week_start = (parsed_date.weekday() - week_start_day) % 7
    first_day = parsed_date - timedelta(days=days_since_week_start)

    # 4. Devolver la fecha con la hora a medianoche
    return first_day.replace(hour=0, minute=0, second=0, microsecond=0)


def last_day_of_week(date_input: Union[datetime, str], week_start_day: int = 0) -> datetime:
    """Calcula el último día de la semana para una fecha dada, permitiendo la personalización del día de inicio de la semana.

    Problema/Necesidad del Usuario: Es necesario encontrar el último día de la semana
    para una fecha específica, lo que es útil para cerrar períodos de informe,
    definir agregaciones semanales o completar ciclos de tareas.

    Objetivos del Producto: Proporcionar una función flexible que determine el día
    final de la semana para cualquier fecha, adaptándose a diversas convenciones
    de calendario mediante la especificación del día de inicio de semana.

    Descripción: Dada una fecha y un día de inicio de semana (por defecto Lunes),
    esta función devuelve un objeto `datetime` que representa el último día de la
    semana que contiene la fecha dada. El día de inicio de semana se especifica
    como un entero (0=Lunes, 1=Martes, ..., 6=Domingo). La fecha devuelta tendrá
    su componente de tiempo establecido a las 23:59:59.999999 (final del día).

    Args:
        date_input (Union[datetime, str]): La fecha para la cual se desea encontrar
                                            el último día de la semana. Puede ser un
                                            objeto `datetime` o una cadena de fecha.
        week_start_day (int, optional): Un entero que representa el día que se
                                         considera el inicio de la semana (0=Lunes,
                                         1=Martes, ..., 6=Domingo). Por defecto es 0 (Lunes).

    Returns:
        datetime: Un objeto `datetime` que representa el último día de la semana
                  que contiene la fecha dada, con la hora fijada al final del día.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o una cadena,
                   o si 'week_start_day' no es un entero.
        ValueError: Si 'week_start_day' no está entre 0 y 6,
                    o si la cadena de fecha no puede ser parseada.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Obtener el último día de la semana (Lunes como inicio) para el 11 de junio de 2025 (Miércoles)
        >>> last_day_of_week(datetime(2025, 6, 11))
        datetime.datetime(2025, 6, 15, 23, 59, 59, 999999) # El domingo de esa semana es el 15 de junio

        >>> # Ejemplo 2: Obtener el último día de la semana (Domingo como inicio) para el 15 de junio de 2025 (Domingo)
        >>> last_day_of_week(datetime(2025, 6, 15), week_start_day=6)
        datetime.datetime(2025, 6, 21, 23, 59, 59, 999999) # El sábado de esa semana es el 21 de junio

        >>> # Ejemplo 3: Usando una cadena de fecha
        >>> last_day_of_week("2025-06-11", week_start_day=0)
        datetime.datetime(2025, 6, 15, 23, 59, 59, 999999)

        >>> # Ejemplo 4: Día de inicio de semana inválido (levantará ValueError)
        >>> try:
        >>>     last_day_of_week(datetime(2025, 6, 11), week_start_day=8)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: week_start_day must be between 0 (Monday) and 6 (Sunday).

    **Cost:** O(1), constant time for date arithmetic operations.
    """
    # Función auxiliar interna para parsear la entrada de fecha (reutilizada de first_day_of_week)
    def _parse_date_input_internal(date_val: Union[datetime, str]) -> datetime:
        if isinstance(date_val, str):
            # Usamos fromisoformat para cadenas, ya que es un formato común y estricto.
            # Si se necesitaran otros formatos, se debería pasar 'input_format' como en `date_intervals`.
            try:
                return datetime.fromisoformat(date_val)
            except ValueError as e:
                raise ValueError(f"Could not parse date string '{date_val}'. Ensure it's in ISO format (YYYY-MM-DDTHH:MM:SS) or pass an 'input_format' if supported by a wrapper. Error: {e}") from e
        elif isinstance(date_val, datetime):
            return date_val
        else:
            raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # 1. Validación de entradas
    if not isinstance(week_start_day, int):
        raise TypeError("Input 'week_start_day' must be an integer.")
    if not (0 <= week_start_day <= 6):
        raise ValueError("week_start_day must be between 0 (Monday) and 6 (Sunday).")

    # 2. Parsear la fecha de entrada
    parsed_date = _parse_date_input_internal(date_input)

    # 3. Calcular el primer día de la semana
    # `parsed_date.weekday()` devuelve un entero donde 0 es Lunes y 6 es Domingo.
    # Se calcula cuántos días han pasado desde el inicio de la semana hasta la fecha dada.
    days_since_week_start = (parsed_date.weekday() - week_start_day) % 7
    first_day_of_current_week = parsed_date - timedelta(days=days_since_week_start)

    # 4. Sumar 6 días para obtener el último día de la semana
    # El primer día de la semana + 6 días = el último día de la semana.
    last_day_of_week = first_day_of_current_week + timedelta(days=6)

    # 5. Devolver la fecha con la hora fijada al final del día
    return last_day_of_week.replace(hour=23, minute=59, second=59, microsecond=999999)


def month_name(date_input: datetime, language: str = 'en') -> str:
    """Gets the name of the month for a given date in the specified language.

    This function leverages your operating system's installed locales to provide
    month names in various languages. The availability of a specific language (locale)
    depends entirely on what is configured and installed on your operating system.
    For example, 'es' for Spanish, 'fr' for French, 'de' for German, etc.

    Args:
        date_input (datetime): The datetime object for which to get the month name.
        language (str, optional): The two-letter ISO 639-1 language code (e.g., 'en', 'es', 'fr', 'de').
                                  Defaults to 'en'.

    Returns:
        str: The full name of the month (e.g., 'October', 'Octubre', 'Oktober', 'Oktober').
             Note: Capitalization might vary based on the specific locale installed on your system.

    Raises:
        TypeError: If 'date_input' is not a datetime object.
        ValueError: If the specified 'language' cannot be set as a locale on your system.
                    This usually means the corresponding language pack is not installed or
                    the locale name is not recognized by your OS.

    Example:
        >>> from datetime import datetime
        >>> # Example for English (always available)
        >>> month_name(datetime(2023, 10, 26), 'en')
        'October'

        >>> # Example for Spanish (requires 'es' or 'es_ES.UTF-8' locale installed on your system)
        >>> try:
        >>>     month_name(datetime(2023, 10, 26), 'es')
        >>> except ValueError as e:
        >>>     print(f"Could not get Spanish month name: {e}")
        # Expected output (if locale installed): 'octubre' or 'Octubre'

        >>> # Example for German (requires 'de' or 'de_DE.UTF-8' locale installed on your system)
        >>> try:
        >>>     month_name(datetime(2023, 10, 26), 'de')
        >>> except ValueError as e:
        >>>     print(f"Could not get German month name: {e}")
        # Expected output (if locale installed): 'Oktober'

    **Cost:** O(1), constant time for locale operations and string formatting.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Store the current locale settings to restore them later, preventing side effects.
    # locale.LC_TIME specifies that we're interested in time-related locale settings.
    original_locale = locale.getlocale(locale.LC_TIME)

    try:
        # Attempt to set the locale based on the provided language code.
        # Python's setlocale is quite flexible; it often tries common variations
        # like 'en_US.UTF-8' if just 'en' is provided, depending on the OS.
        locale.setlocale(locale.LC_TIME, language + '.UTF-8')
    except locale.Error:
        # Fallback: try setting without the .UTF-8 suffix.
        # This can be necessary on some systems or for older configurations.
        try:
            locale.setlocale(locale.LC_TIME, language)
        except locale.Error:
            # If both attempts fail, raise a ValueError, explaining the dependency on system locales.
            raise ValueError(
                f"Unable to set locale for language '{language}'. "
                "This typically means the required language pack is not installed on your operating system, "
                "or the locale name is different. "
                "On Linux/macOS, you can check available locales using 'locale -a'. "
                "On Windows, locales are managed via 'Control Panel -> Region'."
            )

    try:
        # Use strftime with the '%B' format code to get the full month name
        # in the currently active locale.
        month_name = date_input.strftime('%B')
        return month_name
    finally:
        # Crucially, always restore the original locale to ensure other parts
        # of your program or other functions using locale behave as expected.
        locale.setlocale(locale.LC_TIME, original_locale)


def months_between_dates(start_date: datetime, end_date: datetime) -> int:
    """Calcula el número de meses completos transcurridos entre dos fechas.

    Problema/Necesidad del Usuario: Es necesario obtener el número de meses entre dos
    fechas para cálculos de antigüedad, proyecciones financieras o la duración de proyectos,
    requiriendo un manejo preciso de los límites de mes.

    Objetivos del Producto: Proporcionar una función fiable para cuantificar la duración
    en términos de meses completos entre dos puntos en el tiempo.

    Descripción: Esta función toma dos objetos `datetime`, una fecha de inicio y una
    fecha de fin. Calcula la diferencia en meses enteros entre ellas.
    Por ejemplo, del 15 de enero al 14 de febrero es 0 meses. Del 15 de enero al 15 de febrero es 1 mes.
    La función maneja correctamente el orden de las fechas: si `start_date` es posterior
    a `end_date`, el resultado será un número negativo.

    Args:
        start_date (datetime): La fecha de inicio.
        end_date (datetime): La fecha de fin.

    Returns:
        int: El número de meses completos entre `start_date` y `end_date`.
             Será positivo si `end_date` es posterior a `start_date`,
             negativo si `end_date` es anterior, y cero si son el mismo mes o
             si no se ha cumplido un mes completo.

    Raises:
        TypeError: Si `start_date` o `end_date` no son objetos `datetime`.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: 0 meses (mismo mes)
        >>> months_between_dates(datetime(2023, 1, 10), datetime(2023, 1, 25))
        0

        >>> # Ejemplo 2: 1 mes (del 10 de enero al 10 de febrero)
        >>> months_between_dates(datetime(2023, 1, 10), datetime(2023, 2, 10))
        1

        >>> # Ejemplo 3: Más de un mes (del 10 de enero al 9 de marzo)
        >>> months_between_dates(datetime(2023, 1, 10), datetime(2023, 3, 9))
        1

        >>> # Ejemplo 4: Múltiples meses completos
        >>> months_between_dates(datetime(2023, 1, 1), datetime(2023, 7, 31))
        6

        >>> # Ejemplo 5: Orden invertido (resultado negativo)
        >>> months_between_dates(datetime(2023, 5, 1), datetime(2023, 2, 1))
        -3

        >>> # Ejemplo 6: Con horas y minutos (no afectan el cálculo de meses completos)
        >>> months_between_dates(datetime(2023, 1, 31, 23, 59, 59), datetime(2023, 3, 1, 0, 0, 0))
        1 # De enero 31 a marzo 1, solo se ha completado febrero.

        >>> # Ejemplo 7: Tipos de datos incorrectos
        >>> try:
        >>>     months_between_dates("2023-01-01", datetime(2023, 2, 1))
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: start_date and end_date must be datetime objects.

    **Cost:** O(1), constant time for date arithmetic and month calculation.
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    # Asegurarse de que start_date sea siempre la fecha inicial para el cálculo.
    # Si end_date es anterior a start_date, se invertirá el signo al final.
    reverse_order = False
    if start_date > end_date:
        start_date, end_date = end_date, start_date
        reverse_order = True

    # Calcular la diferencia de años y meses directamente
    # Consideramos el día del mes para determinar si un mes completo ha transcurrido.
    years_diff = end_date.year - start_date.year
    months_diff = end_date.month - start_date.month

    total_months = (years_diff * 12) + months_diff

    # Ajustar si el día del mes de end_date es anterior al día de start_date.
    # Por ejemplo, del 15 de enero al 14 de febrero no es un mes completo.
    # Se resta 1 si el día del mes actual es anterior al día de inicio,
    # siempre y cuando no estemos en el mismo mes.
    if end_date.day < start_date.day:
        total_months -= 1
    
    # Si las fechas están en el mismo mes y el día de fin es anterior al día de inicio,
    # el resultado debe ser 0, no -1. Ej: 15 de enero a 10 de enero.
    # La lógica de `reverse_order` ya lo manejará correctamente.
    # Si `start_date > end_date` al inicio (ej. 2023-05-15 a 2023-05-10),
    # se invierten a `start_date=2023-05-10`, `end_date=2023-05-15`.
    # `total_months` sería 0. `end_date.day < start_date.day` sería False. Correcto.

    return -total_months if reverse_order else total_months


def days_in_month(year: int, month: int) -> int:
    """Returns the number of days in a given month and year.

    Problem/User Need: When building calendars or validating date ranges (e.g.,
    user input in a date form), it's crucial to know how many days a specific
    month has, as it varies (28, 29, 30, 31).

    Product Goals: Provide a robust utility for validation and building calendar UIs,
    avoiding errors like "February 31st".

    Description: Given a year and a month (as integers), this function returns
    the total number of days in that specific month, correctly handling leap years
    for February.

    Args:
        year (int): The year (e.g., 2023, 2024).
        month (int): The month (1 for January, 12 for December).

    Returns:
        int: The number of days in the specified month of the given year.

    Raises:
        TypeError: If 'year' or 'month' are not integers.
        ValueError: If 'month' is not between 1 and 12, or if 'year' is less than 1.

    Example:
        >>> days_in_month(2023, 2) # February 2023 (not a leap year)
        28
        >>> days_in_month(2024, 2) # February 2024 (a leap year)
        29
        >>> days_in_month(2023, 1) # January
        31
        >>> days_in_month(2023, 4) # April
        30

    **Cost:** O(1), constant time for calendar lookup.
    """
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if not isinstance(month, int):
        raise TypeError("Input 'month' must be an integer.")

    if not (1 <= month <= 12):
        raise ValueError("Input 'month' must be between 1 and 12.")
    if year < 1:
        raise ValueError("Input 'year' must be a positive integer.")

    # calendar.monthrange(year, month) returns a tuple:
    # (weekday of the first day of the month, number of days in the month).
    # We are interested in the second element (number of days).
    _, num_days = calendar.monthrange(year, month)
    return num_days


def calculate_days_between_dates(start_date: datetime.date, end_date: datetime.date) -> int:
    """
    Calculates the number of days between two dates.

    This function takes two date objects and returns the absolute difference
    in days between them. The order of the dates does not matter.

    Args:
        start_date (datetime.date): The first date.
        end_date (datetime.date): The second date.

    Returns:
        int: The number of days between the two dates.

    Raises:
        TypeError: If either start_date or end_date are not datetime.date objects.

    Example of use:
        >>> from datetime import date
        >>> date1 = date(2023, 1, 1)
        >>> date2 = date(2023, 1, 31)
        >>> calculate_days_between_dates(date1, date2)
        30

    **Cost:** O(1), constant time for date arithmetic.
    """
    if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
        raise TypeError("Both start_date and end_date must be datetime.date objects.")

    # Calculate the difference between the two dates.
    # The result is a timedelta object.
    time_difference = end_date - start_date

    # Access the 'days' attribute of the timedelta object.
    # We use abs() to ensure a positive number of days, regardless of date order.
    number_of_days = abs(time_difference.days)

    return number_of_days


def get_nth_weekday_of_month(year: int, month: int, weekday: int, n: int) -> Optional[datetime]:
    """Calculates the date of the n-th occurrence of a specific weekday in a given month.

    Problema/Necesidad del Usuario: A veces, se necesita encontrar una fecha muy específica
    como "el tercer martes de cada mes" o "el primer lunes del trimestre". Esto es común
    en programaciones recurrentes o plazos específicos.

    Objetivos del Producto: Proporcionar una función de cálculo de fechas recurrente que
    es sorprendentemente compleja de implementar manualmente y propensa a errores.

    Descripción: Dada un año, un mes, un día de la semana (donde 0=Lunes, 6=Domingo)
    y un número 'n' (por ejemplo, 1 para el primero, 2 para el segundo), esta función
    devuelve la fecha de la n-ésima ocurrencia de ese día de la semana en el mes.
    Si la n-ésima ocurrencia no existe dentro de ese mes (por ejemplo, pedir el quinto
    viernes en un mes que solo tiene cuatro), devuelve `None`.

    Args:
        year (int): El año (ej., 2025).
        month (int): El mes (1-12, ej., 6 para junio).
        weekday (int): El día de la semana (0=Lunes, 1=Martes, ..., 6=Domingo).
        n (int): El número de ocurrencia (ej., 1 para la primera, 2 para la segunda, etc.).
                 Debe ser un entero positivo.

    Returns:
        Optional[datetime]: Un objeto `datetime` representando la fecha calculada
                            (con la hora fijada a medianoche 00:00:00), o `None`
                            si la n-ésima ocurrencia no existe en el mes.

    Raises:
        TypeError: Si 'year', 'month', 'weekday' o 'n' no son enteros.
        ValueError: Si 'year' está fuera del rango válido (1-9999), 'month' no
                    está entre 1-12, 'weekday' no está entre 0-6, o 'n' no es
                    un entero positivo.

    Example:
        >>> # Obtener el segundo martes (weekday 1) de junio de 2025
        >>> get_nth_weekday_of_month(2025, 6, 1, 2)
        datetime.datetime(2025, 6, 10, 0, 0)

        >>> # Obtener el primer lunes (weekday 0) de enero de 2024
        >>> get_nth_weekday_of_month(2024, 1, 0, 1)
        datetime.datetime(2024, 1, 1, 0, 0)

        >>> # Obtener el último (cuarto) jueves (weekday 3) de febrero de 2024 (año bisiesto)
        >>> get_nth_weekday_of_month(2024, 2, 3, 4)
        datetime.datetime(2024, 2, 29, 0, 0)

        >>> # Intentar obtener el quinto lunes de febrero de 2024 (no existe)
        >>> get_nth_weekday_of_month(2024, 2, 0, 5)
        None

        >>> # Mes inválido (levantará ValueError)
        >>> try:
        >>>     get_nth_weekday_of_month(2025, 13, 0, 1)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Month must be between 1 and 12.

    **Cost:** O(1), constant time for date calculation.
    """
    # 1. Validación de entradas
    if not all(isinstance(arg, int) for arg in [year, month, weekday, n]):
        raise TypeError("All arguments (year, month, weekday, n) must be integers.")
    if not (1 <= year <= 9999):  # Rango común de años para datetime
        raise ValueError("Year is out of valid range (1-9999).")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (0 <= weekday <= 6):
        raise ValueError("Weekday must be between 0 (Monday) and 6 (Sunday).")
    if n <= 0:
        raise ValueError("Occurrence number 'n' must be a positive integer (e.g., 1 for first).")

    # 2. Encontrar el primer día del mes
    first_day_of_month = datetime(year, month, 1)

    # 3. Calcular la fecha de la primera ocurrencia del día de la semana deseado en el mes
    # `first_day_of_month.weekday()` devuelve el día de la semana para el 1er día del mes (0=Lunes).
    current_weekday = first_day_of_month.weekday()

    # Calcular cuántos días necesitamos avanzar desde el 1er día del mes para llegar
    # a la primera ocurrencia del 'weekday' deseado.
    # Por ejemplo: si el 1er día es Miércoles (2) y queremos Lunes (0): (0 - 2 + 7) % 7 = 5 días.
    # Si el 1er día es Lunes (0) y queremos Lunes (0): (0 - 0 + 7) % 7 = 0 días.
    days_to_add_for_first_occurrence = (weekday - current_weekday + 7) % 7

    # Esta es la fecha de la 1ª ocurrencia del día de la semana deseado en el mes.
    first_occurrence_date = first_day_of_month + timedelta(days=days_to_add_for_first_occurrence)

    # 4. Calcular la fecha de la n-ésima ocurrencia
    # Para la n-ésima ocurrencia, simplemente sumamos (n - 1) semanas completas (7 días cada una).
    nth_occurrence_date = first_occurrence_date + timedelta(weeks=(n - 1))

    # 5. Verificar si la n-ésima ocurrencia calculada cae dentro del mes original
    # Si el mes de la fecha calculada es diferente del mes original,
    # significa que la n-ésima ocurrencia no existe en este mes.
    if nth_occurrence_date.month == month:
        # Devolver la fecha a medianoche (00:00:00) para consistencia
        return nth_occurrence_date.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        return None
    

def add_days_from_now(days: int) -> datetime:
    """Adds or subtracts a specified number of days from the current date and time.

    This function is a convenience wrapper around `add_days_from_now`, providing
    a straightforward way to get a date offset from the present moment. It's
    useful for scenarios where calculations always begin relative to "today"
    or "now", such as setting deadlines, future reminders, or looking at past events.

    Args:
        days (int): The number of days to add (positive) or subtract (negative).

    Returns:
        datetime: A new datetime object representing the date and time after
                  adding/subtracting the specified number of days from the current time.

    Raises:
        TypeError: If 'days' is not an integer. (This check is implicitly handled
                   by the call to `add_days_from_now` which has its own type check).

    Example:
        >>> from datetime import datetime
        >>> # Get today's date (will vary based on when you run it)
        >>> today_plus_5_days = add_days_from_now(5)
        >>> print(f"5 days from now: {today_plus_5_days}")
        # Expected output (will vary): 5 days from now: 2025-06-17 10:35:03.123456

        >>> yesterday = add_days_from_now(-1)
        >>> print(f"Yesterday: {yesterday}")
        # Expected output (will vary): Yesterday: 2025-06-11 10:35:03.123456

        >>> future_date = add_days_from_now(30)
        >>> print(f"30 days from now: {future_date}")
        # Expected output (will vary): 30 days from now: 2025-07-12 10:35:03.123456

    **Cost:** O(1), constant time for getting current time and adding days.
    """
    # Get the current datetime. This is the starting point for the calculation.
    current_datetime = datetime.now()

    # Reuse the existing add_days_from_now function to perform the actual
    # addition/subtraction, promoting code reusability and reducing duplication.
    return add_time_to_date(current_datetime, days, 'days')


def add_time_to_date(original_date: datetime | str | date, quantity: int, unit: str) -> datetime:
    """Adds or subtracts a specified quantity of a given time unit to/from a date.

    Description:
        This function takes a date, which can be a `datetime` object, a `date` object,
        or a `str`, and adds or subtracts a specified quantity based on the unit.
        It leverages the `string_to_date` helper function to intelligently parse string inputs.
        If a `date` object is provided, it's converted to a `datetime` object at
        the beginning of the day (00:00:00) to ensure consistent calculations.

    Args:
        original_date (datetime | str | date): The starting date. This can be a
                                                `datetime.datetime` object, a
                                                `datetime.date` object, or a
                                                string representation of a date
                                                (e.g., "2023-01-15", "01/15/2023").
        quantity (int): The number of units to add (positive) or subtract (negative).
        unit (str): The unit of time to add or subtract. Valid units are:
                    'microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks'.

    Returns:
        datetime: A new `datetime.datetime` object representing the date after
                  adding or subtracting the specified time.

    Raises:
        TypeError: If 'quantity' is not an integer or 'unit' is not a string.
        ValueError: If 'original_date' is a string that cannot be parsed by
                    `string_to_date`, if 'original_date' is of an unsupported type,
                    or if 'unit' is not a supported time unit.

    Example of use:
        >>> from datetime import datetime, date
        >>> add_time_to_date(datetime(2023, 1, 15), 10, 'days')
        datetime.datetime(2023, 1, 25, 0, 0)
        >>> add_time_to_date(date(2023, 1, 15), -5, 'days')
        datetime.datetime(2023, 1, 10, 0, 0)
        >>> add_time_to_date("2023-01-15", 7, 'days')
        datetime.datetime(2023, 1, 22, 0, 0)
        >>> add_time_to_date("2023/01/15 14:30:00", 2, 'hours')
        datetime.datetime(2023, 1, 15, 16, 30)
        >>> add_time_to_date("2023-01-15 10:00:00", 30, 'minutes')
        datetime.datetime(2023, 1, 15, 10, 30)
        >>> add_time_to_date("2023-01-15", 1, 'weeks')
        datetime.datetime(2023, 1, 22, 0, 0)

    Cost: O(1)
    """
    # Validate the 'quantity' parameter.
    if not isinstance(quantity, int):
        raise TypeError("Input 'quantity' must be an integer.")
    
    # Validate the 'unit' parameter.
    if not isinstance(unit, str):
        raise TypeError("Input 'unit' must be a string.")

    # Use string_to_date to convert the input to a datetime or date object.
    # This handles both string parsing and direct passthrough of date/datetime objects.
    processed_date = string_to_date(original_date)

    # If string_to_date couldn't convert the input, it returns None.
    # In this case, we raise a ValueError because we can't proceed.
    if processed_date is None:
        raise ValueError(f"Could not parse 'original_date': '{original_date}'. "
                         "Please ensure it's a valid date/datetime string or object.")

    # If the processed date is a `date` object (meaning it came from a date-only string
    # or a `date` object itself), convert it to a `datetime` object at midnight.
    # This ensures consistency for `timedelta` operations, which prefer `datetime` objects.
    if isinstance(processed_date, date) and not isinstance(processed_date, datetime):
        processed_date = datetime(processed_date.year, processed_date.month, processed_date.day)
    
    # Map the unit string to the corresponding timedelta argument
    # We use a dictionary for clear mapping and easy extension.
    unit_mapping = {
        'microseconds': 'microseconds',
        'milliseconds': 'milliseconds',
        'seconds': 'seconds',
        'minutes': 'minutes',
        'hours': 'hours',
        'days': 'days',
        'weeks': 'weeks',
    }

    unit_arg = unit_mapping.get(unit.lower())
    if unit_arg is None:
        raise ValueError(f"Unsupported time unit: '{unit}'. "
                         "Supported units are: 'microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks'.")

    # Create the timedelta object dynamically based on the unit
    # The ** operator unpacks the dictionary into keyword arguments for timedelta.
    delta = timedelta(**{unit_arg: quantity})

    # Perform the addition/subtraction using `timedelta`.
    return processed_date + delta


def diff_time(start_date: datetime | str | date, end_date: datetime | str | date, unit: str) -> int:
    """Returns the whole-unit difference between two dates.

    Description:
        Uses `time_difference()` to compute the delta and returns the integer
        number of complete units between `start_date` and `end_date`. Supported
        units mirror `add_time_to_date`: 'microseconds', 'milliseconds', 'seconds',
        'minutes', 'hours', 'days', 'weeks'.

    Args:
        start_date (datetime | str | date): Start date/time.
        end_date (datetime | str | date): End date/time.
        unit (str): Unit of time ('microseconds', 'milliseconds', 'seconds',
                    'minutes', 'hours', 'days', 'weeks').

    Returns:
        int: Whole-unit difference according to the specified unit.

    Usage Example:
        >>> from shortfx.fxDate.date_operations import diff_time
        >>> diff_time("2025-01-01", "2025-01-03", "days")
        2
        >>> diff_time("2025-01-01 00:00:00", "2025-01-02 12:00:00", "hours")
        36
        >>> diff_time("2025-01-01", "2025-01-15", "weeks")
        2

    Notes:
        - This function returns whole units (integer truncation). For fractional
          differences (e.g., 1.5 hours), use `time_difference()` instead.

    Cost: O(1)
    """
    iv = unit.lower()
    supported = {"microseconds", "milliseconds", "seconds", "minutes", "hours", "days", "weeks"}
    if iv not in supported:
        raise ValueError(
            "Unsupported time unit. Use one of microseconds, milliseconds, seconds, "
            "minutes, hours, days, weeks."
        )

    # Delegate to time_difference and truncate to whole units
    return int(time_difference(start_date, end_date, iv))


def time_difference(start_date: datetime | str | date, end_date: datetime | str | date, unit: str = 'days') -> float:
    """Calculates the difference between two dates in a specified unit of time.

    Description:
        This function takes two dates, which can be `datetime` objects, `date` objects,
        or `str` representations, and calculates the difference between them
        in the specified unit (e.g., 'days', 'hours', 'minutes'). It uses the
        `string_to_date` helper function to parse string inputs intelligently,
        converting `date` objects to `datetime` objects at the start of the day
        (00:00:00) for consistent calculations.

    Args:
        start_date (datetime | str | date): The starting date. This can be a
                                            `datetime.datetime` object, a
                                            `datetime.date` object, or a
                                            string representation of a date
                                            (e.g., "2023-01-15", "01/15/2023").
        end_date (datetime | str | date): The ending date. This can be a
                                          `datetime.datetime` object, a
                                          `datetime.date` object, or a
                                          string representation of a date.
        unit (str, optional): The unit of time for the difference. Valid units are:
                              'microseconds', 'milliseconds', 'seconds', 'minutes',
                              'hours', 'days', 'weeks'. Defaults to 'days'.

    Returns:
        float: The numerical difference between the two dates in the specified
               unit (can be negative if start_date > end_date). The return type
               is float to allow for fractional differences (e.g., 1.5 hours).

    Raises:
        TypeError: If `start_date` or `end_date` are of unsupported types after
                   parsing, or if 'unit' is not a string.
        ValueError: If `start_date` or `end_date` are strings that cannot be parsed
                    by `string_to_date`, or if 'unit' is not a supported time unit.

    Example of use:
        >>> from datetime import datetime, date
        >>> date1 = datetime(2023, 1, 1, 10, 0, 0)
        >>> date2 = datetime(2023, 1, 1, 12, 30, 0)
        >>> time_difference(date1, date2, 'minutes')
        150.0
        >>> time_difference("2023-01-01", "2023-01-10", 'days')
        9.0
        >>> time_difference("2023-01-01 10:00:00", "2023-01-02 11:00:00", 'hours')
        25.0
        >>> time_difference(date(2023, 5, 1), date(2023, 4, 25), 'days')
        -6.0
        >>> time_difference("2023-01-01 00:00:00", "2023-01-01 00:00:01.5", 'milliseconds')
        1500.0

    **Cost:** O(1), constant time for date subtraction and conversion.
    """
    # Use string_to_date to convert inputs to datetime objects
    processed_start_date = string_to_date(start_date)
    processed_end_date = string_to_date(end_date)

    # Validate that both dates were successfully parsed into datetime objects
    if not isinstance(processed_start_date, datetime):
        raise TypeError(f"'start_date' could not be converted to a datetime object: {start_date}")
    if not isinstance(processed_end_date, datetime):
        raise TypeError(f"'end_date' could not be converted to a datetime object: {end_date}")

    # Validate the 'unit' parameter
    if not isinstance(unit, str):
        raise TypeError("Input 'unit' must be a string.")

    delta: timedelta = processed_end_date - processed_start_date

    # Define conversion factors from seconds to other units
    conversion_factors = {
        'microseconds': 1_000_000.0,
        'milliseconds': 1_000.0,
        'seconds': 1.0,
        'minutes': 1.0 / 60.0,
        'hours': 1.0 / 3600.0,
        'days': 1.0 / 86400.0,
        'weeks': 1.0 / (86400.0 * 7),
    }

    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported time unit: '{unit}'. "
                         "Supported units are: 'microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks'.")

    # Calculate total seconds and convert to the desired unit
    total_seconds = delta.total_seconds()
    return total_seconds * conversion_factors[unit.lower()]


def date_part(part: str, my_date: datetime | str | date, first_day_of_week: int = 0, first_week_of_year: int = 1) -> int:
    """
    Extrae una parte específica de una fecha y hora, similar a la función DatePart de VBA.

    Args:
        part (str): La parte de la fecha a extraer. Las opciones son:
                    - 'd': Día del mes (1-31)
                    - 'y': Día del año (1-366)
                    - 'h': Hora (0-23)
                    - 'n': Minuto (0-59)
                    - 's': Segundo (0-59)
                    - 'm': Mes (1-12)
                    - 'yyyy': Año
                    - 'w': Día de la semana (1-7). Requiere `first_day_of_week`.
                    - 'ww': Semana del año (1-53). Requiere `first_day_of_week` y `first_week_of_year`.
        my_date (datetime | str | date): La fecha/hora de la que se extraerá la parte.
                                        Puede ser un objeto datetime, date o una cadena.
        first_day_of_week (int, opcional): Define el primer día de la semana para 'w' y 'ww'.
                                            0 = Lunes (predeterminado), 6 = Domingo.
                                            (Similar a vbMonday=2 en VBA, pero aquí adaptado a 0-6).
        first_week_of_year (int, opcional): Define cómo se determina la primera semana del año para 'ww'.
                                            1 = La semana que contiene el 1 de enero (predeterminado).
                                            Esta implementación se enfoca en ISO week number (semana que contiene el primer jueves).

    Returns:
        int: El valor entero de la parte de la fecha solicitada.

    Raises:
        TypeError: Si 'my_date' no puede ser convertido a un objeto datetime o si 'part' no es una cadena.
        ValueError: Si la 'part' solicitada no es válida o si hay un problema con los argumentos.

    Ejemplos de uso:
        >>> from datetime import datetime, date
        >>> my_date_obj = datetime(2024, 10, 25, 15, 35, 45)
        >>> date_part("d", my_date_obj)
        25
        >>> date_part("y", my_date_obj)
        299
        >>> date_part("h", my_date_obj)
        15
        >>> date_part("n", my_date_obj)
        35
        >>> date_part("s", my_date_obj)
        45
        >>> date_part("m", my_date_obj)
        10
        >>> date_part("yyyy", my_date_obj)
        2024
        >>> date_part("w", my_date_obj, first_day_of_week=0) # Lunes como primer día (por defecto)
        5 # Viernes
        >>> date_part("ww", my_date_obj, first_day_of_week=0, first_week_of_year=1) # ISO week number
        43
        >>> date_part("ww", "2023-01-01", first_day_of_week=0, first_week_of_year=1) # Ejemplo ISO, 2023-01-01 es domingo, semana 52 de 2022
        52
        >>> date_part("ww", "2023-01-02", first_day_of_week=0, first_week_of_year=1) # Lunes, semana 1 de 2023
        1

    **Cost:** O(1), constant time for extracting date components.
    """
    if not isinstance(part, str):
        raise TypeError("El argumento 'part' debe ser una cadena.")

    # Convierte la entrada de fecha a un objeto datetime
    processed_date = string_to_datetime(my_date)

    if processed_date is None:
        raise TypeError(f"No se pudo convertir '{my_date}' a un objeto datetime válido.")

    # Mapeo de las "partes" solicitadas a los atributos de datetime
    if part == "d":
        return processed_date.day
    elif part == "y":
        return processed_date.timetuple().tm_yday
    elif part == "h":
        return processed_date.hour
    elif part == "n":  # 'n' para minuto en VBA
        return processed_date.minute
    elif part == "s":
        return processed_date.second
    elif part == "m":
        return processed_date.month
    elif part == "yyyy":
        return processed_date.year
    elif part == "w":
        # Python's weekday() returns 0 for Monday, 6 for Sunday.
        # We need to adjust based on `first_day_of_week`.
        # VBA's DatePart("w", date, vbMonday) where vbMonday is 2 makes Monday=1.
        # Our `first_day_of_week=0` maps to Monday=1 in result.
        # (processed_date.weekday() - first_day_of_week + 7) % 7 + 1
        # Example: if Monday (0) is first day (0), then (0-0+7)%7+1 = 1
        # if Tuesday (1) is first day (0), then (1-0+7)%7+1 = 2
        # if Sunday (6) is first day (0), then (6-0+7)%7+1 = 7
        return (processed_date.weekday() - first_day_of_week + 7) % 7 + 1
    elif part == "ww":
        # Python's `isocalendar()` returns (year, week_number, weekday)
        # This aligns with ISO 8601 week numbers, where week 1 is the first week
        # with at least 4 days in the new year, or equivalently, the week
        # containing the first Thursday of the year.
        # VBA's `first_week_of_year=2` (vbFirstFourDays) corresponds to ISO.
        # Our implementation uses isocalendar for simplicity and commonality.
        # We largely ignore `first_day_of_week` for 'ww' as isocalendar handles its own logic.
        return processed_date.isocalendar()[1]
    else:
        raise ValueError(f"Parte de fecha no válida: '{part}'. Consulte la documentación para ver las opciones válidas.")


def parts_to_date(year: int, month: int, day: int) -> date:
    """Create a date from year, month and day with overflow support.

    Overflowing values are normalised automatically: month 14
    becomes February of the next year, day 0 becomes the last day
    of the previous month, day 32 rolls into the next month, etc.

    Args:
        year: Year component.
        month: Month component (may overflow beyond 1-12).
        day: Day component (may overflow; 0 = last day of previous month).

    Returns:
        date: The resulting date after normalisation.

    Raises:
        TypeError: If any argument is not an integer.

    Example:
        >>> parts_to_date(2025, 10, 30)
        datetime.date(2025, 10, 30)
        >>> parts_to_date(2024, 14, 1)
        datetime.date(2025, 2, 1)
        >>> parts_to_date(2024, 3, 0)
        datetime.date(2024, 2, 29)
        >>> parts_to_date(2024, 1, -1)
        datetime.date(2023, 12, 30)
        >>> parts_to_date(2024, 0, 15)
        datetime.date(2023, 12, 15)

    Complexity: O(1)
    """
    if not all(isinstance(arg, int) for arg in [year, month, day]):
        raise TypeError("Arguments 'year', 'month' and 'day' must be integers.")

    # Normalise month overflow.
    month -= 1
    year += month // 12
    month = month % 12 + 1

    # Build base date on the 1st, then add day offset.
    return date(year, month, 1) + timedelta(days=day - 1)


def parts_to_datetime(
    year: int,
    month: int,
    day: int,
    hour: int = 0,
    minute: int = 0,
    second: int = 0,
    microsecond: int = 0,
) -> datetime:
    """Create a datetime from components with overflow support.

    Overflowing values are normalised: month 14 rolls into the next
    year, day 0 becomes the last day of the previous month, hour 25
    becomes 01:00 of the next day, etc.

    Args:
        year: Year component.
        month: Month component (may overflow).
        day: Day component (may overflow; 0 = last day of prev. month).
        hour: Hour component (default 0, may overflow).
        minute: Minute component (default 0, may overflow).
        second: Second component (default 0, may overflow).
        microsecond: Microsecond component (default 0, may overflow).

    Returns:
        datetime: The resulting datetime after normalisation.

    Raises:
        TypeError: If any argument is not an integer.

    Example:
        >>> parts_to_datetime(2025, 10, 30, 15, 30, 45)
        datetime.datetime(2025, 10, 30, 15, 30, 45)
        >>> parts_to_datetime(2025, 1, 1)
        datetime.datetime(2025, 1, 1, 0, 0)
        >>> parts_to_datetime(2024, 1, 1, 25, 0, 0)
        datetime.datetime(2024, 1, 2, 1, 0)

    Complexity: O(1)
    """
    if not all(isinstance(arg, int) for arg in [year, month, day, hour, minute, second, microsecond]):
        raise TypeError("All date/time arguments must be integers.")

    # Normalise month overflow.
    month -= 1
    year += month // 12
    month = month % 12 + 1

    # Build base at day 1, midnight, then add offsets.
    base = datetime(year, month, 1)
    delta = timedelta(
        days=day - 1,
        hours=hour,
        minutes=minute,
        seconds=second,
        microseconds=microsecond,
    )

    return base + delta


def parts_to_time(
    hour: int = 0,
    minute: int = 0,
    second: int = 0,
    microsecond: int = 0,
) -> time:
    """Create a time object from hour, minute and second with overflow.

    Overflowing values wrap around a 24-hour clock: 90 minutes becomes
    1 hour 30 minutes, 25 hours wraps to 01:00, etc.

    Args:
        hour: Hour component (may overflow, wraps mod 24).
        minute: Minute component (may overflow).
        second: Second component (may overflow).
        microsecond: Microsecond component (may overflow).

    Returns:
        time: The resulting time after normalisation.

    Raises:
        TypeError: If any argument is not an integer.

    Example:
        >>> parts_to_time(14, 30, 0)
        datetime.time(14, 30)
        >>> parts_to_time(25, 0, 0)
        datetime.time(1, 0)
        >>> parts_to_time(0, 90, 0)
        datetime.time(1, 30)

    Complexity: O(1)
    """
    if not all(isinstance(arg, int) for arg in [hour, minute, second, microsecond]):
        raise TypeError("All time arguments must be integers.")

    total = timedelta(
        hours=hour,
        minutes=minute,
        seconds=second,
        microseconds=microsecond,
    )
    # Keep only the time-of-day portion (mod 24 h).
    total_us = int(total.total_seconds() * 1_000_000) % (24 * 3600 * 1_000_000)
    total_s, us = divmod(total_us, 1_000_000)
    m, s = divmod(total_s, 60)
    h, m = divmod(m, 60)

    return time(h, m, s, us)
    

def is_between_dates(
    target_date: Union[datetime, str],
    start_date: Union[datetime, str],
    end_date: Union[datetime, str],
    inclusive: bool = True,
    format: Optional[str] = None
) -> bool:
    """Comprueba si una 'target_date' se encuentra entre 'start_date' y 'end_date'.

    Problema/Necesidad del Usuario: Es una operación extremadamente común verificar
    si una fecha cae dentro de un rango de fechas definido. Esto es vital para
    filtros, validaciones de disponibilidad, o reglas de negocio que aplican en ciertos periodos.

    Objetivos del Producto: Simplificar la lógica de validación de rangos de fechas,
    haciéndola intuitiva y flexible (con la opción de incluir o excluir los límites).

    Descripción: Dada una fecha objetivo (`target_date`), esta función verifica
    si cae dentro del rango definido por `start_date` y `end_date`. Permite
    especificar si el rango es inclusivo (los límites `start_date` y `end_date`
    se consideran parte del rango) o exclusivo (la `target_date` debe ser
    estrictamente entre `start_date` y `end_date`). Las fechas de entrada pueden
    ser objetos `datetime` o cadenas de texto.

    Args:
        target_date (Union[datetime, str]): La fecha que se desea comprobar.
        start_date (Union[datetime, str]): La fecha de inicio del rango.
        end_date (Union[datetime, str]): La fecha de fin del rango.
        inclusive (bool, optional): Si `True` (por defecto), el `target_date`
                                    puede ser igual a `start_date` o `end_date`.
                                    Si `False`, `target_date` debe ser estrictamente
                                    mayor que `start_date` y estrictamente menor que `end_date`.
        format (str, optional): El formato de cadena de fecha (ej. `'%Y-%m-%d %H:%M:%S'`)
                                si alguna de las fechas de entrada (`target_date`,
                                `start_date`, `end_date`) es una cadena. Es
                                **obligatorio** si se usa alguna cadena.

    Returns:
        bool: `True` si `target_date` está dentro del rango (según `inclusive`),
              `False` en caso contrario.

    Raises:
        TypeError: Si alguna de las fechas de entrada no es un objeto `datetime` o una cadena.
        ValueError: Si alguna cadena de fecha no puede ser parseada con el formato
                    dado, si `format` es `None` para una entrada de cadena, o
                    si `start_date` es posterior a `end_date` (lo cual es una inconsistencia lógica).

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo inclusivo (por defecto)
        >>> # La fecha está dentro del rango
        >>> is_between_dates(datetime(2025, 6, 15), datetime(2025, 6, 1), datetime(2025, 6, 30))
        True
        >>> # La fecha es igual al límite inferior (inclusivo)
        >>> is_between_dates(datetime(2025, 6, 1), datetime(2025, 6, 1), datetime(2025, 6, 30))
        True
        >>> # La fecha es igual al límite superior (inclusivo)
        >>> is_between_dates(datetime(2025, 6, 30), datetime(2025, 6, 1), datetime(2025, 6, 30))
        True
        >>> # La fecha está fuera del rango
        >>> is_between_dates(datetime(2025, 7, 1), datetime(2025, 6, 1), datetime(2025, 6, 30))
        False

        >>> # Ejemplo exclusivo
        >>> # La fecha está dentro del rango (exclusivo)
        >>> is_between_dates(datetime(2025, 6, 15), datetime(2025, 6, 1), datetime(2025, 6, 30), inclusive=False)
        True
        >>> # La fecha es igual al límite inferior (exclusivo)
        >>> is_between_dates(datetime(2025, 6, 1), datetime(2025, 6, 1), datetime(2025, 6, 30), inclusive=False)
        False
        >>> # La fecha es igual al límite superior (exclusivo)
        >>> is_between_dates(datetime(2025, 6, 30), datetime(2025, 6, 1), datetime(2025, 6, 30), inclusive=False)
        False

        >>> # Ejemplo con cadenas de fecha (mismo formato para todas)
        >>> is_between_dates("2025-06-15 10:00:00", "2025-06-01 00:00:00", "2025-06-30 23:59:59", format="%Y-%m-%d %H:%M:%S")
        True
        >>> # Sin formato para cadena de fecha (levantará ValueError)
        >>> try:
        >>>     is_between_dates("2025-06-15", datetime(2025, 6, 1), datetime(2025, 6, 30))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: 'target_date_format' is required when 'target_date' is a string.

        >>> # start_date después de end_date (levantará ValueError)
        >>> try:
        >>>     is_between_dates(datetime(2025, 6, 15), datetime(2025, 6, 30), datetime(2025, 6, 1))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: start_date cannot be after end_date.

    **Cost:** O(1), constant time for date comparisons.
    """

    # Helper function to parse any single date input
    def _parse_date_input_internal(date_val: Union[datetime, str], param_name_for_error: str) -> datetime:
        """Internal helper to parse a single date input (datetime object or string)."""
        if isinstance(date_val, str):
            if format is None:
                # Indicate which parameter's format is missing
                raise ValueError(f"'{param_name_for_error}_format' is required when '{param_name_for_error}' is a string. Please provide the 'format' argument.")
            try:
                # Parse the string using the provided format
                return datetime.strptime(date_val, format)
            except ValueError as e:
                # Re-raise with a more specific error message
                raise ValueError(f"Could not parse date string '{date_val}' for '{param_name_for_error}' with format '{format}'. Error: {e}") from e
        elif isinstance(date_val, datetime):
            # If it's already a datetime object, return it as is
            return date_val
        else:
            # Raise an error if the type is not supported
            raise TypeError(f"Input '{param_name_for_error}' must be a datetime object or a string.")

    # Parse all three date inputs using the helper
    parsed_target_date = _parse_date_input_internal(target_date, 'target_date')
    parsed_start_date = _parse_date_input_internal(start_date, 'start_date')
    parsed_end_date = _parse_date_input_internal(end_date, 'end_date')

    # Validate the logical order of start_date and end_date
    if parsed_start_date > parsed_end_date:
        raise ValueError("start_date cannot be after end_date. Please ensure start_date <= end_date.")

    # Perform the comparison based on the 'inclusive' parameter
    if inclusive:
        # Check if target_date is greater than or equal to start_date AND
        # less than or equal to end_date
        return parsed_start_date <= parsed_target_date <= parsed_end_date
    else:
        # Check if target_date is strictly greater than start_date AND
        # strictly less than end_date
        return parsed_start_date < parsed_target_date < parsed_end_date
    

def is_valid_time(hour: int, minute: int, second: int = 0, microsecond: int = 0) -> bool:
    """Verifica si una combinación de hora, minuto, segundo y microsegundo dada representa una hora válida.

    Problema/Necesidad del Usuario: Al recibir entradas de tiempo de usuario, es crucial validar
    que los componentes de la hora (horas, minutos, segundos) sean lógicamente posibles
    (ej. no "25:00:00").

    Objetivos del Producto: Mejorar la robustez de la entrada de datos de tiempo,
    reduciendo errores y validaciones en capas superiores de la aplicación.

    Descripción: Esta función toma valores enteros para la hora, minuto, segundo y microsegundo.
    Devuelve `True` si todos los componentes están dentro de sus rangos válidos
    (ej., hora entre 0 y 23, minuto/segundo entre 0 y 59, microsegundo entre 0 y 999999).
    Si alguno de los componentes no es un entero o está fuera de su rango válido,
    la función devuelve `False`.

    Args:
        hour (int): La hora a validar (0-23).
        minute (int): El minuto a validar (0-59).
        second (int, optional): El segundo a validar (0-59). Por defecto es 0.
        microsecond (int, optional): El microsegundo a validar (0-999999). Por defecto es 0.

    Returns:
        bool: `True` si la combinación de tiempo es válida; `False` en caso contrario.

    Example:
        >>> # Ejemplos de uso
        >>> is_valid_time(23, 59, 59)
        True
        >>> is_valid_time(0, 0, 0, 0)
        True
        >>> is_valid_time(12, 30) # Sin segundos ni microsegundos
        True
        >>> is_valid_time(25, 0, 0) # Hora inválida
        False
        >>> is_valid_time(10, 60, 0) # Minuto inválido
        False
        >>> is_valid_time(1, 1, 60) # Segundo inválido
        False
        >>> is_valid_time(1, 1, 1, 1000000) # Microsegundo inválido
        False
        >>> is_valid_time(-1, 0, 0) # Hora negativa
        False
        >>> is_valid_time(10, 0, 'abc') # Tipo de dato incorrecto
        False

    **Cost:** O(1), constant time for validation checks.
    """
    # Validar que todos los componentes sean enteros
    if not all(isinstance(arg, int) for arg in [hour, minute, second, microsecond]):
        return False

    # Validar la hora (0 a 23)
    if not (0 <= hour <= 23):
        return False

    # Validar el minuto (0 a 59)
    if not (0 <= minute <= 59):
        return False

    # Validar el segundo (0 a 59)
    if not (0 <= second <= 59):
        return False

    # Validar el microsegundo (0 a 999999)
    if not (0 <= microsecond <= 999999):
        return False

    # Si todas las validaciones pasan, la hora es válida
    return True


def time_from_datetime(datetime_object: datetime) -> time:
    """Extracts the time component from a datetime object.

    Args:
        datetime_object (datetime): The datetime object from which to extract the time.

    Returns:
        time: A time object representing the hour, minute, second, and microsecond
              of the input datetime object.

    Raises:
        TypeError: If 'datetime_object' is not a datetime object.

    Example:
        >>> from datetime import datetime, time
        >>> my_datetime = datetime(2023, 10, 26, 15, 30, 45, 123456)
        >>> time_from_datetime(my_datetime)
        datetime.time(15, 30, 45, 123456)
        >>> time_from_datetime(datetime(2024, 1, 1, 9, 0, 0))
        datetime.time(9, 0)

    **Cost:** O(1), constant time for extracting time component.
    """
    if not isinstance(datetime_object, datetime):
        raise TypeError("Input 'datetime_object' must be a datetime object.")

    # The .time() method directly returns the time portion of a datetime object.
    return datetime_object.time()


def get_date_component(date_input: datetime, component: Literal["day", "month", "year", "hour", "minute", "second"]) -> int:
    """Extracts a specific component (day, month, year, hour, minute, or second) from a date.

    Args:
        date_input (datetime): The datetime object from which to extract the component.
        component (Literal["day", "month", "year", "hour", "minute", "second"]): A string indicating which
                                                                                 component to extract.
                                                                                 Must be "day", "month", "year",
                                                                                 "hour", "minute", or "second".

    Returns:
        int: The requested date component (day of month, month number, year number,
             hour number (0-23), minute number (0-59), or second number (0-59)).

    Raises:
        TypeError: If 'date_input' is not a datetime object.
        ValueError: If 'component' is not one of the allowed values.

    Example:
        >>> from datetime import datetime
        >>> my_date = datetime(2023, 10, 26, 15, 30, 45) # 3:30:45 PM
        >>> get_date_component(my_date, "day")
        26
        >>> get_date_component(my_date, "month")
        10
        >>> get_date_component(my_date, "year")
        2023
        >>> get_date_component(my_date, "hour")
        15
        >>> get_date_component(my_date, "minute")
        30
        >>> get_date_component(my_date, "second")
        45

    **Cost:** O(1), constant time for accessing datetime attributes.
    """
    # Ensure the input date is a datetime object.
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Convert the component string to lowercase for case-insensitive comparison.
    normalized_component = component.lower()

    # Extract the requested component based on the normalized string.
    if normalized_component == "day":
        return date_input.day
    elif normalized_component == "month":
        return date_input.month
    elif normalized_component == "year":
        return date_input.year
    elif normalized_component == "hour":
        return date_input.hour
    elif normalized_component == "minute":
        return date_input.minute
    elif normalized_component == "second":
        return date_input.second
    else:
        # Raise an error if an invalid component string is provided.
        raise ValueError("Invalid 'component' specified. Must be 'day', 'month', 'year', 'hour', 'minute', or 'second'.")
    

def set_date_component(date_input: datetime, **kwargs: Any) -> datetime:
    """Returns a new datetime object with specified components modified.

    Problem/User Need: Users often need to modify only a part of an existing date
    without affecting the others (e.g., change only the day to 15, or set the time to 00:00:00).

    Product Goals: Offer granular and flexible date manipulation, useful for
    date editing scenarios or precise normalization.

    Description: Given an existing datetime object, this function returns a new datetime
    object where the components specified in `kwargs` (e.g., 'year', 'month', 'day',
    'hour', 'minute', 'second', 'microsecond', 'tzinfo') have been updated.
    All other components remain unchanged.

    Args:
        date_input (datetime): The original datetime object to modify.
        **kwargs: Keyword arguments corresponding to datetime components you want to change.
                  Valid keywords are 'year', 'month', 'day', 'hour', 'minute', 'second',
                  'microsecond', and 'tzinfo'.

    Returns:
        datetime: A new datetime object with the specified components updated.

    Raises:
        TypeError: If 'date_input' is not a datetime object.
        ValueError: If any provided keyword argument is not a valid datetime component
                    or if its value is out of the valid range (e.g., month=13).

    Example:
        >>> from datetime import datetime, timezone

        >>> # Original date
        >>> original_date = datetime(2025, 6, 11, 15, 30, 45, 123456)
        >>> print(f"Original: {original_date}")
        Original: 2025-06-11 15:30:45.123456

        >>> # Change only the day to 1
        >>> set_date_component(original_date, day=1)
        datetime.datetime(2025, 6, 1, 15, 30, 45, 123456)

        >>> # Set hour, minute, second to midnight (00:00:00)
        >>> set_date_component(original_date, hour=0, minute=0, second=0, microsecond=0)
        datetime.datetime(2025, 6, 11, 0, 0, 0, 0)

        >>> # Change year and timezone
        >>> set_date_component(original_date, year=2026, tzinfo=timezone.utc)
        datetime.datetime(2026, 6, 11, 15, 30, 45, 123456, tzinfo=datetime.timezone.utc)

        >>> # Invalid component will raise an error
        >>> try:
        >>>     set_date_component(original_date, invalid_param=10)
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: 'invalid_param' is an invalid keyword argument for this method.

    **Cost:** O(1), constant time for creating new datetime with modified components.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # The datetime object has a built-in .replace() method that's perfect for this.
    # It takes keyword arguments to change specific components and returns a *new* datetime object.
    # It automatically handles validation for valid component names and their ranges.
    try:
        return date_input.replace(**kwargs)
    except TypeError as e:
        # Catch TypeErrors specifically from replace() for invalid kwargs
        # and re-raise as ValueError for clarity, indicating the component issue.
        if "is an invalid keyword argument" in str(e):
            raise ValueError(f"Invalid datetime component specified: {e}") from e
        raise # Re-raise other TypeErrors if any, though unlikely here
    except ValueError as e:
        # Catch ValueErrors from replace() if the value is out of range (e.g., day=32)
        raise ValueError(f"Invalid value for datetime component: {e}") from e
    

def is_leap_year(year: int) -> bool:
    """Checks if a given year is a leap year.

    A leap year occurs every four years, except for years that are
    divisible by 100 but not by 400.

    Args:
        year (int): The year to check (e.g., 2024).

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        TypeError: If 'year' is not an integer.
        ValueError: If 'year' is less than 1.

    Example:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(2023)
        False
        >>> is_leap_year(2000) # Divisible by 400, so it's a leap year
        True
        >>> is_leap_year(1900) # Divisible by 100 but not by 400, so NOT a leap year
        False

    **Cost:** O(1), constant time for arithmetic operations.
    """
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if year < 1:
        raise ValueError("Input 'year' must be a positive integer.")

    # A year is a leap year if it is divisible by 4
    # BUT if it's divisible by 100, it must also be divisible by 400.
    # This single expression covers all three rules.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_number_of_days_in_year(year: int) -> int:
    """Calculates the total number of days in a given year.

    Problem/User Need: There is a need to know the total number of days in a
    specific year for calculations like annual percentages, averages, or data validations.

    Product Goals: Simplify annual calculations and ensure accuracy by correctly
    considering leap years, which have an extra day.

    Description: Given a year as an integer, this function determines if it's a
    leap year. If it is (e.g., 2024, 2000), it returns 366 days. Otherwise (e.g., 2023, 1900),
    it returns 365 days.

    Args:
        year (int): The year for which to get the number of days (e.g., 2023, 2024).

    Returns:
        int: The total number of days in that year (either 365 or 366).

    Raises:
        TypeError: If 'year' is not an integer.
        ValueError: If 'year' is less than 1.

    Example:
        >>> get_number_of_days_in_year(2023) # Not a leap year
        365
        >>> get_number_of_days_in_year(2024) # A leap year
        366
        >>> get_number_of_days_in_year(1900) # Not a leap year (divisible by 100 but not by 400)
        365
        >>> get_number_of_days_in_year(2000) # A leap year (divisible by 400)
        366

    **Cost:** O(1), constant time for leap year check.
    """
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if year < 1:
        raise ValueError("Input 'year' must be a positive integer.")

    # The calendar.isleap() function is the standard and most reliable way
    # to check if a year is a leap year according to the Gregorian calendar rules.
    if calendar.isleap(year):
        return 366
    else:
        return 365
    

# Assuming get_week_range function is available from previous turn:
def get_week_range(year: int, week_number: int) -> Tuple[datetime, datetime]:
    """Retrieves the start and end dates (Monday to Sunday) for a specific ISO week of a given year.

    **Cost:** O(1), constant time for ISO week date calculation.
    """
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if not isinstance(week_number, int):
        raise TypeError("Input 'week_number' must be an integer.")
    if year < 1:
        raise ValueError("Input 'year' must be a positive integer.")
    if not (1 <= week_number <= 53):
        raise ValueError("Input 'week_number' must be between 1 and 53.")

    try:
        monday_of_week = datetime.fromisocalendar(year, week_number, 1)
    except ValueError as e:
        raise ValueError(f"Invalid week_number {week_number} for year {year}. Error: {e}") from e

    sunday_of_week = monday_of_week + timedelta(days=6)

    return (
        monday_of_week.replace(hour=0, minute=0, second=0, microsecond=0),
        sunday_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
    )


def get_year_calendar_by_weeks(
    year: int,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    granularity: str = "week",
) -> list:
    """Generates a calendar table for a year, similar to DAX CALENDAR/CALENDARAUTO.

    By default produces ISO-week rows (backward-compatible). When *granularity*
    is ``"day"`` it returns one row per calendar day, matching
    ``CALENDAR(start, end)`` / ``CALENDARAUTO()`` behaviour.

    Args:
        year: The calendar year. Ignored when both *start_date* and
            *end_date* are supplied.
        start_date: Optional first date of the range (inclusive).
            Defaults to Jan 1 of *year*.
        end_date: Optional last date of the range (inclusive).
            Defaults to Dec 31 of *year*.
        granularity: ``"week"`` (default, legacy) returns ISO-week tuples.
            ``"day"`` returns one dict per day with date components.

    Returns:
        When *granularity* is ``"week"``:
            List[Tuple[int, datetime, datetime]] — (week_number, monday, sunday).
        When *granularity* is ``"day"``:
            List[dict] — each dict has keys ``date``, ``year``, ``month``,
            ``day``, ``weekday``, ``quarter``, ``iso_week``.

    Raises:
        TypeError: If *year* is not an integer.
        ValueError: If *year* < 1 or *granularity* is invalid.

    Example:
        >>> # Legacy week-based calendar
        >>> cal = get_year_calendar_by_weeks(2023)
        >>> cal[0]
        (1, datetime.datetime(2023, 1, 2, 0, 0), datetime.datetime(2023, 1, 8, 0, 0))

        >>> # Day-level calendar (CALENDARAUTO style)
        >>> days = get_year_calendar_by_weeks(2023, granularity="day")
        >>> days[0]["date"]
        datetime.date(2023, 1, 1)

        >>> # Custom date range (CALENDAR style)
        >>> from datetime import datetime
        >>> days = get_year_calendar_by_weeks(
        ...     2023,
        ...     start_date=datetime(2023, 6, 1),
        ...     end_date=datetime(2023, 6, 30),
        ...     granularity="day",
        ... )
        >>> len(days)
        30

    Complexity: O(n) where n is the number of rows produced.
    """
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")

    if year < 1:
        raise ValueError("Input 'year' must be a positive integer.")

    if granularity not in ("week", "day"):
        raise ValueError("granularity must be 'week' or 'day'.")

    # --- week granularity (legacy behaviour) ---
    if granularity == "week":
        year_calendar: List[Tuple[int, datetime, datetime]] = []
        last_day_of_dec = datetime(year, 12, 28)
        max_iso_week = last_day_of_dec.isocalendar()[1]

        for week_num in range(1, max_iso_week + 1):
            start, end = get_week_range(year, week_num)
            year_calendar.append((week_num, start, end))

        return year_calendar

    # --- day granularity (CALENDAR / CALENDARAUTO) ---
    first = start_date or datetime(year, 1, 1)
    last = end_date or datetime(year, 12, 31)
    first_d = first.date() if isinstance(first, datetime) else first
    last_d = last.date() if isinstance(last, datetime) else last

    rows: List[Dict] = []
    current = first_d
    one_day = timedelta(days=1)

    while current <= last_d:
        _iso_year, iso_week, _ = current.isocalendar()
        rows.append({
            "date": current,
            "year": current.year,
            "month": current.month,
            "day": current.day,
            "weekday": current.isoweekday(),
            "quarter": (current.month - 1) // 3 + 1,
            "iso_week": iso_week,
        })
        current += one_day

    return rows


def get_quarter(date_input: Union[datetime, str], input_format: Optional[str] = None) -> int:
    """Extrae el número de trimestre (1 a 4) al que pertenece una fecha dada.

    Problema/Necesidad del Usuario: Extraer el trimestre de una fecha es una operación
    muy común para informes financieros, de ventas o de rendimiento que se agrupan por trimestres.

    Objetivos del Producto: Proporcionar una forma sencilla y directa de obtener el
    trimestre al que pertenece una fecha, simplificando la lógica de agrupación y análisis de datos.

    Descripción: Dada una fecha como objeto `datetime` o como cadena de texto,
    esta función determina y devuelve el número del trimestre del año al que
    corresponde esa fecha. Los trimestres se definen de la siguiente manera:
    - Q1: Enero (1), Febrero (2), Marzo (3)
    - Q2: Abril (4), Mayo (5), Junio (6)
    - Q3: Julio (7), Agosto (8), Septiembre (9)
    - Q4: Octubre (10), Noviembre (11), Diciembre (12)

    Args:
        date_input (Union[datetime, str]): La fecha de la cual se desea obtener el trimestre.
                                            Puede ser un objeto `datetime` o una cadena de fecha.
        input_format (str, optional): El formato de cadena de fecha (ej. `'%Y-%m-%d %H:%M:%S'`)
                                      si 'date_input' es una cadena. Es **obligatorio**
                                      si 'date_input' es una cadena.

    Returns:
        int: El número del trimestre (1, 2, 3 o 4) al que pertenece la fecha.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o una cadena.
        ValueError: Si 'date_input' es una cadena y 'input_format' es `None`,
                    o si la cadena no puede ser parseada con el formato dado.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo con objeto datetime
        >>> get_quarter(datetime(2025, 8, 15)) # Agosto (mes 8) está en el Q3
        3
        >>> get_quarter(datetime(2024, 1, 1)) # Enero (mes 1) está en el Q1
        1
        >>> get_quarter(datetime(2023, 12, 31)) # Diciembre (mes 12) está en el Q4
        4
        >>> get_quarter(datetime(2022, 4, 1)) # Abril (mes 4) está en el Q2
        2

        >>> # Ejemplo con cadena de fecha
        >>> get_quarter("2025-08-15", "%Y-%m-%d")
        3
        >>> get_quarter("2024/02/29 10:30:00", "%Y/%m/%d %H:%M:%S")
        1

        >>> # Cadena de fecha sin formato (levantará ValueError)
        >>> try:
        >>>     get_quarter("2025-06-15")
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: 'input_format' is required when 'date_input' is a string.

        >>> # Formato incorrecto para cadena de fecha (levantará ValueError)
        >>> try:
        >>>     get_quarter("15-06-2025", "%Y-%m-%d") # Formato no coincide
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Could not parse date string '15-06-2025' with format '%Y-%m-%d'. Error: time data '15-06-2025' does not match format '%Y-%m-%d'

    **Cost:** O(1), constant time for extracting month and calculating quarter.
    """
    
    # Función auxiliar interna para parsear la entrada de fecha (datetime o string)
    def _parse_date_input_internal(date_val: Union[datetime, str]) -> datetime:
        if isinstance(date_val, str):
            if input_format is None:
                # Si es una cadena y no se proporciona formato, se lanza un error
                raise ValueError("'input_format' is required when 'date_input' is a string.")
            try:
                # Intentar parsear la cadena con el formato dado
                return datetime.strptime(date_val, input_format)
            except ValueError as e:
                # Si el parseo falla, se lanza un error descriptivo
                raise ValueError(f"Could not parse date string '{date_val}' with format '{input_format}'. Error: {e}") from e
        elif isinstance(date_val, datetime):
            # Si ya es un objeto datetime, se devuelve directamente
            return date_val
        else:
            # Si el tipo de entrada no es compatible, se lanza un TypeError
            raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Parsear la fecha de entrada utilizando la función auxiliar
    parsed_date = _parse_date_input_internal(date_input)

    # Extraer el número del mes (1-12) de la fecha parseada
    month = parsed_date.month

    # Calcular el trimestre usando la lógica de los meses:
    # Enero-Marzo (1-3) -> Q1
    # Abril-Junio (4-6) -> Q2
    # Julio-Septiembre (7-9) -> Q3
    # Octubre-Diciembre (10-12) -> Q4
    # La fórmula `(month - 1) // 3 + 1` logra esto de manera concisa:
    # (1-1)//3+1 = 1 (para enero)
    # (3-1)//3+1 = 1 (para marzo)
    # (4-1)//3+1 = 2 (para abril)
    # (12-1)//3+1 = 4 (para diciembre)
    quarter = (month - 1) // 3 + 1

    return quarter


def get_number_of_days_in_quarter(year: int, quarter: int) -> int:
    """Calculates the total number of days in a specific quarter of a given year.

    Problema/Necesidad del Usuario: Para informes y análisis financieros o de rendimiento
    que se basan en trimestres, es necesario saber el número exacto de días en un trimestre
    dado, lo cual varía debido a la duración de los meses y los años bisiestos.

    Objetivos del Producto: Facilitar cálculos precisos basados en periodos trimestrales,
    sin tener que codificar manualmente la lógica de los meses y los años bisiestos.

    Descripción: Dada un año y un número de trimestre (1-4), esta función devuelve
    el número total de días en ese trimestre. Considera correctamente la duración de
    cada mes y el efecto de los años bisiestos en febrero.

    Args:
        year (int): El año para el cual se desea calcular el número de días en el trimestre.
        quarter (int): El número del trimestre (1, 2, 3 o 4).

    Returns:
        int: El número total de días en el trimestre especificado.

    Raises:
        TypeError: Si 'year' o 'quarter' no son enteros.
        ValueError: Si 'year' está fuera del rango válido (1-9999), o si 'quarter'
                    no está entre 1 y 4.

    Example:
        >>> get_number_of_days_in_quarter(2024, 1) # Q1 de un año bisiesto (Ene, Feb(29), Mar)
        91
        >>> get_number_of_days_in_quarter(2023, 1) # Q1 de un año común (Ene, Feb(28), Mar)
        90
        >>> get_number_of_days_in_quarter(2023, 2) # Q2 de un año común (Abr, May, Jun)
        91
        >>> get_number_of_days_in_quarter(2023, 3) # Q3 de un año común (Jul, Ago, Sep)
        92
        >>> get_number_of_days_in_quarter(2023, 4) # Q4 de un año común (Oct, Nov, Dic)
        92
        >>> # Año fuera de rango (levantará ValueError)
        >>> try:
        >>>     get_number_of_days_in_quarter(0, 1)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Year is out of valid range (1-9999).

    **Cost:** O(1), constant time for summing days in three months.
    """
    # 1. Validación de entradas
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if not isinstance(quarter, int):
        raise TypeError("Input 'quarter' must be an integer.")
    if not (1 <= year <= 9999): # Rango común de años para objetos datetime
        raise ValueError("Year is out of valid range (1-9999).")
    if not (1 <= quarter <= 4):
        raise ValueError("Quarter must be between 1 and 4.")

    # 2. Definir los meses que componen cada trimestre
    quarter_months: List[int]
    if quarter == 1:
        quarter_months = [1, 2, 3]  # Enero, Febrero, Marzo
    elif quarter == 2:
        quarter_months = [4, 5, 6]  # Abril, Mayo, Junio
    elif quarter == 3:
        quarter_months = [7, 8, 9]  # Julio, Agosto, Septiembre
    else:  # quarter == 4
        quarter_months = [10, 11, 12] # Octubre, Noviembre, Diciembre

    # 3. Sumar los días de cada mes en el trimestre
    total_days = 0
    for month_num in quarter_months:
        # `calendar.monthrange(year, month)[1]` devuelve el número de días en ese mes y año.
        # Esto maneja automáticamente los años bisiestos para febrero.
        days_in_month = calendar.monthrange(year, month_num)[1]
        total_days += days_in_month

    return total_days


def start_of_month(date_input: Union[datetime, str], input_format: str = None) -> datetime:
    """Returns a datetime object representing the first day of the month for a given date.

    Problem/User Need: When dealing with monthly reports, billing cycles, or any
    month-based aggregation, it's often necessary to precisely define the start
    of the month.

    Product Goals: Simplify business logic and data aggregation for monthly periods.

    Description: Given a date (as a datetime object or a string with a specified format),
    this function returns a new datetime object set to the 1st day of that date's month,
    at 00:00:00.

    Args:
        date_input (Union[datetime, str]): The date for which to get the start of the month.
                                            Can be a datetime object (e.g., datetime(2023, 10, 15))
                                            or a string (e.g., "15/10/2023").
        input_format (str, optional): The format code string for 'date_input' if it's a string.
                                      Required if 'date_input' is a string.
                                      E.g., '%d/%m/%Y' for "15/10/2023".
                                      Not used if 'date_input' is a datetime object.

    Returns:
        datetime: A new datetime object representing the 1st day of the month, at midnight.

    Raises:
        TypeError: If 'date_input' is not a datetime object or a string.
        ValueError: If 'date_input' is a string and 'input_format' is not provided,
                    or if the string cannot be parsed with the given format.

    Example:
        >>> from datetime import datetime

        >>> # Using a datetime object in the middle of a month
        >>> start_of_month(datetime(2023, 10, 15, 10, 30, 0))
        datetime.datetime(2023, 10, 1, 0, 0)

        >>> # Using a string input
        >>> start_of_month("25-11-2024", "%d-%m-%Y")
        datetime.datetime(2024, 11, 1, 0, 0)

    **Cost:** O(1), constant time for date manipulation.
    """
    # Ensure the input is a datetime object, parsing from string if necessary.
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Create a new datetime object for the 1st day of the same month and year, at 00:00:00.
    return datetime(parsed_dt.year, parsed_dt.month, 1, 0, 0, 0)


def end_of_month(date_input: Union[datetime, str], input_format: str = None) -> datetime:
    """Returns a datetime object representing the last day of the month for a given date.

    Problem/User Need: Essential for closing monthly periods, defining complete date ranges,
    or calculating durations that span full months.

    Product Goals: Complete the support for monthly reports and analysis, providing precise
    end-of-month boundaries.

    Description: Given a date (as a datetime object or a string with a specified format),
    this function returns a new datetime object set to the last day of that date's month,
    at 23:59:59.999999. It correctly handles months with 28, 29, 30, or 31 days, including leap years.

    Args:
        date_input (Union[datetime, str]): The date for which to get the end of the month.
                                            Can be a datetime object (e.g., datetime(2023, 10, 15))
                                            or a string (e.g., "15/10/2023").
        input_format (str, optional): The format code string for 'date_input' if it's a string.
                                      Required if 'date_input' is a string.
                                      E.g., '%d/%m/%Y' for "15/10/2023".
                                      Not used if 'date_input' is a datetime object.

    Returns:
        datetime: A new datetime object representing the last day of the month, at 23:59:59.999999.

    Raises:
        TypeError: If 'date_input' is not a datetime object or a string.
        ValueError: If 'date_input' is a string and 'input_format' is not provided,
                    or if the string cannot be parsed with the given format.

    Example:
        >>> from datetime import datetime

        >>> # Using a datetime object (October has 31 days)
        >>> end_of_month(datetime(2023, 10, 15, 10, 30, 0))
        datetime.datetime(2023, 10, 31, 23, 59, 59, 999999)

        >>> # Using a string input (February 2024 - a leap year)
        >>> end_of_month("20-02-2024", "%d-%m-%Y")
        datetime.datetime(2024, 2, 29, 23, 59, 59, 999999)

        >>> # February 2023 (not a leap year)
        >>> end_of_month(datetime(2023, 2, 1))
        datetime.datetime(2023, 2, 28, 23, 59, 59, 999999)

    **Cost:** O(1), constant time for date manipulation and calendar lookup.
    """
    # Ensure the input is a datetime object, parsing from string if necessary.
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Get the number of days in the month using calendar.monthrange.
    # It returns (weekday of first day, number of days in month). We need the second element.
    _, last_day_of_month = calendar.monthrange(parsed_dt.year, parsed_dt.month)

    # Create a new datetime object for the last day of the same month and year, at 23:59:59.999999.
    return datetime(parsed_dt.year, parsed_dt.month, last_day_of_month, 23, 59, 59, 999999)


def start_of_year(date_input: Union[datetime, str], input_format: str = None) -> datetime:
    """Returns a datetime object representing the first day of the year for a given date.

    Problem/User Need: Similar to months, annual reports and planning require an easy way
    to get the first day of a year.

    Product Goals: Support annual analysis and reporting functionality.

    Description: Given a date (as a datetime object or a string with a specified format),
    this function returns a new datetime object set to January 1st of the year to which
    that date belongs, at 00:00:00.

    Args:
        date_input (Union[datetime, str]): The date for which to get the start of the year.
                                            Can be a datetime object (e.g., datetime(2023, 7, 20))
                                            or a string (e.g., "20/07/2023").
        input_format (str, optional): The format code string for 'date_input' if it's a string.
                                      Required if 'date_input' is a string.
                                      E.g., '%d/%m/%Y' for "20/07/2023".
                                      Not used if 'date_input' is a datetime object.

    Returns:
        datetime: A new datetime object representing January 1st of the year, at midnight.

    Raises:
        TypeError: If 'date_input' is not a datetime object or a string.
        ValueError: If 'date_input' is a string and 'input_format' is not provided,
                    or if the string cannot be parsed with the given format.

    Example:
        >>> from datetime import datetime

        >>> # Using a datetime object
        >>> start_of_year(datetime(2023, 7, 20))
        datetime.datetime(2023, 1, 1, 0, 0)

        >>> # Using a string input
        >>> start_of_year("15-03-2024", "%d-%m-%Y")
        datetime.datetime(2024, 1, 1, 0, 0)

    **Cost:** O(1), constant time for date manipulation.
    """
    # Ensure the input is a datetime object, parsing from string if necessary.
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Create a new datetime object for January 1st of the same year, at 00:00:00.
    return datetime(parsed_dt.year, 1, 1, 0, 0, 0)


def end_of_year(date_input: Union[datetime, str], input_format: str = None) -> datetime:
    """Returns a datetime object representing the last day of the year for a given date.

    Problem/User Need: To close annual periods and define complete date ranges.

    Product Goals: Complete the support for annual reports and analysis.

    Description: Given a date (as a datetime object or a string with a specified format),
    this function returns a new datetime object set to December 31st of the year to which
    that date belongs, at 23:59:59.999999.

    Args:
        date_input (Union[datetime, str]): The date for which to get the end of the year.
                                            Can be a datetime object (e.g., datetime(2023, 7, 20))
                                            or a string (e.g., "20/07/2023").
        input_format (str, optional): The format code string for 'date_input' if it's a string.
                                      Required if 'date_input' is a string.
                                      E.g., '%d/%m/%Y' for "20/07/2023".
                                      Not used if 'date_input' is a datetime object.

    Returns:
        datetime: A new datetime object representing December 31st of the year, at 23:59:59.999999.

    Raises:
        TypeError: If 'date_input' is not a datetime object or a string.
        ValueError: If 'date_input' is a string and 'input_format' is not provided,
                    or if the string cannot be parsed with the given format.

    Example:
        >>> from datetime import datetime

        >>> # Using a datetime object
        >>> end_of_year(datetime(2023, 7, 20))
        datetime.datetime(2023, 12, 31, 23, 59, 59, 999999)

        >>> # Using a string input
        >>> end_of_year("01-01-2024", "%d-%m-%Y")
        datetime.datetime(2024, 12, 31, 23, 59, 59, 999999)

    **Cost:** O(1), constant time for date manipulation.
    """
    # Ensure the input is a datetime object, parsing from string if necessary.
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Create a new datetime object for December 31st of the same year, at 23:59:59.999999.
    return datetime(parsed_dt.year, 12, 31, 23, 59, 59, 999999)


def get_last_friday_of_month(year: int, month: int) -> datetime:
    """Calculates the date of the last Friday of a given month and year.

    This function determines the last day of the specified month and then
    iterates backward to find the most recent Friday.

    Args:
        year (int): The year (e.g., 2023).
        month (int): The month (1-12, e.g., 10 for October).

    Returns:
        datetime: A datetime object representing the last Friday of that month, at midnight.

    Raises:
        TypeError: If 'year' or 'month' are not integers.
        ValueError: If 'month' is not between 1 and 12, or if 'year' is less than 1.

    Example:
        >>> get_last_friday_of_month(2023, 10) # October 2023
        datetime.datetime(2023, 10, 27, 0, 0)
        >>> get_last_friday_of_month(2024, 2) # February 2024 (leap year)
        datetime.datetime(2024, 2, 23, 0, 0)

    **Cost:** O(1), constant time for date calculation.
    """
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if not isinstance(month, int):
        raise TypeError("Input 'month' must be an integer.")
    if not (1 <= month <= 12):
        raise ValueError("Input 'month' must be between 1 and 12.")
    if year < 1:
        raise ValueError("Input 'year' must be a positive integer.")

    # Get the last day of the given month and year
    # calendar.monthrange returns (weekday_of_first_day, num_days_in_month)
    _, last_day = calendar.monthrange(year, month)
    last_day_of_month = datetime(year, month, last_day)

    # Python's weekday() method: Monday=0, Tuesday=1, ..., Friday=4, Saturday=5, Sunday=6
    # We want Friday, which is 4.
    # Calculate how many days to subtract from the last day to get to the last Friday.
    # (last_day_of_month.weekday() - 4 + 7) % 7 gives the number of days to go back.
    # For example, if last day is Sat (5), (5 - 4 + 7) % 7 = 8 % 7 = 1. Subtract 1 day.
    # If last day is Fri (4), (4 - 4 + 7) % 7 = 7 % 7 = 0. Subtract 0 days.
    days_to_subtract = (last_day_of_month.weekday() - 4 + 7) % 7

    last_friday = last_day_of_month - timedelta(days=days_to_subtract)
    return last_friday.replace(hour=0, minute=0, second=0, microsecond=0)


def get_next_friday(date_input: datetime) -> datetime:
    """Calculates the date of the next upcoming Friday relative to a given date.

    This function is useful for scheduling or determining the immediate
    future occurrence of Friday.

    Args:
        date_input (datetime): The starting date from which to find the next Friday.

    Returns:
        datetime: A datetime object representing the next Friday, at midnight.
                  If the input date is a Friday, it returns the Friday of the following week.

    Raises:
        TypeError: If 'date_input' is not a datetime object.

    Example:
        >>> get_next_friday(datetime(2023, 10, 26)) # Thursday
        datetime.datetime(2023, 10, 27, 0, 0)
        >>> get_next_friday(datetime(2023, 10, 27)) # Friday
        datetime.datetime(2023, 11, 3, 0, 0)
        >>> get_next_friday(datetime(2023, 10, 28)) # Saturday
        datetime.datetime(2023, 11, 3, 0, 0)

    **Cost:** O(1), constant time for date arithmetic.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Python's weekday() method: Monday=0, Tuesday=1, ..., Friday=4, Saturday=5, Sunday=6
    # We want Friday, which is 4.
    # Calculate how many days until the next Friday.
    # (4 - date_input.weekday() + 7) % 7 will give 0 for Friday, 1 for Thursday, 2 for Wednesday, etc.
    # To get the *next* Friday (even if today is Friday), we need to ensure at least 1 day is added for Friday.
    # A cleaner approach is to add 7 days if it's Friday, otherwise calculate the difference.
    days_until_friday = (4 - date_input.weekday() + 7) % 7
    if days_until_friday == 0: # If today is Friday, we want the Friday of the *next* week.
        days_until_friday = 7

    next_friday = date_input + timedelta(days=days_until_friday)
    return next_friday.replace(hour=0, minute=0, second=0, microsecond=0)


def get_previous_friday(date_input: datetime) -> datetime:
    """Calculates the date of the immediately preceding Friday relative to a given date.

    This function is useful for going back in time to the nearest past Friday,
    for instance, to align data to the end of the last working week.

    Args:
        date_input (datetime): The starting date from which to find the previous Friday.

    Returns:
        datetime: A datetime object representing the previous Friday, at midnight.
                  If the input date is a Friday, it returns that date itself.

    Raises:
        TypeError: If 'date_input' is not a datetime object.

    Example:
        >>> from datetime import datetime

        >>> # Starting from a Monday (June 9, 2025 was a Monday)
        >>> get_previous_friday(datetime(2025, 6, 9))
        datetime.datetime(2025, 6, 6, 0, 0)

        >>> # Starting from a Thursday (June 12, 2025 will be a Thursday)
        >>> get_previous_friday(datetime(2025, 6, 12))
        datetime.datetime(2025, 6, 6, 0, 0)

        >>> # Starting from a Friday (June 6, 2025 was a Friday)
        >>> get_previous_friday(datetime(2025, 6, 6))
        datetime.datetime(2025, 6, 6, 0, 0)

        >>> # Starting from a Sunday (June 8, 2025 was a Sunday)
        >>> get_previous_friday(datetime(2025, 6, 8))
        datetime.datetime(2025, 6, 6, 0, 0)

    **Cost:** O(1), constant time for date arithmetic.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Python's weekday() method: Monday=0, Tuesday=1, ..., Friday=4, Saturday=5, Sunday=6.
    # We want Friday, which is 4.
    
    # Calculate how many days to subtract to reach the previous or current Friday.
    # If today is Friday (4), (date_input.weekday() - 4 + 7) % 7 will be 0.
    # If today is Saturday (5), (5 - 4 + 7) % 7 = 1. Subtract 1 day.
    # If today is Monday (0), (0 - 4 + 7) % 7 = 3. Subtract 3 days.
    # This logic gives the number of days to go back to the *last occurrence of Friday or today if it's Friday*.
    days_to_subtract = (date_input.weekday() - 4 + 7) % 7

    previous_friday = date_input - timedelta(days=days_to_subtract)
    
    # Ensure the time is set to midnight for consistency.
    return previous_friday.replace(hour=0, minute=0, second=0, microsecond=0)


def next_weekday(date_input: datetime, target_weekday: int) -> datetime:
    """Returns the next occurrence of a specific weekday after a given date.

    Description:
        Calculates the nearest future date matching the target weekday. If the
        given date already falls on the target weekday, returns the same weekday
        of the following week.

    Args:
        date_input: The starting date.
        target_weekday: Weekday as integer (0=Monday … 6=Sunday). Constants
                        from the ``calendar`` module (e.g. ``calendar.FRIDAY``)
                        are accepted.

    Returns:
        datetime: The next occurrence at midnight.

    Raises:
        TypeError: If *date_input* is not a datetime object.
        ValueError: If *target_weekday* is not in 0‑6.

    Example:
        >>> import calendar
        >>> next_weekday(datetime(2025, 6, 9), calendar.FRIDAY)
        datetime.datetime(2025, 6, 13, 0, 0)
        >>> next_weekday(datetime(2025, 6, 13), calendar.FRIDAY)
        datetime.datetime(2025, 6, 20, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    if not isinstance(target_weekday, int) or not (0 <= target_weekday <= 6):
        raise ValueError("target_weekday must be an integer between 0 (Monday) and 6 (Sunday).")

    days_ahead = (target_weekday - date_input.weekday() + 7) % 7

    if days_ahead == 0:
        days_ahead = 7

    result = date_input + timedelta(days=days_ahead)
    return result.replace(hour=0, minute=0, second=0, microsecond=0)


def previous_weekday(date_input: datetime, target_weekday: int) -> datetime:
    """Returns the most recent occurrence of a specific weekday before a given date.

    Description:
        Calculates the nearest past date matching the target weekday. If the
        given date already falls on the target weekday, returns that same date.

    Args:
        date_input: The starting date.
        target_weekday: Weekday as integer (0=Monday … 6=Sunday).

    Returns:
        datetime: The previous (or current) occurrence at midnight.

    Raises:
        TypeError: If *date_input* is not a datetime object.
        ValueError: If *target_weekday* is not in 0‑6.

    Example:
        >>> import calendar
        >>> previous_weekday(datetime(2025, 6, 9), calendar.FRIDAY)
        datetime.datetime(2025, 6, 6, 0, 0)
        >>> previous_weekday(datetime(2025, 6, 6), calendar.FRIDAY)
        datetime.datetime(2025, 6, 6, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    if not isinstance(target_weekday, int) or not (0 <= target_weekday <= 6):
        raise ValueError("target_weekday must be an integer between 0 (Monday) and 6 (Sunday).")

    days_back = (date_input.weekday() - target_weekday + 7) % 7
    result = date_input - timedelta(days=days_back)
    return result.replace(hour=0, minute=0, second=0, microsecond=0)


def last_weekday_of_month(date_input: datetime, target_weekday: int) -> datetime:
    """Returns the last occurrence of a specific weekday in the month of a given date.

    Description:
        Finds the last day in the month that matches *target_weekday*. Useful for
        recurring schedules like "last Friday of the month".

    Args:
        date_input: Any date within the target month.
        target_weekday: Weekday as integer (0=Monday … 6=Sunday).

    Returns:
        datetime: The last matching weekday of the month at midnight.

    Raises:
        TypeError: If *date_input* is not a datetime object.
        ValueError: If *target_weekday* is not in 0‑6.

    Example:
        >>> import calendar
        >>> last_weekday_of_month(datetime(2025, 6, 1), calendar.FRIDAY)
        datetime.datetime(2025, 6, 27, 0, 0)
        >>> last_weekday_of_month(datetime(2024, 2, 10), calendar.THURSDAY)
        datetime.datetime(2024, 2, 29, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    if not isinstance(target_weekday, int) or not (0 <= target_weekday <= 6):
        raise ValueError("target_weekday must be an integer between 0 (Monday) and 6 (Sunday).")

    _, last_day_num = calendar.monthrange(date_input.year, date_input.month)
    last_date = datetime(date_input.year, date_input.month, last_day_num)
    days_back = (last_date.weekday() - target_weekday + 7) % 7
    return (last_date - timedelta(days=days_back)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )


def last_day_of_month(date_input: Union[datetime, str], input_format: str = None) -> datetime:
    """Returns the last day of the month for a given date.

    Description:
        Convenience alias for ``end_of_month`` with a more intuitive name.
        Called by ``date_sys.current_last_day_of_month``.

    Args:
        date_input: A datetime object or date string.
        input_format: Format string when *date_input* is a string.

    Returns:
        datetime: Last day of the month at end-of-day (23:59:59.999999).

    Example:
        >>> last_day_of_month(datetime(2025, 2, 10))
        datetime.datetime(2025, 2, 28, 23, 59, 59, 999999)

    Complexity: O(1)
    """
    return end_of_month(date_input, input_format)


def add_years(date_input: datetime, years: int) -> datetime:
    """Shifts a date forward or backward by a given number of years.

    Description:
        Preserves the month and day when possible. If the original date is Feb 29
        and the target year is not a leap year, clamps to Feb 28.

    Args:
        date_input: The starting datetime.
        years: Number of years to add (positive) or subtract (negative).

    Returns:
        datetime: The resulting date with time components preserved.

    Raises:
        TypeError: If *date_input* is not a datetime or *years* is not an int.

    Example:
        >>> add_years(datetime(2024, 2, 29, 10, 30), 1)
        datetime.datetime(2025, 2, 28, 10, 30)
        >>> add_years(datetime(2025, 6, 15), -3)
        datetime.datetime(2022, 6, 15, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    if not isinstance(years, int):
        raise TypeError("Input 'years' must be an integer.")

    target_year = date_input.year + years
    target_day = min(date_input.day, calendar.monthrange(target_year, date_input.month)[1])
    return date_input.replace(year=target_year, day=target_day)


def get_working_days_in_range(start_date: datetime, end_date: datetime, holidays: Optional[List[datetime]] = None) -> int:
    """Calculates the number of working days within a given date range.

    Problema/Necesidad del Usuario: Es común necesitar saber cuántos días hábiles hay
    entre dos fechas, excluyendo fines de semana y festivos definidos, para la
    planificación de proyectos, cálculo de plazos de entrega o métricas de eficiencia.

    Objetivos del Producto: Proporcionar una función precisa para la planificación
    de recursos y la contabilidad de tiempo de trabajo, lo que es crucial en entornos empresariales.

    Descripción: Esta función calcula el número de días hábiles (excluyendo sábados,
    domingos y una lista opcional de festivos) dentro de un rango de fechas dado.
    Tanto la fecha de inicio (`start_date`) como la fecha de fin (`end_date`)
    son inclusivas en el cálculo si resultan ser días hábiles.

    Args:
        start_date (datetime): La fecha de inicio del rango (inclusiva).
        end_date (datetime): La fecha de fin del rango (inclusiva).
        holidays (Optional[List[datetime]]): Una lista opcional de objetos `datetime`
                                            que representan días festivos a excluir.
                                            La parte de la hora de estos objetos no
                                            afecta la comparación, solo la fecha.

    Returns:
        int: El número total de días hábiles en el rango especificado.

    Raises:
        TypeError: Si 'start_date' o 'end_date' no son objetos datetime,
                   o si 'holidays' no es una lista de datetimes (o None).
        ValueError: Si 'start_date' es posterior a 'end_date'.

    Example:
        >>> from datetime import datetime, date

        >>> # Ejemplo 1: Rango de Lunes a Viernes sin festivos
        >>> get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 13))
        5 # Lunes 9, Martes 10, Miércoles 11, Jueves 12, Viernes 13

        >>> # Ejemplo 2: Rango que incluye un fin de semana
        >>> get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 15))
        5 # Sábado 14 y Domingo 15 son excluidos

        >>> # Ejemplo 3: Rango con festivos específicos
        >>> holiday_list = [datetime(2025, 6, 10), datetime(2025, 6, 12)] # Martes 10 y Jueves 12 son festivos
        >>> get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 13), holidays=holiday_list)
        3 # Días hábiles: Lunes 9, Miércoles 11, Viernes 13

        >>> # Ejemplo 4: Rango de un solo día (que es un fin de semana)
        >>> get_working_days_in_range(datetime(2025, 6, 14), datetime(2025, 6, 14)) # Sábado 14
        0

        >>> # Ejemplo 5: Rango de un solo día (que es un día hábil)
        >>> get_working_days_in_range(datetime(2025, 6, 11), datetime(2025, 6, 11)) # Miércoles 11
        1

        >>> # start_date después de end_date (levantará ValueError)
        >>> try:
        >>>     get_working_days_in_range(datetime(2025, 6, 13), datetime(2025, 6, 9))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: start_date cannot be after end_date.

        >>> # Lista de festivos con elemento no datetime (levantará TypeError)
        >>> try:
        >>>     get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 13), holidays=[datetime(2025, 6, 10), "not_a_date"])
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: All items in 'holidays' list must be datetime objects.

    **Cost:** O(n), where n is the number of days between start_date and end_date.
    """
    # 1. Validación de entradas
    if not isinstance(start_date, datetime):
        raise TypeError("Input 'start_date' must be a datetime object.")
    if not isinstance(end_date, datetime):
        raise TypeError("Input 'end_date' must be a datetime object.")
    if start_date > end_date:
        raise ValueError("start_date cannot be after end_date.")

    # Convertir la lista de festivos a un conjunto de objetos `date` para una
    # búsqueda eficiente (complejidad de tiempo promedio O(1)).
    # También se valida que los elementos de la lista `holidays` sean objetos datetime.
    holiday_set: Set[date] = set()
    if holidays is not None:
        if not isinstance(holidays, list):
            raise TypeError("Input 'holidays' must be a list of datetime objects or None.")
        for h in holidays:
            if not isinstance(h, datetime):
                raise TypeError("All items in 'holidays' list must be datetime objects.")
            holiday_set.add(h.date()) # Se añade solo la parte de la fecha para la comparación

    working_days_count = 0
    
    # Se inicializa `current_date` con solo la parte de la fecha para evitar problemas
    # de comparación con la hora si las fechas de inicio/fin tienen componentes de tiempo.
    current_date = start_date.date()
    end_date_only = end_date.date()

    # Iterar día por día desde `start_date` hasta `end_date` (ambos inclusive)
    while current_date <= end_date_only:
        # `datetime.weekday()` devuelve un entero donde 0 es Lunes y 6 es Domingo.
        # Los días de semana son 0 (Lunes) a 4 (Viernes).
        if current_date.weekday() < 5:
            # Si el día actual no es un fin de semana, verificar si es un día festivo
            if current_date not in holiday_set:
                working_days_count += 1
        
        # Moverse al siguiente día en el rango
        current_date += timedelta(days=1)

    return working_days_count


def get_first_business_day_of_month(year: int, month: int, holidays: Optional[List[datetime]] = None) -> datetime:
    """Devuelve el primer día hábil de un mes y año dados, considerando fines de semana y una lista opcional de festivos.

    Problema/Necesidad del Usuario: Muchas operaciones financieras, pagos o inicios
    de ciclo de informes se basan en el primer día hábil de un mes.

    Objetivos del Producto: Proporcionar una función precisa para la planificación
    de recursos y la contabilidad de tiempo de trabajo, lo que es crucial en entornos empresariales.

    Descripción: Esta función calcula y devuelve el primer día laborable (excluyendo
    sábados, domingos y una lista opcional de festivos) de un mes y año específicos.
    La fecha devuelta tendrá su componente de tiempo establecido a medianoche (00:00:00).

    Args:
        year (int): El año para el cual se desea obtener el primer día hábil.
        month (int): El mes (1-12) para el cual se desea obtener el primer día hábil.
        holidays (Optional[List[datetime]]): Una lista opcional de objetos `datetime`
                                            que representan días festivos a excluir.
                                            La parte de la hora de estos objetos no
                                            afecta la comparación, solo la fecha.

    Returns:
        datetime: Un objeto `datetime` que representa el primer día hábil del mes.

    Raises:
        TypeError: Si 'year' o 'month' no son enteros, o si 'holidays' no es una
                   lista de datetimes (o None).
        ValueError: Si 'year' está fuera del rango válido (1-9999), o si 'month'
                    no está entre 1 y 12.

    Example:
        >>> from datetime import datetime, date

        >>> # Ejemplo 1: Enero 2025 (1 de enero es Miércoles)
        >>> get_first_business_day_of_month(2025, 1)
        datetime.datetime(2025, 1, 1, 0, 0) # El 1 de enero de 2025 es un Miércoles.

        >>> # Ejemplo 2: Marzo 2025 (1 de marzo es Sábado)
        >>> get_first_business_day_of_month(2025, 3)
        datetime.datetime(2025, 3, 3, 0, 0) # El 1 y 2 de marzo son Sábado y Domingo. El 3 de marzo es Lunes.

        >>> # Ejemplo 3: Diciembre 2025 (1 de diciembre es Lunes, pero si fuera festivo)
        >>> # Asumiendo que el 1 y 2 de diciembre de 2025 son festivos.
        >>> custom_holidays = [datetime(2025, 12, 1), datetime(2025, 12, 2)]
        >>> get_first_business_day_of_month(2025, 12, holidays=custom_holidays)
        datetime.datetime(2025, 12, 3, 0, 0) # El 1 y 2 de dic son festivos. El 3 de dic es Miércoles.

        >>> # Mes inválido (levantará ValueError)
        >>> try:
        >>>     get_first_business_day_of_month(2025, 13)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Month must be between 1 and 12.

    **Cost:** O(1), constant time for finding first business day (typically requires checking only a few days).
    """
    # 1. Validación de entradas
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if not isinstance(month, int):
        raise TypeError("Input 'month' must be an integer.")
    if not (1 <= year <= 9999): # Rango común de años para objetos datetime
        raise ValueError("Year is out of valid range (1-9999).")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")

    # Convertir la lista de festivos a un conjunto de objetos `date` para una
    # búsqueda eficiente (complejidad de tiempo promedio O(1)).
    holiday_set: Set[date] = set()
    if holidays is not None:
        if not isinstance(holidays, list):
            raise TypeError("Input 'holidays' must be a list of datetime objects or None.")
        for h in holidays:
            if not isinstance(h, datetime):
                raise TypeError("All items in 'holidays' list must be datetime objects.")
            holiday_set.add(h.date()) # Se añade solo la parte de la fecha para la comparación

    # Empezar desde el primer día del mes
    current_date = datetime(year, month, 1)

    # Iterar día por día hasta encontrar el primer día hábil
    while True:
        current_date_only = current_date.date() # Obtener solo la parte de la fecha

        # `datetime.weekday()` devuelve un entero donde 0 es Lunes y 6 es Domingo.
        # Los días de semana son 0 (Lunes) a 4 (Viernes).
        is_weekend = current_date_only.weekday() >= 5 # Es Sábado (5) o Domingo (6)
        
        # Verificar si el día actual es un día festivo
        is_holiday = current_date_only in holiday_set

        # Si no es fin de semana y no es festivo, hemos encontrado el primer día hábil
        if not is_weekend and not is_holiday:
            # Devolver la fecha con la hora a medianoche para consistencia
            return current_date.replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Si no es un día hábil, avanzar al siguiente día
        current_date += timedelta(days=1)


def get_last_business_day_of_month(year: int, month: int, holidays: Optional[List[datetime]] = None) -> datetime:
    """Devuelve el último día hábil de un mes y año dados, considerando fines de semana y una lista opcional de festivos.

    Problema/Necesidad del Usuario: Muchas operaciones financieras, cierres de período,
    o plazos de informes se basan en el último día hábil de un mes.

    Descripción: Esta función calcula y devuelve el último día laborable (excluyendo
    sábados, domingos y una lista opcional de festivos) de un mes y año específicos.
    La fecha devuelta tendrá su componente de tiempo establecido a medianoche (00:00:00).

    Args:
        year (int): El año para el cual se desea obtener el último día hábil.
        month (int): El mes (1-12) para el cual se desea obtener el último día hábil.
        holidays (Optional[List[datetime]]): Una lista opcional de objetos `datetime`
                                            que representan días festivos a excluir.
                                            La parte de la hora de estos objetos no
                                            afecta la comparación, solo la fecha.

    Returns:
        datetime: Un objeto `datetime` que representa el último día hábil del mes.

    Raises:
        TypeError: Si 'year' o 'month' no son enteros, o si 'holidays' no es una
                   lista de datetimes (o None).
        ValueError: Si 'year' está fuera del rango válido (1-9999), o si 'month'
                    no está entre 1 y 12.

    Example:
        >>> from datetime import datetime, date
        >>> import calendar

        >>> # Ejemplo 1: Junio 2025 (30 de junio es Lunes)
        >>> get_last_business_day_of_month(2025, 6)
        datetime.datetime(2025, 6, 30, 0, 0) # El 30 de junio de 2025 es un Lunes.

        >>> # Ejemplo 2: Mayo 2025 (31 de mayo es Sábado)
        >>> get_last_business_day_of_month(2025, 5)
        datetime.datetime(2025, 5, 30, 0, 0) # El 31 de mayo es Sábado, el 30 de mayo es Viernes.

        >>> # Ejemplo 3: Enero 2025 (31 de enero es Viernes, pero si fuera festivo)
        >>> # Asumiendo que el 31 de enero de 2025 es un festivo.
        >>> custom_holidays = [datetime(2025, 1, 31)]
        >>> get_last_business_day_of_month(2025, 1, holidays=custom_holidays)
        datetime.datetime(2025, 1, 30, 0, 0) # El 31 de enero es festivo, el 30 de enero es Jueves.

        >>> # Mes inválido (levantará ValueError)
        >>> try:
        >>>     get_last_business_day_of_month(2025, 0)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Month must be between 1 and 12.

    **Cost:** O(1), constant time for finding last business day (typically requires checking only a few days).
    """
    # 1. Validación de entradas
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    if not isinstance(month, int):
        raise TypeError("Input 'month' must be an integer.")
    if not (1 <= year <= 9999): # Rango común de años para objetos datetime
        raise ValueError("Year is out of valid range (1-9999).")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")

    # Convertir la lista de festivos a un conjunto de objetos `date` para una
    # búsqueda eficiente (complejidad de tiempo promedio O(1)).
    holiday_set: Set[date] = set()
    if holidays is not None:
        if not isinstance(holidays, list):
            raise TypeError("Input 'holidays' must be a list of datetime objects or None.")
        for h in holidays:
            if not isinstance(h, datetime):
                raise TypeError("All items in 'holidays' list must be datetime objects.")
            holiday_set.add(h.date()) # Se añade solo la parte de la fecha para la comparación

    # Obtener el último día del mes
    last_day_of_month_num = calendar.monthrange(year, month)[1]
    current_date = datetime(year, month, last_day_of_month_num)

    # Iterar día por día hacia atrás hasta encontrar el último día hábil
    while True:
        current_date_only = current_date.date() # Obtener solo la parte de la fecha

        # `datetime.weekday()` devuelve un entero donde 0 es Lunes y 6 es Domingo.
        # Los días de semana son 0 (Lunes) a 4 (Viernes).
        is_weekend = current_date_only.weekday() >= 5 # Es Sábado (5) o Domingo (6)
        
        # Verificar si el día actual es un día festivo
        is_holiday = current_date_only in holiday_set

        # Si no es fin de semana y no es festivo, hemos encontrado el último día hábil
        if not is_weekend and not is_holiday:
            # Devolver la fecha con la hora a medianoche para consistencia
            return current_date.replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Si no es un día hábil, retroceder al día anterior
        current_date -= timedelta(days=1)


def is_working_day(
    date_input: Union[datetime, str],
    input_format: str = None,
    system: Literal['european', 'anglo'] = 'european'
) -> bool:
    """Checks if a given date is a working day (Monday to Friday) based on the specified week numbering system.

    This function determines if a date falls on a weekday (Monday through Friday),
    allowing for the consideration of different week numbering systems.
    The definition of working days (Monday-Friday) remains consistent across systems,
    but their numerical representation differs.

    Args:
        date_input (Union[datetime, str]): The date to check.
                                            Can be a datetime object (e.g., `datetime(2025, 6, 9)`)
                                            or a string (e.g., `"09/06/2025"`).
        input_format (str, optional): The format code string for `date_input` if it's a string.
                                      This is **required** if `date_input` is a string.
                                      Example: `'%d/%m/%Y'` for `"09/06/2025"`.
                                      Not used if `date_input` is a `datetime` object.
        system (Literal['european', 'anglo'], optional): The week numbering system to use for
                                                                interpreting the day of the week.
                                                                - `'european'`: Monday is 0, Tuesday is 1, ..., Sunday is 6.
                                                                  (Matches `datetime.weekday()`)
                                                                - `'anglo'`: Sunday is 0, Monday is 1, ..., Saturday is 6.
                                                                  (Matches `datetime.strftime('%w')`)
                                                                Defaults to `'european'`.

    Returns:
        bool: `True` if the date is a working day (Monday-Friday), `False` otherwise.

    Raises:
        TypeError: If `date_input` is not a `datetime` object or a string.
        ValueError: If `date_input` is a string and `input_format` is not provided,
                    or if the string cannot be parsed with the given format.
                    If an unsupported `system` value is provided.

    Example:
        >>> from datetime import datetime

        >>> # A Monday (June 9, 2025, was a Monday)
        >>> is_working_day(datetime(2025, 6, 9), system='european') # Monday = 0 in European system
        True
        >>> is_working_day(datetime(2025, 6, 9), system='anglo') # Monday = 1 in anglo system
        True

        >>> # A Saturday (June 14, 2025, will be a Saturday)
        >>> is_working_day(datetime(2025, 6, 14), system='european') # Saturday = 5 in European system
        False
        >>> is_working_day(datetime(2025, 6, 14), system='anglo') # Saturday = 6 in anglo system
        False

        >>> # Using string input for a Thursday (June 12, 2025, will be a Thursday)
        >>> is_working_day("12/06/2025", "%d/%m/%Y", system='european')
        True
        >>> is_working_day("12/06/2025", "%d/%m/%Y", system='anglo')
        True

    **Cost:** O(1), constant time for weekday calculation and comparison.
    """
    # 1. Parse the input into a datetime object
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # 2. Determine the weekday number and the set of working days based on the specified system
    weekday_number: int
    working_days_set: set[int]

    if system == 'european':
        # Python's datetime.weekday() method aligns with the European standard:
        # Monday=0, Tuesday=1, Wednesday=2, Thursday=3, Friday=4, Saturday=5, Sunday=6.
        weekday_number = parsed_dt.weekday()
        # Working days are Monday through Friday.
        working_days_set = {0, 1, 2, 3, 4}
    elif system == 'anglo':
        # The strftime('%w') format code aligns with the anglo/US standard:
        # Sunday=0, Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5, Saturday=6.
        # We convert it to an integer because strftime returns a string.
        weekday_number = int(parsed_dt.strftime('%w'))
        # Working days are Monday through Friday.
        working_days_set = {1, 2, 3, 4, 5}
    else:
        # Raise an error if an unsupported system is provided.
        raise ValueError("Invalid 'system' parameter. Must be 'european' or 'anglo'.")

    # 3. Check if the determined weekday number is within the set of working days.
    return weekday_number in working_days_set


def is_weekend(date_input: Union[datetime, str], input_format: str = None, language: str = 'en') -> bool:
    """Determines if a given date is a Saturday or a Sunday.

    This function accepts either a datetime object or a date string.
    If a string is provided, its format must be specified. The 'language' parameter
    is primarily for internal use or future expansion related to locale-specific
    date processing, though the function itself returns a boolean indicating weekend status.

    Args:
        date_input (Union[datetime, str]): The date to check.
                                            Can be a datetime object (e.g., datetime(2023, 10, 28))
                                            or a string (e.g., "28/10/2023").
        input_format (str, optional): The format code string for 'date_input' if it's a string.
                                      Required if 'date_input' is a string.
                                      E.g., '%d/%m/%Y' for "28/10/2023".
                                      Not used if 'date_input' is a datetime object.
        language (str, optional): The two-letter ISO 639-1 language code (e.g., 'en', 'es', 'fr', 'de').
                                  This parameter is available for consistency with other date functions
                                  that use locales, but it doesn't directly affect the boolean output
                                  of this specific function. Defaults to 'en'.

    Returns:
        bool: True if the date is a Saturday or Sunday, False otherwise.

    Raises:
        TypeError: If 'date_input' is not a datetime object or a string.
        ValueError: If 'date_input' is a string and 'input_format' is not provided,
                    or if the string cannot be parsed with the given format.
                    Also, if the specified 'language' cannot be set as a locale on your system.

    Example:
        >>> from datetime import datetime

        >>> # Saturday (using datetime object)
        >>> is_weekend(datetime(2023, 10, 28))
        True

        >>> # Sunday (using datetime object)
        >>> is_weekend(datetime(2023, 10, 29))
        True

        >>> # Friday (using datetime object)
        >>> is_weekend(datetime(2023, 10, 27))
        False

        >>> # Saturday (using a string input with format)
        >>> is_weekend("28/10/2023", "%d/%m/%Y")
        True

        >>> # Monday (using a string input with format)
        >>> is_weekend("30-10-2023", "%d-%m-%Y")
        False

        >>> # Using 'es' language (parameter included, but output is still boolean)
        >>> is_weekend(datetime(2023, 10, 28), language='es')
        True

    **Cost:** O(1), constant time for weekday check.
    """
    # Ensure the input is a datetime object, parsing from string if necessary.
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Store the current locale settings to restore them later.
    original_locale = locale.getlocale(locale.LC_TIME)
    
    # Attempt to set the locale for potential future use or consistency,
    # though it doesn't directly impact the `weekday()` method's integer return.
    try:
        locale.setlocale(locale.LC_TIME, language + '.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, language)
        except locale.Error:
            raise ValueError(
                f"Unable to set locale for language '{language}'. "
                "This typically means the required language pack is not installed on your operating system, "
                "or the locale name is different. "
                "On Linux/macOS, check 'locale -a'. On Windows, check 'Control Panel -> Region'."
            )
    
    try:
        # In Python's datetime, .weekday() returns:
        # Monday = 0, ..., Friday = 4, Saturday = 5, Sunday = 6.
        # So, Saturday and Sunday correspond to 5 and 6 respectively.
        return parsed_dt.weekday() in [5, 6]
    finally:
        # Always restore the original locale to prevent global side effects.
        locale.setlocale(locale.LC_TIME, original_locale)


def get_age_from_dob(
    dob: Union[datetime, str],
    dob_format: str = None,
    as_of_date: Optional[datetime] = None
) -> int:
    """Calculates the age in full years from a date of birth.

    Problem/User Need: Calculating age is a very common operation in applications
    with user profiles, registration systems, or age requirements.

    Product Goals: Simplify a common date calculation that often has nuances
    (e.g., past or future birthdays) and can be prone to errors if implemented manually.

    Description: Given a date of birth (dob) and an optional reference date
    (defaults to the current date if not provided), this function calculates
    the age in complete years. It correctly handles cases where the birthday
    has not yet occurred in the reference year.

    Args:
        dob (Union[datetime, str]): The date of birth. Can be a datetime object
                                    or a string.
        dob_format (str, optional): The format code string for `dob` if it's a string.
                                    This is **required** if `dob` is a string.
                                    Example: `'%Y-%m-%d'` for `"1990-06-11"`.
        as_of_date (Optional[datetime], optional): The reference date to calculate the age against.
                                                   If `None`, the current UTC date is used.
                                                   It should preferably be a date-only (time at 00:00:00)
                                                   or timezone-aware for consistency.

    Returns:
        int: The age in full years.

    Raises:
        TypeError: If `dob` is not a datetime object or a string, or if `as_of_date`
                   is provided and is not a datetime object.
        ValueError: If `dob` is a string and `dob_format` is not provided,
                    or if the string cannot be parsed with the given format.
                    If `dob` is in the future relative to `as_of_date`.

    Example:
        >>> from datetime import datetime, timezone

        >>> # Birthday on the same day as reference date
        >>> get_age_from_dob(datetime(1990, 6, 11), as_of_date=datetime(2025, 6, 11))
        35

        >>> # Birthday has already passed in the reference year
        >>> get_age_from_dob(datetime(1990, 1, 15), as_of_date=datetime(2025, 6, 11))
        35

        >>> # Birthday has NOT yet passed in the reference year
        >>> get_age_from_dob(datetime(1990, 12, 25), as_of_date=datetime(2025, 6, 11))
        34

        >>> # Using current date as reference (assumes current date is 2025-06-11 UTC)
        >>> # Actual result will vary based on current system date.
        >>> get_age_from_dob(datetime(1990, 6, 11))
        35

        >>> # Using string input for date of birth
        >>> get_age_from_dob("1985-03-20", dob_format="%Y-%m-%d", as_of_date=datetime(2025, 6, 11))
        40

        >>> # Date of birth in the future (will raise ValueError)
        >>> try:
        >>>     get_age_from_dob(datetime(2030, 1, 1), as_of_date=datetime(2025, 1, 1))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Date of birth cannot be in the future relative to the reference date.

    **Cost:** O(1), constant time for date arithmetic and comparison.
    """
    # 1. Parse the date of birth (dob) into a datetime object
    parsed_dob: datetime
    if isinstance(dob, str):
        if dob_format is None:
            raise ValueError("'dob_format' is required when 'dob' is a string.")
        try:
            parsed_dob = datetime.strptime(dob, dob_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{dob}' with format '{dob_format}'. Error: {e}") from e
    elif isinstance(dob, datetime):
        parsed_dob = dob
    else:
        raise TypeError("Input 'dob' must be a datetime object or a string.")

    # 2. Determine the reference date (as_of_date)
    reference_date: datetime
    if as_of_date is None:
        # Use current UTC date if no reference date is provided.
        # Using UTC for consistency, but if local time is preferred, remove tzinfo=timezone.utc.
        reference_date = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    elif isinstance(as_of_date, datetime):
        reference_date = as_of_date
    else:
        raise TypeError("Input 'as_of_date' must be a datetime object or None.")

    # Ensure parsed_dob is not in the future relative to reference_date
    if parsed_dob > reference_date:
        raise ValueError("Date of birth cannot be in the future relative to the reference date.")

    # 3. Calculate age in full years
    # Start by assuming the difference in years.
    age = reference_date.year - parsed_dob.year

    # Adjust age if the birthday hasn't occurred yet in the current year.
    # We compare the (month, day) of the DOB with the (month, day) of the reference date.
    if (parsed_dob.month, parsed_dob.day) > (reference_date.month, reference_date.day):
        age -= 1

    return age


# Reutilizamos la función auxiliar interna para parsear la entrada de fecha
def _parse_date_input_internal(date_val: Union[datetime, str], input_format: Optional[str]) -> datetime:
    if isinstance(date_val, str):
        if input_format is None:
            raise ValueError("'format' is required when 'date_input' is a string for parsing.")
        try:
            return datetime.strptime(date_val, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_val}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_val, datetime):
        return date_val
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")


def get_season(
    date_input: Union[datetime, str],
    hemisphere: str = 'northern',
    lang: str = 'en',
    format: Optional[str] = None
) -> str:
    """Dada una fecha, devuelve la estación del año en el idioma especificado para el hemisferio indicado.

    Problema/Necesidad del Usuario: Además de identificar la estación según el hemisferio,
    es fundamental que la respuesta se adapte al idioma del usuario y, potencialmente,
    a su localización para convenciones predeterminadas.

    Objetivos del Producto: Proporcionar una función de contextualización de fechas
    más completa, que sea útil para aplicaciones globales que requieran respuestas
    localizadas y precisas estacionalmente.

    Descripción: Esta función toma una fecha, un hemisferio ('northern' o 'southern'),
    y un código de idioma (ej. 'en' para inglés, 'es' para español). Devuelve el nombre
    de la estación meteorológica correspondiente. Las estaciones meteorológicas se definen
    por meses completos:
    - Hemisferio Norte: Primavera (Mar-May), Verano (Jun-Ago), Otoño (Sep-Nov), Invierno (Dic-Feb).
    - Hemisferio Sur: Otoño (Mar-May), Invierno (Jun-Ago), Primavera (Sep-Nov), Verano (Dic-Feb).

    Args:
        date_input (Union[datetime, str]): La fecha para la cual se desea obtener la estación.
                                            Puede ser un objeto `datetime` o una cadena de fecha.
        hemisphere (str, optional): El hemisferio para el cálculo de la estación.
                                     Puede ser 'northern' (hemisferio norte) o 'southern'
                                     (hemisferio sur). No es sensible a mayúsculas/minúsculas.
                                     Por defecto es 'northern'.
        lang (str, optional): El código de idioma para la respuesta (ej. 'en', 'es').
                               Por defecto es 'en' (inglés).
        format (str, optional): El formato de cadena de fecha (ej. '%Y-%m-%d')
                                  si 'date_input' es una cadena. Es **obligatorio**
                                  si 'date_input' es una cadena.

    Returns:
        str: El nombre de la estación en el idioma especificado.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o una cadena,
                   o si 'hemisphere' o 'lang' no son cadenas.
        ValueError: Si 'hemisphere' no es 'northern' ni 'southern',
                    si 'lang' no es un idioma soportado,
                    o si 'format' es `None` y 'date_input' es una cadena,
                    o si la cadena de fecha no puede ser parseada.

    Example:
        >>> from datetime import datetime

        >>> # 1. Verano en el Hemisferio Norte (inglés)
        >>> get_season(datetime(2025, 6, 11), 'northern', lang='en')
        'Summer'

        >>> # 2. Invierno en el Hemisferio Sur (español)
        >>> get_season(datetime(2025, 6, 11), 'southern', lang='es')
        'Invierno'

        >>> # 3. Otoño en el Hemisferio Norte (español, desde cadena)
        >>> get_season("2025-09-20", 'northern', lang='es', format="%Y-%m-%d")
        'Otoño'

        >>> # 4. Hemisferio inválido (levantará ValueError)
        >>> try:
        >>>     get_season(datetime(2025, 6, 11), 'equator', lang='en')
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Invalid hemisphere. Must be 'northern' or 'southern'.

        >>> # 5. Idioma no soportado (levantará ValueError)
        >>> try:
        >>>     get_season(datetime(2025, 6, 11), 'northern', lang='fr')
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Unsupported language. Supported languages are: en, es.

    **Cost:** O(1), constant time for date parsing and season determination.
    """
    # 1. Parsear la fecha de entrada
    parsed_date = _parse_date_input_internal(date_input, format)
    
    # 2. Validar el hemisferio
    hemisphere_lower = hemisphere.lower()
    if hemisphere_lower not in ['northern', 'southern']:
        raise ValueError("Invalid hemisphere. Must be 'northern' or 'southern'.")

    # 3. Mapeo de nombres de estaciones por idioma
    # Puedes añadir más idiomas aquí si es necesario.
    season_names = {
        'en': {
            'spring': 'Spring',
            'summer': 'Summer',
            'autumn': 'Autumn',
            'winter': 'Winter'
        },
        'es': {
            'spring': 'Primavera',
            'summer': 'Verano',
            'autumn': 'Otoño',
            'winter': 'Invierno'
        }
    }

    # 4. Validar y obtener los nombres de las estaciones para el idioma solicitado
    lang_lower = lang.lower()
    if lang_lower not in season_names:
        raise ValueError(f"Unsupported language. Supported languages are: {', '.join(season_names.keys())}.")
    
    current_season_names = season_names[lang_lower]

    month = parsed_date.month

    # 5. Determinar la estación según el hemisferio y el mes (definición meteorológica)
    season_key: str
    if hemisphere_lower == 'northern':
        if 3 <= month <= 5: # Marzo, Abril, Mayo
            season_key = 'spring'
        elif 6 <= month <= 8: # Junio, Julio, Agosto
            season_key = 'summer'
        elif 9 <= month <= 11: # Septiembre, Octubre, Noviembre
            season_key = 'autumn'
        else: # Diciembre, Enero, Febrero (envuelve el fin de año)
            season_key = 'winter'
    else: # hemisferio sur
        if 9 <= month <= 11: # Septiembre, Octubre, Noviembre
            season_key = 'spring'
        elif 12 == month or 1 <= month <= 2: # Diciembre, Enero, Febrero (envuelve el fin de año)
            season_key = 'summer'
        elif 3 <= month <= 5: # Marzo, Abril, Mayo
            season_key = 'autumn'
        else: # Junio, Julio, Agosto
            season_key = 'winter'
            
    return current_season_names[season_key]


def format_datetime_ampm(dt_object: datetime) -> str:
    """
    Formats a datetime object into a 12-hour (AM/PM) string representation.

    This function takes a datetime object and converts it into a string
    formatted as 'YYYY-MM-DD HH:MM:SS AM/PM'. This is a common and clear
    way to display time with an AM/PM indicator.

    Args:
        dt_object (datetime.datetime): The datetime object to format.

    Returns:
        str: A string representing the datetime object in AM/PM format.

    Raises:
        TypeError: If the input dt_object is not a datetime.datetime object.

    Example of use:
        >>> from datetime import datetime
        >>> now = datetime(2025, 6, 29, 15, 30, 0)
        >>> format_datetime_ampm(now)
        '2025-06-29 03:30:00 PM'

        >>> morning = datetime(2025, 6, 29, 9, 15, 45)
        >>> format_datetime_ampm(morning)
        '2025-06-29 09:15:45 AM'

    **Cost:** O(1), constant time for string formatting.
    """
    if not isinstance(dt_object, datetime.datetime):
        raise TypeError("The input must be a datetime.datetime object.")

    # Use strftime to format the datetime object.
    # %Y: Year with century as a decimal number.
    # %m: Month as a zero-padded decimal number.
    # %d: Day of the month as a zero-padded decimal number.
    # %I: Hour (12-hour clock) as a zero-padded decimal number.
    # %M: Minute as a zero-padded decimal number.
    # %S: Second as a zero-padded decimal number.
    # %p: Locale’s equivalent of either AM or PM.
    formatted_string = dt_object.strftime("%Y-%m-%d %I:%M:%S %p")

    return formatted_string


def timedelta_to_components(timedelta_obj: timedelta) -> Dict[str, Union[int, float]]:
    """Convierte un objeto timedelta de Python en un diccionario con sus componentes.

    Problema/Necesidad del Usuario: Cuando calculamos diferencias entre fechas,
    obtenemos un objeto timedelta. A menudo, los usuarios necesitan desglosar
    este timedelta en componentes más legibles (días, horas, minutos, segundos)
    para mostrarlos en la UI o para realizar cálculos adicionales.

    Objetivos del Producto: Mejorar la legibilidad y la manipulación de los
    resultados de diferencias de tiempo, haciéndolos más accesibles para la
    presentación al usuario o para la lógica de negocio.

    Descripción: Dada un objeto `timedelta`, esta función lo descompone en
    días, las horas restantes, los minutos restantes, los segundos restantes,
    y los microsegundos restantes, y los devuelve en un diccionario. La función
    maneja correctamente los `timedelta` positivos y negativos, aplicando el
    signo correspondiente a cada componente.

    Args:
        timedelta_obj (timedelta): El objeto `timedelta` a convertir.

    Returns:
        Dict[str, Union[int, float]]: Un diccionario con las claves:
                                      'days', 'hours', 'minutes', 'seconds', 'microseconds'.
                                      Todos los valores son enteros y reflejan el signo
                                      general del `timedelta`.

    Raises:
        TypeError: Si 'timedelta_obj' no es un objeto `datetime.timedelta`.

    Example:
        >>> # Ejemplo 1: Diferencia positiva (1 día, 1 hora, 30 minutos)
        >>> dt_future = datetime(2025, 6, 12, 10, 0, 0)
        >>> dt_past = datetime(2025, 6, 11, 8, 30, 0)
        >>> td_positive = dt_future - dt_past # Esto resulta en timedelta(days=1, seconds=5400)
        >>> timedelta_to_components(td_positive)
        {'days': 1, 'hours': 1, 'minutes': 30, 'seconds': 0, 'microseconds': 0}

        >>> # Ejemplo 2: Diferencia negativa (1 día, 1 hora, 30 minutos antes)
        >>> td_negative = dt_past - dt_future # Esto es -1 día, -1 hora, -30 minutos
        >>> timedelta_to_components(td_negative)
        {'days': -1, 'hours': -1, 'minutes': -30, 'seconds': 0, 'microseconds': 0}

        >>> # Ejemplo 3: Solo segundos y microsegundos
        >>> td_small = timedelta(seconds=123, microseconds=456789)
        >>> timedelta_to_components(td_small)
        {'days': 0, 'hours': 0, 'minutes': 2, 'seconds': 3, 'microseconds': 456789}

        >>> # Ejemplo 4: Un timedelta con microsegundos exactos
        >>> td_micro = timedelta(microseconds=500)
        >>> timedelta_to_components(td_micro)
        {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0, 'microseconds': 500}

        >>> # Ejemplo 5: Entrada inválida (levantará TypeError)
        >>> try:
        >>>     timedelta_to_components("5 days")
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Input 'timedelta_obj' must be a datetime.timedelta object.
    """
    if not isinstance(timedelta_obj, timedelta):
        raise TypeError("Input 'timedelta_obj' must be a datetime.timedelta object.")

    # Obtener el valor total del timedelta en segundos como un flotante.
    # Esto es crucial porque total_seconds() maneja el signo correctamente.
    total_seconds_float = timedelta_obj.total_seconds()

    # Determinar el signo general del timedelta.
    # Esto se aplicará a todos los componentes para una representación consistente.
    sign = -1 if total_seconds_float < 0 else 1

    # Trabajar con el valor absoluto de los segundos totales para extraer los componentes,
    # y luego aplicar el signo al final.
    abs_total_seconds = abs(total_seconds_float)

    # Extraer días (partes enteras de 24 horas)
    days = int(abs_total_seconds // (24 * 3600))
    
    # Calcular los segundos restantes después de extraer los días completos
    remaining_seconds_after_days = abs_total_seconds % (24 * 3600)

    # Extraer horas, minutos y segundos de los segundos restantes
    hours = int(remaining_seconds_after_days // 3600)
    remaining_seconds_after_hours = remaining_seconds_after_days % 3600

    minutes = int(remaining_seconds_after_hours // 60)
    seconds = int(remaining_seconds_after_hours % 60)
    
    # Los microsegundos son la parte fraccionaria de los segundos restantes.
    # Se redondea para manejar posibles imprecisiones de flotantes.
    microseconds = int(round((remaining_seconds_after_hours % 1) * 1_000_000))

    # Aplicar el signo original a todos los componentes para que el diccionario
    # refleje la dirección (positiva o negativa) del timedelta.
    return {
        'days': days * sign,
        'hours': hours * sign,
        'minutes': minutes * sign,
        'seconds': seconds * sign,
        'microseconds': microseconds * sign
    }


def intersection_of_date_ranges(start1: datetime, end1: datetime, start2: datetime, end2: datetime) -> Optional[Tuple[datetime, datetime]]:
    """Si dos rangos de fechas se solapan, devuelve una tupla con las fechas de inicio y fin del período de intersección.
    Si no hay solapamiento, devuelve None.

    Problema/Necesidad del Usuario: Si dos rangos se superponen, a menudo es necesario saber cuál es el período
    de tiempo común entre ellos. Útil para análisis de concurrencia o cálculo de duraciones compartidas.

    Objetivos del Producto: Extender la funcionalidad de detección de solapamientos para proporcionar el
    rango exacto de la superposición, lo que permite cálculos más precisos y lógica de negocio avanzada.

    Descripción: Esta función toma cuatro objetos `datetime` que definen dos rangos de fechas:
    [start1, end1] y [start2, end2]. Determina si estos rangos se superponen y, si lo hacen,
    devuelve un nuevo rango `(datetime, datetime)` que representa la intersección.
    Si los rangos solo se tocan en un punto (ej. [A, B] y [B, C]), el punto de contacto
    (B, B) se considera la intersección.

    Args:
        start1 (datetime): Fecha y hora de inicio del primer rango.
        end1 (datetime): Fecha y hora de fin del primer rango.
        start2 (datetime): Fecha y hora de inicio del segundo rango.
        end2 (datetime): Fecha y hora de fin del segundo rango.

    Returns:
        Optional[Tuple[datetime, datetime]]: Una tupla `(start_intersection, end_intersection)`
                                              si hay solapamiento, o `None` si no lo hay.

    Raises:
        TypeError: Si alguno de los argumentos no es un objeto `datetime`.
        ValueError: Si `start1 > end1` o `start2 > end2` (rangos invertidos).

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Rangos con solapamiento (superposición parcial)
        >>> r1_start = datetime(2025, 6, 10, 10, 0, 0)
        >>> r1_end = datetime(2025, 6, 15, 10, 0, 0)
        >>> r2_start = datetime(2025, 6, 13, 10, 0, 0)
        >>> r2_end = datetime(2025, 6, 18, 10, 0, 0)
        >>> intersection_of_date_ranges(r1_start, r1_end, r2_start, r2_end)
        (datetime.datetime(2025, 6, 13, 10, 0), datetime.datetime(2025, 6, 15, 10, 0))

        >>> # Ejemplo 2: Un rango contenido completamente en otro
        >>> r1_start = datetime(2025, 1, 1)
        >>> r1_end = datetime(2025, 1, 31)
        >>> r2_start = datetime(2025, 1, 10)
        >>> r2_end = datetime(2025, 1, 20)
        >>> intersection_of_date_ranges(r1_start, r1_end, r2_start, r2_end)
        (datetime.datetime(2025, 1, 10, 0, 0), datetime.datetime(2025, 1, 20, 0, 0))

        >>> # Ejemplo 3: Rangos que no se solapan (rango1 antes de rango2)
        >>> r1_start = datetime(2025, 2, 1)
        >>> r1_end = datetime(2025, 2, 10)
        >>> r2_start = datetime(2025, 2, 15)
        >>> r2_end = datetime(2025, 2, 20)
        >>> intersection_of_date_ranges(r1_start, r1_end, r2_start, r2_end) is None
        True

        >>> # Ejemplo 4: Rangos que solo se tocan en un punto
        >>> r1_start = datetime(2025, 3, 1)
        >>> r1_end = datetime(2025, 3, 5)
        >>> r2_start = datetime(2025, 3, 5)
        >>> r2_end = datetime(2025, 3, 10)
        >>> intersection_of_date_ranges(r1_start, r1_end, r2_start, r2_end)
        (datetime.datetime(2025, 3, 5, 0, 0), datetime.datetime(2025, 3, 5, 0, 0))

        >>> # Ejemplo 5: Rangos inválidos (inicio > fin)
        >>> try:
        >>>     intersection_of_date_ranges(datetime(2025, 1, 10), datetime(2025, 1, 5), datetime(2025, 1, 1), datetime(2025, 1, 2))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: start1 must be less than or equal to end1.

        >>> # Ejemplo 6: Tipos de datos incorrectos
        >>> try:
        >>>     intersection_of_date_ranges("not a date", r1_end, r2_start, r2_end)
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: All date range arguments must be datetime objects.
    """
    # 1. Validación de tipos de datos de entrada
    if not all(isinstance(d, datetime) for d in [start1, end1, start2, end2]):
        raise TypeError("All date range arguments must be datetime objects.")

    # 2. Validación de la validez de los rangos individuales (inicio no puede ser posterior al fin)
    if start1 > end1:
        raise ValueError("start1 must be less than or equal to end1.")
    if start2 > end2:
        raise ValueError("start2 must be less than or equal to end2.")

    # 3. Calcular el inicio de la posible intersección (el más tardío de los dos inicios)
    intersection_start = max(start1, start2)
    
    # 4. Calcular el fin de la posible intersección (el más temprano de los dos fines)
    intersection_end = min(end1, end2)

    # 5. Comprobar si hay una intersección válida.
    # Si el inicio calculado de la intersección es igual o anterior al fin calculado,
    # significa que hay un período de solapamiento.
    if intersection_start <= intersection_end:
        return (intersection_start, intersection_end)
    else:
        # Si el inicio de la intersección es posterior al fin, los rangos no se solapan.
        return None


def dates_between(start_date: datetime.date, end_date: datetime.date) -> list[datetime.date]:
    """
    Generates a list of dates between a start date and an end date, inclusive.

    This function iterates day by day from the start_date up to and including
    the end_date, collecting each date into a list. The order of the input dates
    does not matter; the function will automatically determine the chronological
    start and end.

    Args:
        start_date (datetime.date): The initial date.
        end_date (datetime.date): The final date.

    Returns:
        list[datetime.date]: A list containing all dates between the start and end dates.

    Raises:
        TypeError: If start_date or end_date are not datetime.date objects.

    Example of use:
        >>> from datetime import date
        >>> start = date(2023, 1, 1)
        >>> end = date(2023, 1, 5)
        >>> dates_between(start, end)
        [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), datetime.date(2023, 1, 4), datetime.date(2023, 1, 5)]

        >>> start = date(2023, 1, 5)
        >>> end = date(2023, 1, 1)
        >>> dates_between(start, end)
        [datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), datetime.date(2023, 1, 4), datetime.date(2023, 1, 5)]
    """
    if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
        raise TypeError("Both start_date and end_date must be datetime.date objects.")

    # Ensure the start_date is chronologically before or equal to the end_date.
    # This simplifies the loop logic by always iterating forward.
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    list_of_dates = []
    current_date = start_date

    # Iterate through each day from the start_date to the end_date.
    # We use a while loop because the number of iterations depends on the date difference.
    while current_date <= end_date:
        list_of_dates.append(current_date)
        current_date += datetime.timedelta(days=1) # Move to the next day

    return list_of_dates
    

def date_intervals(
    start_date: Union[datetime, str],
    end_date: Union[datetime, str],
    granularity: str,
    input_format: Optional[str] = None
) -> List[Tuple[datetime, datetime]]:
    """Genera una lista de intervalos de fechas (inicio, fin) para una granularidad específica,
    alineados a las unidades naturales de la granularidad y cubriendo el rango dado.

    Problema/Necesidad del Usuario: Es necesario segmentar un período de tiempo
    extenso en intervalos más pequeños y uniformes (años, trimestres, meses, etc.)
    para análisis, informes o procesamiento por lotes.

    Objetivos del Producto: Proporcionar una herramienta flexible y precisa para
    dividir rangos de fechas en unidades de tiempo estandarizadas, facilitando
    la agregación y visualización de datos temporales.

    Descripción: Esta función toma una fecha de inicio y una fecha de fin, junto
    con una granularidad deseada, y devuelve una lista de tuplas,
    donde cada tupla representa el (inicio, fin) de un intervalo. Los intervalos
    se generan alineados a los inicios y fines naturales de su unidad (ej. 1 de mes,
    lunes de semana) y cubren todas las unidades que intersectan
    el rango `[start_date, end_date]`.

    Args:
        start_date (Union[datetime, str]): La fecha de inicio del rango (inclusiva). Puede ser un
                                            objeto `datetime` o una cadena de fecha.
        end_date (Union[datetime, str]): La fecha de fin del rango (inclusiva). Puede ser un
                                          objeto `datetime` o una cadena de fecha.
        granularity (str): La unidad de tiempo para los intervalos.
                           Valores permitidos (en minúsculas):
                           'year', 'quarter', 'month', 'half_month', 'week',
                           'day', 'hour', 'minute', 'second'.
        input_format (str, optional): El formato de cadena de fecha (ej. '%Y-%m-%d %H:%M:%S')
                                      si 'start_date' o 'end_date' son cadenas. Es
                                      **obligatorio** si alguna de las fechas es una cadena.

    Returns:
        List[Tuple[datetime, datetime]]: Una lista de tuplas, donde cada tupla
                                         contiene (datetime_inicio_intervalo, datetime_fin_intervalo).
                                         Los objetos datetime de fin de intervalo siempre se ajustarán
                                         al final de la unidad de tiempo correspondiente (ej. 23:59:59.999999 para día).

    Raises:
        TypeError: Si 'start_date' o 'end_date' no son objetos datetime o cadenas.
        ValueError: Si 'input_format' es `None` y alguna de las fechas es una cadena;
                    si la cadena de fecha no puede ser parseada; si 'start_date' es
                    posterior a 'end_date'; o si la 'granularity' no es reconocida.

    Example:
        >>> from datetime import datetime, timedelta

        >>> # 1. Intervalos diarios
        >>> # Cubre del 1 de junio al 3 de junio.
        >>> intervals_day = date_intervals(datetime(2025, 6, 1, 10, 0), datetime(2025, 6, 3, 14, 30), 'day')
        >>> for s, e in intervals_day: print(f"({s}, {e})")
        # (2025-06-01 00:00:00, 2025-06-01 23:59:59.999999)
        # (2025-06-02 00:00:00, 2025-06-02 23:59:59.999999)
        # (2025-06-03 00:00:00, 2025-06-03 23:59:59.999999)

        >>> # 2. Intervalos semanales (Lunes como inicio de semana)
        >>> # June 2025: 1st is Sunday. Week starts May 26.
        >>> # Cubre desde la semana del 1 de junio hasta la semana del 9 de junio.
        >>> intervals_week = date_intervals(datetime(2025, 6, 1, 12, 0), datetime(2025, 6, 9, 10, 0), 'week')
        >>> for s, e in intervals_week: print(f"({s}, {e})")
        # (2025-05-26 00:00:00, 2025-06-01 23:59:59.999999) # Semana que contiene el 1 de junio
        # (2025-06-02 00:00:00, 2025-06-08 23:59:59.999999) # Semana que contiene el 2 de junio
        # (2025-06-09 00:00:00, 2025-06-15 23:59:59.999999) # Semana que contiene el 9 de junio (hasta el 15, aunque end_date sea antes)

        >>> # 3. Intervalos mensuales
        >>> # Cubre de enero a marzo 2025.
        >>> intervals_month = date_intervals(datetime(2025, 1, 15), datetime(2025, 3, 10), 'month')
        >>> for s, e in intervals_month: print(f"({s}, {e})")
        # (2025-01-01 00:00:00, 2025-01-31 23:59:59.999999)
        # (2025-02-01 00:00:00, 2025-02-28 23:59:59.999999)
        # (2025-03-01 00:00:00, 2025-03-31 23:59:59.999999)

        >>> # 4. Intervalos de quincena (1-15, 16-fin de mes)
        >>> # Cubre desde la 2da quincena de junio hasta la 2da quincena de julio 2025.
        >>> intervals_half_month = date_intervals(datetime(2025, 6, 10), datetime(2025, 7, 20), 'half_month')
        >>> for s, e in intervals_half_month: print(f"({s}, {e})")
        # (2025-06-01 00:00:00, 2025-06-15 23:59:59.999999) # La quincena que contiene el 10 de junio
        # (2025-06-16 00:00:00, 2025-06-30 23:59:59.999999)
        # (2025-07-01 00:00:00, 2025-07-15 23:59:59.999999)
        # (2025-07-16 00:00:00, 2025-07-31 23:59:59.999999) # La quincena que contiene el 20 de julio

        >>> # 5. Intervalos de horas
        >>> date_intervals(datetime(2025, 6, 1, 10, 30), datetime(2025, 6, 1, 12, 15), 'hour')
        # Output: [(2025-06-01 10:00:00, 2025-06-01 10:59:59.999999),
        #          (2025-06-01 11:00:00, 2025-06-01 11:59:59.999999),
        #          (2025-06-01 12:00:00, 2025-06-01 12:59:59.999999)]
    """
    # --- Función auxiliar interna para parsear la entrada de fecha (reutilizada) ---
    def _parse_date_input_internal(date_val: Union[datetime, str], input_fmt: Optional[str]) -> datetime:
        if isinstance(date_val, str):
            if input_fmt is None:
                raise ValueError("'input_format' is required when 'date_input' is a string.")
            try:
                return datetime.strptime(date_val, input_fmt)
            except ValueError as e:
                raise ValueError(f"Could not parse date string '{date_val}' with format '{input_fmt}'. Error: {e}") from e
        elif isinstance(date_val, datetime):
            return date_val
        else:
            raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # --- Parsear y validar las fechas de inicio y fin ---
    parsed_start_date = _parse_date_input_internal(start_date, input_format)
    parsed_end_date = _parse_date_input_internal(end_date, input_format)

    if parsed_start_date > parsed_end_date:
        raise ValueError("start_date cannot be after end_date.")

    granularity = granularity.lower() # Normalizar la cadena de granularidad a minúsculas

    intervals: List[Tuple[datetime, datetime]] = []
    
    # Determinar el inicio del primer intervalo, alineado a la granularidad
    current_iter_date: datetime

    if granularity == 'year':
        current_iter_date = datetime(parsed_start_date.year, 1, 1)
    elif granularity == 'quarter':
        current_quarter = (parsed_start_date.month - 1) // 3 + 1
        current_iter_date = datetime(parsed_start_date.year, (current_quarter - 1) * 3 + 1, 1)
    elif granularity == 'month':
        current_iter_date = datetime(parsed_start_date.year, parsed_start_date.month, 1)
    elif granularity == 'half_month':
        # Una quincena va del día 1 al 15, la otra del día 16 al final del mes.
        if parsed_start_date.day <= 15:
            current_iter_date = datetime(parsed_start_date.year, parsed_start_date.month, 1)
        else:
            current_iter_date = datetime(parsed_start_date.year, parsed_start_date.month, 16)
    elif granularity == 'week':
        # Ajustar a Lunes (weekday() devuelve 0 para Lunes, 6 para Domingo)
        current_iter_date = parsed_start_date - timedelta(days=parsed_start_date.weekday())
        current_iter_date = current_iter_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elif granularity == 'day':
        current_iter_date = parsed_start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elif granularity == 'hour':
        current_iter_date = parsed_start_date.replace(minute=0, second=0, microsecond=0)
    elif granularity == 'minute':
        current_iter_date = parsed_start_date.replace(second=0, microsecond=0)
    elif granularity == 'second':
        current_iter_date = parsed_start_date.replace(microsecond=0)
    else:
        raise ValueError(f"Unsupported granularity: '{granularity}'. "
                         f"Supported: 'year', 'quarter', 'month', 'half_month', 'week', 'day', 'hour', 'minute', 'second'.")

    # --- Bucle para generar los intervalos ---
    # El bucle continúa mientras el inicio del intervalo actual no exceda la fecha de fin del rango.
    while current_iter_date <= parsed_end_date:
        interval_start = current_iter_date
        interval_end: datetime
        next_iter_date: datetime # El inicio del próximo intervalo

        if granularity == 'year':
            interval_end = datetime(current_iter_date.year, 12, 31, 23, 59, 59, 999999)
            next_iter_date = datetime(current_iter_date.year + 1, 1, 1)
        elif granularity == 'quarter':
            # Calcular el mes final del trimestre actual
            current_quarter_num = (current_iter_date.month - 1) // 3 + 1
            quarter_end_month = current_iter_date.month + (3 - (current_iter_date.month - (current_quarter_num - 1) * 3)) # Month of current quarter
            
            last_day_of_quarter_end_month = calendar.monthrange(current_iter_date.year, quarter_end_month)[1]
            interval_end = datetime(current_iter_date.year, quarter_end_month, last_day_of_quarter_end_month, 23, 59, 59, 999999)
            
            # Calcular el inicio del próximo trimestre
            next_month = current_iter_date.month + 3
            next_year = current_iter_date.year
            if next_month > 12:
                next_month -= 12
                next_year += 1
            next_iter_date = datetime(next_year, next_month, 1)
        elif granularity == 'month':
            last_day_of_month = calendar.monthrange(current_iter_date.year, current_iter_date.month)[1]
            interval_end = datetime(current_iter_date.year, current_iter_date.month, last_day_of_month, 23, 59, 59, 999999)
            
            next_month = current_iter_date.month + 1
            next_year = current_iter_date.year
            if next_month > 12:
                next_month = 1
                next_year += 1
            next_iter_date = datetime(next_year, next_month, 1)
        elif granularity == 'half_month':
            if current_iter_date.day == 1: # Primera quincena (día 1 al 15)
                interval_end = datetime(current_iter_date.year, current_iter_date.month, 15, 23, 59, 59, 999999)
                next_iter_date = datetime(current_iter_date.year, current_iter_date.month, 16)
            else: # Segunda quincena (día 16 al final del mes)
                last_day_of_month = calendar.monthrange(current_iter_date.year, current_iter_date.month)[1]
                interval_end = datetime(current_iter_date.year, current_iter_date.month, last_day_of_month, 23, 59, 59, 999999)
                
                # Siguiente quincena es el día 1 del próximo mes
                next_month = current_iter_date.month + 1
                next_year = current_iter_date.year
                if next_month > 12:
                    next_month = 1
                    next_year += 1
                next_iter_date = datetime(next_year, next_month, 1)
        elif granularity == 'week':
            # La semana termina 6 días después del lunes (incluyendo el lunes)
            interval_end = current_iter_date + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
            next_iter_date = current_iter_date + timedelta(weeks=1)
        elif granularity == 'day':
            interval_end = current_iter_date.replace(hour=23, minute=59, second=59, microsecond=999999)
            next_iter_date = current_iter_date + timedelta(days=1)
        elif granularity == 'hour':
            interval_end = current_iter_date.replace(minute=59, second=59, microsecond=999999)
            next_iter_date = current_iter_date + timedelta(hours=1)
        elif granularity == 'minute':
            interval_end = current_iter_date.replace(second=59, microsecond=999999)
            next_iter_date = current_iter_date + timedelta(minutes=1)
        elif granularity == 'second':
            interval_end = current_iter_date.replace(microsecond=999999)
            next_iter_date = current_iter_date + timedelta(seconds=1)
        # No se necesita else aquí, ya que la validación inicial de granularidad lo cubre.

        # Añadir el intervalo actual a la lista
        intervals.append((interval_start, interval_end))
        
        # Mover al inicio del próximo intervalo para la siguiente iteración
        current_iter_date = next_iter_date
        
    return intervals


def add_microseconds(date_input: datetime, microseconds: int) -> datetime:
    """Añade o resta un número específico de microsegundos a un objeto datetime.

    Problema/Necesidad del Usuario: Para aplicaciones que requieren una precisión
    extremadamente alta en el tiempo (ej. trading financiero, mediciones científicas,
    sistemas de control), la capacidad de sumar o restar microsegundos es esencial.

    Objetivos del Producto: Proporcionar una manipulación de tiempo con la granularidad
    más fina disponible en Python, abordando casos de uso de alta precisión.

    Descripción: Esta función toma un objeto `datetime` y un entero que representa
    la cantidad de microsegundos a añadir o restar. Los microsegundos pueden ser
    positivos (para sumar) o negativos (para restar). La función devuelve un
    nuevo objeto `datetime` con el ajuste aplicado.

    Args:
        date_input (datetime): El objeto `datetime` original.
        microseconds (int): El número de microsegundos a añadir (positivo) o restar (negativo).

    Returns:
        datetime: Un nuevo objeto `datetime` con los microsegundos ajustados.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o si 'microseconds' no es un entero.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Sumar microsegundos
        >>> dt = datetime(2025, 6, 11, 10, 0, 0, 100)
        >>> add_microseconds(dt, 50)
        datetime.datetime(2025, 6, 11, 10, 0, 0, 150)

        >>> # Ejemplo 2: Restar microsegundos
        >>> dt = datetime(2025, 6, 11, 10, 0, 0, 500)
        >>> add_microseconds(dt, -200)
        datetime.datetime(2025, 6, 11, 10, 0, 0, 300)

        >>> # Ejemplo 3: Ajuste que afecta segundos (o componentes superiores)
        >>> dt = datetime(2025, 6, 11, 10, 0, 0, 999999) # Casi un segundo completo
        >>> add_microseconds(dt, 2)
        datetime.datetime(2025, 6, 11, 10, 0, 1, 1) # Pasa al siguiente segundo y microsegundo 1

        >>> # Ejemplo 4: Resta que afecta segundos (o componentes superiores)
        >>> dt = datetime(2025, 6, 11, 10, 0, 1, 5) # Un segundo y 5 microsegundos
        >>> add_microseconds(dt, -10)
        datetime.datetime(2025, 6, 11, 9, 59, 59, 999995) # Retrocede un segundo, un minuto, etc.
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")
    if not isinstance(microseconds, int):
        raise TypeError("Input 'microseconds' must be an integer.")

    # Se usa timedelta para sumar o restar microsegundos.
    # timedelta maneja automáticamente los desbordamientos a segundos, minutos, etc.
    return date_input + timedelta(microseconds=microseconds)


def set_microseconds(date_input: datetime, microseconds: int) -> datetime:
    """Devuelve un nuevo objeto datetime con los microsegundos establecidos al valor especificado.

    Problema/Necesidad del Usuario: A veces, se necesita establecer los microsegundos
    de un datetime a un valor exacto, sin afectar los otros componentes de tiempo.

    Objetivos del Producto: Ofrecer control total sobre la granularidad de microsegundos,
    útil para normalización o para establecer valores precisos.

    Descripción: Esta función toma un objeto `datetime` y un entero para los microsegundos.
    Crea y devuelve un *nuevo* objeto `datetime` donde solo la parte de los microsegundos
    ha sido modificada al valor proporcionado, manteniendo el año, mes, día, hora,
    minuto, segundo y zona horaria (si existe) del objeto original.

    Args:
        date_input (datetime): El objeto `datetime` original.
        microseconds (int): El valor de microsegundos a establecer (de 0 a 999999).

    Returns:
        datetime: Un nuevo objeto `datetime` con los microsegundos establecidos.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o si 'microseconds' no es un entero.
        ValueError: Si 'microseconds' está fuera del rango válido (0 a 999999).

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Establecer microsegundos a un valor específico
        >>> dt = datetime(2025, 6, 11, 10, 0, 0, 123456)
        >>> set_microseconds(dt, 789)
        datetime.datetime(2025, 6, 11, 10, 0, 0, 789)

        >>> # Ejemplo 2: Establecer microsegundos a cero
        >>> dt = datetime(2025, 6, 11, 10, 0, 0, 987654)
        >>> set_microseconds(dt, 0)
        datetime.datetime(2025, 6, 11, 10, 0, 0, 0)

        >>> # Ejemplo 3: Valor de microsegundos fuera de rango (levantará ValueError)
        >>> try:
        >>>     set_microseconds(datetime(2025, 6, 11, 10, 0, 0), 1000000)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: microseconds must be in 0..999999
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")
    if not isinstance(microseconds, int):
        raise TypeError("Input 'microseconds' must be an integer.")
    if not (0 <= microseconds <= 999999):
        raise ValueError("microseconds must be in 0..999999")

    # El método replace() es ideal para esto, ya que devuelve un nuevo objeto datetime
    # con los componentes especificados modificados, dejando el resto intacto.
    return date_input.replace(microsecond=microseconds)


def is_duration_less_than(start_date: datetime, end_date: datetime, threshold_duration: timedelta) -> bool:
    """Comprueba si la duración entre start_date y end_date es estrictamente menor que threshold_duration.

    Problema/Necesidad del Usuario: Validar si la duración entre dos fechas es menor que un
    umbral específico. Muy útil para SLAs (Acuerdos de Nivel de Servicio), plazos o límites de tiempo.

    Objetivos del Producto: Proporcionar una forma clara y concisa de validar la duración
    de un evento o un período, esencial para reglas de negocio basadas en el tiempo.

    Descripción: Esta función calcula la duración absoluta entre `start_date` y `end_date`
    y la compara con `threshold_duration`. Retorna `True` si la duración calculada es
    estrictamente menor que el umbral, y `False` en cualquier otro caso (mayor o igual).
    No importa el orden de `start_date` y `end_date`, ya que la duración se calcula
    como un valor absoluto.

    Args:
        start_date (datetime): La fecha y hora de inicio.
        end_date (datetime): La fecha y hora de fin.
        threshold_duration (timedelta): La duración de umbral con la que comparar.

    Returns:
        bool: `True` si la duración es estrictamente menor que el umbral; `False` en caso contrario.

    Raises:
        TypeError: Si `start_date` o `end_date` no son objetos `datetime`,
                   o si `threshold_duration` no es un objeto `timedelta`.

    Example:
        >>> from datetime import datetime, timedelta

        >>> # Ejemplo 1: Duración menor que el umbral
        >>> is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 20), timedelta(minutes=30))
        True
        >>> # (20 minutos < 30 minutos)

        >>> # Ejemplo 2: Duración igual al umbral (debe ser False porque es estrictamente menor)
        >>> is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 30), timedelta(minutes=30))
        False
        >>> # (30 minutos < 30 minutos) es Falso

        >>> # Ejemplo 3: Duración mayor que el umbral
        >>> is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 45), timedelta(minutes=30))
        False
        >>> # (45 minutos < 30 minutos) es Falso

        >>> # Ejemplo 4: Fechas en orden invertido (la duración absoluta sigue siendo la misma)
        >>> is_duration_less_than(datetime(2025, 6, 11, 10, 20), datetime(2025, 6, 11, 10, 0), timedelta(minutes=30))
        True
        >>> # (20 minutos < 30 minutos)

        >>> # Ejemplo 5: Tipos de datos incorrectos
        >>> try:
        >>>     is_duration_less_than("2025-06-11", datetime(2025, 6, 11, 10, 20), timedelta(minutes=30))
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: start_date and end_date must be datetime objects.
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")
    if not isinstance(threshold_duration, timedelta):
        raise TypeError("threshold_duration must be a timedelta object.")

    # Calcular la duración absoluta entre las dos fechas
    actual_duration = abs(end_date - start_date)

    # Comprobar si la duración calculada es estrictamente menor que el umbral
    return actual_duration < threshold_duration


def is_duration_greater_than(start_date: datetime, end_date: datetime, threshold_duration: timedelta) -> bool:
    """Comprueba si la duración entre start_date y end_date es estrictamente mayor que threshold_duration.

    Problema/Necesidad del Usuario: La contraparte de la anterior: verificar si la duración
    es mayor que un umbral. Útil para identificar eventos de larga duración o violaciones de tiempo.

    Objetivos del Producto: Complementar las validaciones de duración, permitiendo la
    detección de eventos que exceden ciertos límites de tiempo.

    Descripción: Esta función calcula la duración absoluta entre `start_date` y `end_date`
    y la compara con `threshold_duration`. Retorna `True` si la duración calculada es
    estrictamente mayor que el umbral, y `False` en cualquier otro caso (menor o igual).
    No importa el orden de `start_date` y `end_date`, ya que la duración se calcula
    como un valor absoluto.

    Args:
        start_date (datetime): La fecha y hora de inicio.
        end_date (datetime): La fecha y hora de fin.
        threshold_duration (timedelta): La duración de umbral con la que comparar.

    Returns:
        bool: `True` si la duración es estrictamente mayor que el umbral; `False` en caso contrario.

    Raises:
        TypeError: Si `start_date` o `end_date` no son objetos `datetime`,
                   o si `threshold_duration` no es un objeto `timedelta`.

    Example:
        >>> from datetime import datetime, timedelta

        >>> # Ejemplo 1: Duración mayor que el umbral
        >>> is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 45), timedelta(minutes=30))
        True
        >>> # (45 minutos > 30 minutos)

        >>> # Ejemplo 2: Duración igual al umbral (debe ser False porque es estrictamente mayor)
        >>> is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 30), timedelta(minutes=30))
        False
        >>> # (30 minutos > 30 minutos) es Falso

        >>> # Ejemplo 3: Duración menor que el umbral
        >>> is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 15), timedelta(minutes=30))
        False
        >>> # (15 minutos > 30 minutos) es Falso

        >>> # Ejemplo 4: Fechas en orden invertido
        >>> is_duration_greater_than(datetime(2025, 6, 11, 10, 45), datetime(2025, 6, 11, 10, 0), timedelta(minutes=30))
        True
        >>> # (45 minutos > 30 minutos)

        >>> # Ejemplo 5: Tipos de datos incorrectos
        >>> try:
        >>>     is_duration_greater_than(datetime(2025, 6, 11, 10, 0), "2025-06-11", timedelta(minutes=30))
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: start_date and end_date must be datetime objects.
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")
    if not isinstance(threshold_duration, timedelta):
        raise TypeError("threshold_duration must be a timedelta object.")

    # Calcular la duración absoluta entre las dos fechas
    actual_duration = abs(end_date - start_date)

    # Comprobar si la duración calculada es estrictamente mayor que el umbral
    return actual_duration > threshold_duration


def full_years_between(start_date: datetime, end_date: datetime) -> int:
    """Devuelve el número de años completos transcurridos entre start_date y end_date. No cuenta años parciales.

    Problema/Necesidad del Usuario: Calcular el número de años completos transcurridos entre dos fechas.
    Diferente de la resta simple que podría dar decimales. Esto es útil para cálculos de edad exactos
    o periodos de tiempo completos.

    Objetivos del Producto: Proporcionar una función precisa para calcular la diferencia de años completos,
    que es vital en cálculos demográficos, contractuales o de antigüedad.

    Descripción: Esta función calcula el número de años completos que han pasado desde `start_date` hasta `end_date`.
    Un año completo se cuenta solo si `end_date` ha alcanzado o superado el día y mes de `start_date` en el año `end_date`.
    Si `start_date` es posterior a `end_date`, el resultado será un número negativo.

    Args:
        start_date (datetime): La fecha de inicio.
        end_date (datetime): La fecha de fin.

    Returns:
        int: El número de años completos transcurridos.

    Raises:
        TypeError: Si `start_date` o `end_date` no son objetos `datetime`.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: No se ha completado el quinto año (falta 1 día)
        >>> full_years_between(datetime(2020, 6, 11), datetime(2025, 6, 10))
        4

        >>> # Ejemplo 2: Se ha completado el quinto año (en el mismo día)
        >>> full_years_between(datetime(2020, 6, 11), datetime(2025, 6, 11))
        5

        >>> # Ejemplo 3: Múltiples años completos
        >>> full_years_between(datetime(2010, 1, 1), datetime(2025, 12, 31))
        15

        >>> # Ejemplo 4: Solo días, sin años completos
        >>> full_years_between(datetime(2025, 1, 1), datetime(2025, 12, 31))
        0

        >>> # Ejemplo 5: Fechas en orden invertido (resultado negativo)
        >>> full_years_between(datetime(2025, 6, 11), datetime(2020, 6, 10))
        -4

        >>> # Ejemplo 6: Diferencia de días dentro del mismo año (sin años completos)
        >>> full_years_between(datetime(2025, 1, 15), datetime(2025, 3, 14))
        0
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    # Determinar el orden de las fechas para el cálculo
    is_reverse = False
    if start_date > end_date:
        start_date, end_date = end_date, start_date
        is_reverse = True

    # Calcular la diferencia de años
    years = end_date.year - start_date.year

    # Ajustar si el "cumpleaños" del año no se ha alcanzado aún
    # Si el mes o el día de end_date es anterior al de start_date,
    # significa que no se ha completado un año más.
    if end_date.month < start_date.month or \
       (end_date.month == start_date.month and end_date.day < start_date.day):
        years -= 1
    
    return -years if is_reverse else years


def full_months_between(start_date: datetime, end_date: datetime) -> int:
    """Devuelve el número de meses completos transcurridos entre start_date y end_date. No cuenta meses parciales.

    Problema/Necesidad del Usuario: Similar al cálculo de años, pero para el número de meses completos.
    Útil para períodos de facturación, suscripciones o antigüedad laboral.

    Objetivos del Producto: Ofrecer una función precisa para calcular la diferencia de meses completos,
    esencial para la gestión de membresías, finanzas o cualquier ciclo mensual.

    Descripción: Esta función calcula el número de meses completos que han pasado desde `start_date` hasta `end_date`.
    Un mes completo se cuenta solo si `end_date` ha alcanzado o superado el día de `start_date` en el mes `end_date`.
    Si `start_date` es posterior a `end_date`, el resultado será un número negativo.

    Args:
        start_date (datetime): La fecha de inicio.
        end_date (datetime): La fecha de fin.

    Returns:
        int: El número de meses completos transcurridos.

    Raises:
        TypeError: Si `start_date` o `end_date` no son objetos `datetime`.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Solo un mes completo (del 15 de enero al 14 de marzo)
        >>> full_months_between(datetime(2025, 1, 15), datetime(2025, 3, 14))
        1

        >>> # Ejemplo 2: Dos meses completos (del 15 de enero al 15 de marzo)
        >>> full_months_between(datetime(2025, 1, 15), datetime(2025, 3, 15))
        2

        >>> # Ejemplo 3: Múltiples meses completos
        >>> full_months_between(datetime(2024, 8, 1), datetime(2025, 2, 28))
        6

        >>> # Ejemplo 4: Solo días, sin meses completos
        >>> full_months_between(datetime(2025, 1, 1), datetime(2025, 1, 31))
        0

        >>> # Ejemplo 5: Fechas en orden invertido (resultado negativo)
        >>> full_months_between(datetime(2025, 3, 15), datetime(2025, 1, 15))
        -2

        >>> # Ejemplo 6: Con días que "no cumplen" el mes completo
        >>> full_months_between(datetime(2025, 1, 31), datetime(2025, 3, 1))
        1 # De 31 de enero a 1 de marzo, solo se ha completado febrero.
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    # Determinar el orden de las fechas para el cálculo
    is_reverse = False
    if start_date > end_date:
        start_date, end_date = end_date, start_date
        is_reverse = True

    # Calcular la diferencia total en meses
    total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    # Ajustar si el día del mes de end_date es anterior al día de start_date.
    # Si el día del mes actual es anterior al día de inicio,
    # significa que el último mes no se ha completado.
    if end_date.day < start_date.day:
        total_months -= 1
    
    return -total_months if is_reverse else total_months


def generate_random_date(start_date: Optional[date] = None, end_date: Optional[date] = None, business_days_only: bool = False) -> date:
    """Generates a random date within a specified range, optionally restricted to business days.

    Args:
        start_date (Optional[date]): The earliest possible date. Defaults to 1900-01-01 if None.
        end_date (Optional[date]): The latest possible date. Defaults to 2100-12-31 if None.
        business_days_only (bool): If True, only returns dates that are not Saturdays or Sundays. Defaults to False.

    Returns:
        date: A randomly generated date.

    Raises:
        ValueError: If start_date is after end_date.
        TypeError: If start_date or end_date are not date objects, or business_days_only is not a bool.

    Example:
        >>> # Get a random date today or in the future (up to 2050)
        >>> from datetime import date
        >>> today = date.today()
        >>> generate_random_date(start_date=today, end_date=date(2050, 12, 31))
        # Example output: date(2035, 7, 23)

        >>> # Get a random date in the past, only on business days
        >>> generate_random_date(start_date=date(2020, 1, 1), end_date=date(2022, 12, 31), business_days_only=True)
        # Example output: date(2021, 5, 18) (not a Saturday/Sunday)

        >>> # Get a random date with default range
        >>> generate_random_date()
        # Example output: date(2045, 11, 5)

        >>> # Invalid date range (will raise ValueError)
        >>> try:
        >>>     generate_random_date(start_date=date(2025, 1, 1), end_date=date(2024, 1, 1))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: start_date cannot be after end_date.
    """
    if start_date is None:
        start_date = date(1900, 1, 1)
    if end_date is None:
        end_date = date(2100, 12, 31)

    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise TypeError("start_date and end_date must be date objects.")
    if not isinstance(business_days_only, bool):
        raise TypeError("business_days_only must be a boolean.")
    if start_date > end_date:
        raise ValueError("start_date cannot be after end_date.")

    time_between_dates = end_date - start_date
    random_days = random.randrange(time_between_dates.days + 1)
    random_date = start_date + timedelta(days=random_days)

    if business_days_only:
        # Keep trying until a business day is found
        # In rare cases, if start_date and end_date are very close and only contain weekends,
        # this might loop many times. For very small ranges with only weekends,
        # it might even lead to an infinite loop if not handled carefully (though unlikely with random.randrange).
        # A safer approach for small ranges could be to pre-filter all business days in the range.
        # But for general use, re-rolling is fine.
        max_attempts = 1000 # Prevent infinite loops for edge cases
        attempts = 0
        while random_date.weekday() >= 5: # 5 is Saturday, 6 is Sunday
            attempts += 1
            if attempts > max_attempts:
                # If we can't find one after many tries, it means the range is likely all weekends
                # or extremely small. Re-roll completely or signal failure.
                # For this function, let's just re-roll until a valid one is found, assuming reasonable ranges.
                # If this is problematic for very narrow, weekend-only ranges, this needs more specific logic.
                # But for general random date generation, re-rolling is sufficient.
                # An alternative would be to adjust random_date by +1 day until weekday() < 5
                # and then check if it's still within the original end_date.
                # For now, let's stick to simple re-rolling within the original range.
                random_days = random.randrange(time_between_dates.days + 1)
                random_date = start_date + timedelta(days=random_days)
            else:
                random_days = random.randrange(time_between_dates.days + 1)
                random_date = start_date + timedelta(days=random_days)
    
    return random_date


def generate_random_time(min_time: Optional[time] = None, max_time: Optional[time] = None) -> time:
    """Generates a random time object within an optional specified range.

    Args:
        min_time (Optional[time]): The earliest possible time. Defaults to 00:00:00 if None.
        max_time (Optional[time]): The latest possible time. Defaults to 23:59:59.999999 if None.

    Returns:
        time: A randomly generated time.

    Raises:
        ValueError: If min_time is after max_time.
        TypeError: If min_time or max_time are not time objects.

    Example:
        >>> # Get a random time between 9 AM and 5 PM
        >>> generate_random_time(min_time=time(9, 0, 0), max_time=time(17, 0, 0))
        # Example output: datetime.time(14, 23, 5, 876543)

        >>> # Get a random time with default range (any time of day)
        >>> generate_random_time()
        # Example output: datetime.time(21, 5, 34, 123456)

        >>> # Invalid time range (will raise ValueError)
        >>> try:
        >>>     generate_random_time(min_time=time(17, 0, 0), max_time=time(9, 0, 0))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: min_time cannot be after max_time.
    """
    if min_time is None:
        min_time = time.min # 00:00:00
    if max_time is None:
        max_time = time.max # 23:59:59.999999

    if not isinstance(min_time, time) or not isinstance(max_time, time):
        raise TypeError("min_time and max_time must be time objects.")
    if min_time > max_time:
        raise ValueError("min_time cannot be after max_time.")

    # Convert times to microseconds from midnight for easier calculation
    min_us = (min_time.hour * 3600 + min_time.minute * 60 + min_time.second) * 1_000_000 + min_time.microsecond
    max_us = (max_time.hour * 3600 + max_time.minute * 60 + max_time.second) * 1_000_000 + max_time.microsecond

    random_us = random.randrange(min_us, max_us + 1)

    # Convert back to time object
    seconds = random_us // 1_000_000
    microsecond = random_us % 1_000_000
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60

    return time(hour, minute, second, microsecond)


def generate_random_datetime(start_dt: Optional[datetime] = None, end_dt: Optional[datetime] = None, tz_info: Optional[str] = None) -> datetime:
    """Generates a random datetime object within a specified range, optionally localized to a timezone.

    Args:
        start_dt (Optional[datetime]): The earliest possible datetime. Defaults to 1900-01-01 00:00:00 UTC if None.
        end_dt (Optional[datetime]): The latest possible datetime. Defaults to 2100-12-31 23:59:59.999999 UTC if None.
        tz_info (Optional[str]): IANA timezone string (e.g., 'America/New_York', 'Europe/Madrid').
                                 If None, the generated datetime will be naive (without timezone info).
                                 If a timezone is provided, start_dt/end_dt are converted to it for range calculation
                                 or assumed to be in that timezone if naive. It's best to provide timezone-aware datetimes.

    Returns:
        datetime: A randomly generated datetime.

    Raises:
        ValueError: If start_dt is after end_dt, or if tz_info is an invalid timezone string.
        TypeError: If start_dt or end_dt are not datetime objects, or tz_info is not a string.
        zoneinfo.ZoneInfoNotFoundError: (Captured and re-raised as ValueError) If the timezone is not found.

    Example:
        >>> # Get a random datetime in the next year (UTC)
        >>> from datetime import datetime, timezone
        >>> now = datetime.now(timezone.utc)
        >>> generate_random_datetime(start_dt=now, end_dt=now + timedelta(days=365), tz_info='UTC')
        # Example output: datetime.datetime(2026, 3, 10, 15, 30, 45, 123456, tzinfo=datetime.timezone.utc)

        >>> # Get a random datetime in a specific timezone (e.g., Madrid) for a past month
        >>> generate_random_datetime(start_dt=datetime(2025, 5, 1, 0, 0, 0),
        >>>                          end_dt=datetime(2025, 5, 31, 23, 59, 59),
        >>>                          tz_info='Europe/Madrid')
        # Example output: datetime.datetime(2025, 5, 18, 11, 7, 22, 98765, tzinfo=zoneinfo.ZoneInfo(key='Europe/Madrid'))

        >>> # Get a random naive datetime (no timezone)
        >>> generate_random_datetime(start_dt=datetime(2020, 1, 1), end_dt=datetime(2020, 12, 31))
        # Example output: datetime.datetime(2020, 7, 10, 8, 55, 1, 54321)

        >>> # Invalid datetime range (will raise ValueError)
        >>> try:
        >>>     generate_random_datetime(start_dt=datetime(2025, 1, 1), end_dt=datetime(2024, 1, 1))
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: start_dt cannot be after end_dt.
    """
    if start_dt is None:
        start_dt = datetime(1900, 1, 1, tzinfo=timezone.utc)
    if end_dt is None:
        end_dt = datetime(2100, 12, 31, 23, 59, 59, 999999, tzinfo=timezone.utc)

    if not isinstance(start_dt, datetime) or not isinstance(end_dt, datetime):
        raise TypeError("start_dt and end_dt must be datetime objects.")
    if tz_info is not None and not isinstance(tz_info, str):
        raise TypeError("tz_info must be a string representing an IANA timezone.")
    if start_dt > end_dt:
        raise ValueError("start_dt cannot be after end_dt.")

    target_tz = None
    if tz_info:
        try:
            target_tz = zoneinfo.ZoneInfo(tz_info)
        except zoneinfo.ZoneInfoNotFoundError:
            raise ValueError(f"Invalid or unknown timezone: '{tz_info}'.")
        
        # If start_dt or end_dt are naive, assume they are in the target_tz for the range.
        # If they are aware, convert them to the target_tz for the range.
        if start_dt.tzinfo is None:
            start_dt = start_dt.replace(tzinfo=target_tz)
        else:
            start_dt = start_dt.astimezone(target_tz)
        
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=target_tz)
        else:
            end_dt = end_dt.astimezone(target_tz)

    # If no tz_info, but start_dt/end_dt have tzinfo, make them naive for calculation
    # or ensure they are both naive/aware for proper comparison.
    # For simplicity, if no tz_info is provided, we assume the range is in local system time if naive,
    # or convert to UTC if aware, then operate on timestamps.
    # The safest way is to convert both start and end to UTC timestamps if possible,
    # generate a random timestamp, then convert back.

    # Convert to UTC for consistent random generation across timezones if timezone-aware.
    # If naive, `timestamp()` assumes local time.
    start_timestamp_us: int
    end_timestamp_us: int

    if start_dt.tzinfo is None: # Naive datetime
        start_timestamp_us = int(start_dt.timestamp() * 1_000_000)
        end_timestamp_us = int(end_dt.timestamp() * 1_000_000)
    else: # Timezone-aware datetime
        start_timestamp_us = int(start_dt.astimezone(timezone.utc).timestamp() * 1_000_000)
        end_timestamp_us = int(end_dt.astimezone(timezone.utc).timestamp() * 1_000_000)

    random_timestamp_us = random.randrange(start_timestamp_us, end_timestamp_us + 1)

    # Convert back to datetime
    # Use fromtimestamp with timezone.utc and then convert to target_tz if specified.
    random_dt_utc = datetime.fromtimestamp(random_timestamp_us / 1_000_000, tz=timezone.utc)
    
    if target_tz:
        return random_dt_utc.astimezone(target_tz)
    else:
        # If no tz_info was provided, return a naive datetime from the UTC one.
        # This will be equivalent to what datetime.fromtimestamp(local_timestamp) would give,
        # but avoids relying on local system time during generation.
        return random_dt_utc.replace(tzinfo=None)
    

def get_week_of_year(date_input: datetime) -> int:
    """Returns the ISO 8601 week number for a given date.

    Delegates to :func:`iso_week_number`.

    Args:
        date_input (datetime): The datetime object.

    Returns:
        int: ISO week number (1-53).

    Raises:
        TypeError: If date_input is not a datetime object.

    Example:
        >>> from datetime import datetime
        >>> get_week_of_year(datetime(2025, 6, 11))
        24

    Complexity: O(1)
    """
    return iso_week_number(date_input)


def week_of_month(date_input: datetime, start_of_week: int = 0) -> int:
    """Devuelve el número de la semana del mes para una fecha dada.

    Problema/Necesidad del Usuario: Determinar la semana del mes es útil para la planificación
    mensual, la generación de informes o la organización de eventos recurrentes.

    Objetivos del Producto: Proporcionar una forma sencilla de identificar la semana del mes,
    con la flexibilidad de definir el día de inicio de la semana.

    Descripción: Esta función calcula el número de la semana del mes para `date_input`.
    La semana 1 comienza con el primer día del mes. Las semanas subsiguientes se cuentan
    basándose en el `start_of_week` especificado. Por defecto, `start_of_week` es 0 (lunes).
    Es decir, si el primer día del mes es un miércoles y `start_of_week` es lunes,
    la semana 1 incluirá ese miércoles y la semana 2 comenzará el primer lunes completo
    después del día 1 del mes.

    Args:
        date_input (datetime): La fecha para la cual se desea obtener el número de semana del mes.
        start_of_week (int, optional): El día en que comienza la semana (0=Lunes, 6=Domingo).
                                        Por defecto es 0 (Lunes).

    Returns:
        int: El número de la semana del mes (1-5 o 1-6, dependiendo de la configuración y el mes).

    Raises:
        TypeError: Si `date_input` no es un objeto `datetime` o si `start_of_week` no es un entero.
        ValueError: Si `start_of_week` está fuera del rango válido (0-6).

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Fecha en medio del mes (Lunes como inicio de semana por defecto)
        >>> week_of_month(datetime(2025, 6, 11)) # 11 de junio de 2025 es miércoles
        2 # La semana 1 comienza el 1 de junio (domingo), la semana 2 el 2 de junio (lunes).

        >>> # Ejemplo 2: Principio de mes (Lunes como inicio de semana)
        >>> week_of_month(datetime(2025, 6, 1)) # 1 de junio de 2025 es domingo
        1

        >>> # Ejemplo 3: Final de mes (Lunes como inicio de semana)
        >>> week_of_month(datetime(2025, 6, 30)) # 30 de junio de 2025 es lunes
        5

        >>> # Ejemplo 4: Configurando el Domingo como inicio de semana
        >>> week_of_month(datetime(2025, 6, 11), start_of_week=6) # 11 de junio de 2025 es miércoles
        3 # La semana 1 comienza el 1 de junio (domingo), la semana 2 el 8 de junio (domingo).

        >>> # Ejemplo 5: Tipo de dato incorrecto
        >>> try:
        >>>     week_of_month("not a date")
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: date_input must be a datetime object.

        >>> # Ejemplo 6: start_of_week fuera de rango
        >>> try:
        >>>     week_of_month(datetime(2025, 1, 1), start_of_week=7)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: start_of_week must be an integer between 0 (Monday) and 6 (Sunday).
    """
    if not isinstance(date_input, datetime):
        raise TypeError("date_input must be a datetime object.")
    if not isinstance(start_of_week, int):
        raise TypeError("start_of_week must be an integer.")
    if not (0 <= start_of_week <= 6):
        raise ValueError("start_of_week must be an integer between 0 (Monday) and 6 (Sunday).")

    # Obtener el primer día del mes de la fecha de entrada
    first_day_of_month = date_input.replace(day=1)

    # Calcular el desfase para que el primer día del mes "caiga" en el inicio de la semana.
    # weekday() devuelve 0 para lunes, 6 para domingo.
    # Si start_of_week es lunes (0), y first_day_of_month es miércoles (2),
    # then (2 - 0 + 7) % 7 = 2. Esto significa que el primer día del mes está 2 días después de un lunes.
    # Para que la semana 1 empiece "en" el inicio de semana, necesitamos retroceder los días necesarios.
    offset_to_first_start_of_week = (first_day_of_month.weekday() - start_of_week + 7) % 7

    # Calcular la fecha del "primer día de la primera semana del mes" (puede ser del mes anterior)
    first_day_of_first_week = first_day_of_month - timedelta(days=offset_to_first_start_of_week)

    # Calcular la diferencia en días desde ese "primer día de la primera semana" hasta la fecha_input
    days_since_first_week_start = (date_input.date() - first_day_of_first_week).days

    # Calcular el número de semana. Sumamos 1 porque las semanas empiezan en 1.
    # Dividimos por 7 y usamos el techo para obtener el número de semana.
    week_number = (days_since_first_week_start // 7) + 1

    return week_number


def filter_dates_by_weekday(dates: List[datetime], weekday: int) -> List[datetime]:
    """Filtra una lista de fechas, devolviendo solo aquellas que caen en un día específico de la semana.

    Args:
        dates (List[datetime]): Una lista de objetos datetime.
        weekday (int): El día de la semana a filtrar (0=Lunes, 6=Domingo).

    Returns:
        List[datetime]: Una nueva lista que contiene solo las fechas que coinciden con el día de la semana especificado.

    Raises:
        TypeError: Si 'dates' no es una lista, si contiene elementos que no son datetime,
                   o si 'weekday' no es un entero.
        ValueError: Si 'weekday' está fuera del rango válido (0-6).

    Example:
        >>> from datetime import datetime
        >>> # Definir algunas fechas
        >>> date_list = [
        ...     datetime(2025, 6, 9),  # Lunes
        ...     datetime(2025, 6, 10), # Martes
        ...     datetime(2025, 6, 11), # Miércoles
        ...     datetime(2025, 6, 12), # Jueves
        ...     datetime(2025, 6, 16), # Lunes
        ...     datetime(2025, 6, 17), # Martes
        ...     datetime(2025, 6, 15), # Domingo
        ... ]

        >>> # Filtrar fechas que caen en Lunes (0)
        >>> monday_dates = filter_dates_by_weekday(date_list, 0)
        >>> print(monday_dates)
        [datetime.datetime(2025, 6, 9, 0, 0), datetime.datetime(2025, 6, 16, 0, 0)]

        >>> # Filtrar fechas que caen en Martes (1)
        >>> tuesday_dates = filter_dates_by_weekday(date_list, 1)
        >>> print(tuesday_dates)
        [datetime.datetime(2025, 6, 10, 0, 0), datetime.datetime(2025, 6, 17, 0, 0)]

        >>> # Filtrar fechas que caen en Sábado (5) - ninguna en la lista
        >>> saturday_dates = filter_dates_by_weekday(date_list, 5)
        >>> print(saturday_dates)
        []

        >>> # Lista vacía como entrada
        >>> filter_dates_by_weekday([], 0)
        []

        >>> # Tipo de dato incorrecto en la lista (levantará TypeError)
        >>> try:
        >>>     filter_dates_by_weekday([datetime(2025, 1, 1), "not a date"], 0)
        >>> except TypeError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: All elements in 'dates' must be datetime objects.

        >>> # 'weekday' fuera de rango (levantará ValueError)
        >>> try:
        >>>     filter_dates_by_weekday(date_list, 7)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Salida esperada: Error: 'weekday' must be an integer between 0 (Monday) and 6 (Sunday).
    """
    if not isinstance(dates, list):
        raise TypeError("'dates' must be a list.")
    if not isinstance(weekday, int):
        raise TypeError("'weekday' must be an integer.")
    if not (0 <= weekday <= 6):
        raise ValueError("'weekday' must be an integer between 0 (Monday) and 6 (Sunday).")

    filtered_dates: List[datetime] = []
    for date_obj in dates:
        if not isinstance(date_obj, datetime):
            raise TypeError("All elements in 'dates' must be datetime objects.")
        
        # El método .weekday() de datetime devuelve el día de la semana como un entero,
        # donde 0 es lunes y 6 es domingo.
        if date_obj.weekday() == weekday:
            filtered_dates.append(date_obj)
            
    return filtered_dates


def days_360(start_date: datetime, end_date: datetime, method: str = 'us') -> int:
    """Calculates days between two dates based on a 360-day year (12 months of 30 days).

    Description:
        Commonly used in financial calculations (bond pricing, interest accrual).
        Two methods are supported: US (NASD) and European.

    Args:
        start_date: The start date.
        end_date: The end date.
        method: Calculation method — 'us' for US/NASD or 'eu' for European.
                Defaults to 'us'.

    Returns:
        int: Number of days based on the 360-day year convention.

    Raises:
        TypeError: If start_date or end_date are not datetime objects.
        ValueError: If method is not 'us' or 'eu'.

    Example:
        >>> from datetime import datetime
        >>> days_360(datetime(2025, 1, 30), datetime(2025, 2, 28))
        28
        >>> days_360(datetime(2025, 1, 1), datetime(2025, 7, 1))
        180

    Complexity: O(1)
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    method = method.lower()

    if method not in ('us', 'eu'):
        raise ValueError("method must be 'us' or 'eu'.")

    if method == 'eu':
        day1 = min(start_date.day, 30)
        day2 = min(end_date.day, 30)
    else:
        day1 = start_date.day if start_date.day < 31 else 30
        day2 = end_date.day

        if end_date.day == 31 and start_date.day >= 30:
            day2 = 30

    return (
        (end_date.year - start_date.year) * 360
        + (end_date.month - start_date.month) * 30
        + (day2 - day1)
    )


def network_days_intl(
    start_date: datetime,
    end_date: datetime,
    weekend: Union[int, str] = 1,
    holidays: Optional[List[datetime]] = None
) -> int:
    """Calculates working days between two dates with custom weekend definition.

    Description:
        Extension of get_working_days_in_range that allows specifying which days
        are considered weekends. Weekend can be an integer preset (1-7) or a
        7-character string of 0s/1s (Monday-Sunday, 1 = weekend day).

    Args:
        start_date: The start date (inclusive).
        end_date: The end date (inclusive).
        weekend: Weekend definition. Integer presets:
                 1 = Sat-Sun (default), 2 = Sun-Mon, 3 = Mon-Tue,
                 4 = Tue-Wed, 5 = Wed-Thu, 6 = Thu-Fri, 7 = Fri-Sat.
                 Or a 7-char string of 0/1 (Mon-Sun), e.g. '0000011' = Sat-Sun.
        holidays: Optional list of holiday datetimes to exclude.

    Returns:
        int: Number of working days.

    Raises:
        TypeError: If dates are not datetime objects.
        ValueError: If start_date > end_date or weekend value is invalid.

    Example:
        >>> from datetime import datetime
        >>> network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 10))
        5
        >>> network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 12), weekend='0000011')
        5

    Complexity: O(n) where n is the number of days in the range
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    if start_date > end_date:
        raise ValueError("start_date cannot be after end_date.")

    weekend_days = _resolve_weekend_days(weekend)
    holiday_set = _build_holiday_set(holidays)

    count = 0
    current = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end = end_date.replace(hour=0, minute=0, second=0, microsecond=0)

    while current <= end:

        if current.weekday() not in weekend_days and current.date() not in holiday_set:
            count += 1

        current += timedelta(days=1)

    return count


def workday(
    start_date: datetime,
    days: int,
    holidays: Optional[List[datetime]] = None
) -> datetime:
    """Returns the date after a given number of working days (Mon-Fri).

    Description:
        Starting from start_date, counts forward (positive days) or backward
        (negative days), skipping weekends (Saturday/Sunday) and optional
        holidays. The start_date itself is not counted.

    Args:
        start_date: The starting date.
        days: Number of working days to advance (positive) or go back (negative).
        holidays: Optional list of holiday datetimes to skip.

    Returns:
        datetime: The resulting date after the specified working days.

    Raises:
        TypeError: If start_date is not a datetime or days is not an int.

    Example:
        >>> from datetime import datetime
        >>> workday(datetime(2025, 1, 6), 5)  # Mon + 5 working days = Mon
        datetime.datetime(2025, 1, 13, 0, 0)
        >>> workday(datetime(2025, 1, 6), -1)
        datetime.datetime(2025, 1, 3, 0, 0)

    Complexity: O(n) where n is abs(days)
    """
    if not isinstance(start_date, datetime):
        raise TypeError("start_date must be a datetime object.")

    if not isinstance(days, int):
        raise TypeError("days must be an integer.")

    holiday_set = _build_holiday_set(holidays)
    step = 1 if days >= 0 else -1
    remaining = abs(days)
    current = start_date

    while remaining > 0:
        current += timedelta(days=step)

        if current.weekday() < 5 and current.date() not in holiday_set:
            remaining -= 1

    return current.replace(hour=0, minute=0, second=0, microsecond=0)


def workday_intl(
    start_date: datetime,
    days: int,
    weekend: Union[int, str] = 1,
    holidays: Optional[List[datetime]] = None
) -> datetime:
    """Returns the date after a given number of working days with custom weekends.

    Description:
        Like workday but allows specifying which days count as weekends via
        the same convention as network_days_intl.

    Args:
        start_date: The starting date.
        days: Number of working days to advance (positive) or go back (negative).
        weekend: Weekend definition (see network_days_intl for details).
        holidays: Optional list of holiday datetimes to skip.

    Returns:
        datetime: The resulting date.

    Raises:
        TypeError: If start_date is not a datetime or days is not an int.

    Example:
        >>> from datetime import datetime
        >>> workday_intl(datetime(2025, 1, 6), 5, weekend=2)
        datetime.datetime(2025, 1, 14, 0, 0)

    Complexity: O(n) where n is abs(days)
    """
    if not isinstance(start_date, datetime):
        raise TypeError("start_date must be a datetime object.")

    if not isinstance(days, int):
        raise TypeError("days must be an integer.")

    weekend_days = _resolve_weekend_days(weekend)
    holiday_set = _build_holiday_set(holidays)
    step = 1 if days >= 0 else -1
    remaining = abs(days)
    current = start_date

    while remaining > 0:
        current += timedelta(days=step)

        if current.weekday() not in weekend_days and current.date() not in holiday_set:
            remaining -= 1

    return current.replace(hour=0, minute=0, second=0, microsecond=0)


def year_fraction(start_date: datetime, end_date: datetime, basis: int = 0) -> float:
    """Calculates the fraction of year between two dates.

    Description:
        Useful for financial calculations such as bond accrued interest or
        prorated payments. Supports two day-count conventions.

    Args:
        start_date: The start date.
        end_date: The end date.
        basis: Day-count basis.
               0 = US 30/360 (default), 1 = Actual/Actual.

    Returns:
        float: Fraction of the year between the dates.

    Raises:
        TypeError: If dates are not datetime objects.
        ValueError: If basis is not 0 or 1.

    Example:
        >>> from datetime import datetime
        >>> year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=0)
        0.5
        >>> year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=1)
        0.4958904109589041

    Complexity: O(1)
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    if basis not in (0, 1):
        raise ValueError("basis must be 0 (US 30/360) or 1 (Actual/Actual).")

    if basis == 0:
        numerator = days_360(start_date, end_date, method='us')
        return numerator / 360
    else:
        actual_days = (end_date - start_date).days

        if start_date.year == end_date.year:
            year_days = 366 if calendar.isleap(start_date.year) else 365
        else:
            year_days = 365.25

        return actual_days / year_days


def week_number(date_input: datetime, system: int = 1) -> int:
    """Returns the week number of the year for a given date.

    Description:
        Standalone convenience function to get the week number. Supports
        two systems: week starting on Sunday (system 1) or ISO standard
        (system 21, week starting on Monday with ISO rules).

    Args:
        date_input: The date to evaluate.
        system: 1 = week begins on Sunday (default), 21 = ISO week number.

    Returns:
        int: Week number (1-53).

    Raises:
        TypeError: If date_input is not a datetime object.
        ValueError: If system is not 1 or 21.

    Example:
        >>> from datetime import datetime
        >>> week_number(datetime(2025, 1, 1))
        1
        >>> week_number(datetime(2025, 1, 1), system=21)
        1

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("date_input must be a datetime object.")

    if system not in (1, 21):
        raise ValueError("system must be 1 (Sunday start) or 21 (ISO).")

    if system == 21:
        return date_input.isocalendar()[1]

    # System 1: week starts on Sunday
    # Jan 1 is always in week 1; week increments each Sunday
    jan1 = datetime(date_input.year, 1, 1)
    jan1_weekday = (jan1.weekday() + 1) % 7  # Sunday=0
    day_of_year = date_input.timetuple().tm_yday
    return (day_of_year + jan1_weekday - 1) // 7 + 1


def iso_week_number(date_input: datetime) -> int:
    """Returns the ISO 8601 week number for a given date.

    Description:
        The ISO week number ranges from 1 to 53. Week 1 is the week
        containing the first Thursday of the year.

    Args:
        date_input: The date to evaluate.

    Returns:
        int: ISO week number (1-53).

    Raises:
        TypeError: If date_input is not a datetime object.

    Example:
        >>> from datetime import datetime
        >>> iso_week_number(datetime(2025, 1, 1))
        1
        >>> iso_week_number(datetime(2025, 6, 15))
        24

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("date_input must be a datetime object.")

    return date_input.isocalendar()[1]


def quarters_between_dates(start_date: datetime, end_date: datetime) -> int:
    """Calculates the number of complete quarters between two dates.

    Description:
        Returns the whole-quarter difference. A positive result means end_date
        is after start_date; negative means it is before.

    Args:
        start_date: The start date.
        end_date: The end date.

    Returns:
        int: Number of quarters between the dates.

    Raises:
        TypeError: If start_date or end_date are not datetime objects.

    Example:
        >>> from datetime import datetime
        >>> quarters_between_dates(datetime(2025, 1, 1), datetime(2025, 10, 1))
        3
        >>> quarters_between_dates(datetime(2025, 1, 15), datetime(2025, 4, 14))
        0

    Complexity: O(1)
    """
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")

    total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    # Adjust for incomplete month if day hasn't been reached
    if end_date.day < start_date.day:
        total_months -= 1 if total_months > 0 else 0

        if total_months < 0:
            total_months += 1

    # Integer division gives complete quarters
    return total_months // 3


def add_months(date_input: datetime, months: int) -> datetime:
    """Shifts a date forward or backward by a given number of months.

    Description:
        Preserves the day-of-month when possible. If the target month has fewer
        days than the original day (e.g. Jan 31 + 1 month), clamps to the last
        day of the target month.

    Args:
        date_input: The starting date.
        months: Number of months to add (positive) or subtract (negative).

    Returns:
        datetime: The resulting date with time components preserved.

    Raises:
        TypeError: If date_input is not a datetime or months is not an int.

    Example:
        >>> from datetime import datetime
        >>> add_months(datetime(2025, 1, 31), 1)
        datetime.datetime(2025, 2, 28, 0, 0)
        >>> add_months(datetime(2025, 3, 15), -1)
        datetime.datetime(2025, 2, 15, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("date_input must be a datetime object.")

    if not isinstance(months, int):
        raise TypeError("months must be an integer.")

    target_year = date_input.year + (date_input.month + months - 1) // 12
    target_month = (date_input.month + months - 1) % 12 + 1
    max_day = calendar.monthrange(target_year, target_month)[1]
    target_day = min(date_input.day, max_day)

    return date_input.replace(year=target_year, month=target_month, day=target_day)


def start_of_quarter(date_input: Union[datetime, str], input_format: Optional[str] = None) -> datetime:
    """Returns the first day of the quarter for a given date.

    Description:
        Determines which quarter the date belongs to and returns the first
        day of that quarter at 00:00:00.

    Args:
        date_input: The date for which to get the start of the quarter.
        input_format: Format string if date_input is a string.

    Returns:
        datetime: First day of the quarter at midnight.

    Raises:
        TypeError: If date_input is not a datetime or string.
        ValueError: If date_input is a string and input_format is not provided.

    Example:
        >>> from datetime import datetime
        >>> start_of_quarter(datetime(2026, 8, 15))
        datetime.datetime(2026, 7, 1, 0, 0)
        >>> start_of_quarter(datetime(2026, 1, 20))
        datetime.datetime(2026, 1, 1, 0, 0)

    Complexity: O(1)
    """
    parsed_dt = _parse_date_input_internal(date_input, input_format)
    quarter = (parsed_dt.month - 1) // 3
    first_month = quarter * 3 + 1

    return datetime(parsed_dt.year, first_month, 1, 0, 0, 0)


def end_of_quarter(date_input: Union[datetime, str], input_format: Optional[str] = None) -> datetime:
    """Returns the last day of the quarter for a given date.

    Description:
        Determines which quarter the date belongs to and returns the last
        day of that quarter at 23:59:59.999999.

    Args:
        date_input: The date for which to get the end of the quarter.
        input_format: Format string if date_input is a string.

    Returns:
        datetime: Last day of the quarter at 23:59:59.999999.

    Raises:
        TypeError: If date_input is not a datetime or string.
        ValueError: If date_input is a string and input_format is not provided.

    Example:
        >>> from datetime import datetime
        >>> end_of_quarter(datetime(2026, 8, 15))
        datetime.datetime(2026, 9, 30, 23, 59, 59, 999999)
        >>> end_of_quarter(datetime(2026, 1, 20))
        datetime.datetime(2026, 3, 31, 23, 59, 59, 999999)

    Complexity: O(1)
    """
    parsed_dt = _parse_date_input_internal(date_input, input_format)
    quarter = (parsed_dt.month - 1) // 3
    last_month = quarter * 3 + 3
    last_day = calendar.monthrange(parsed_dt.year, last_month)[1]

    return datetime(parsed_dt.year, last_month, last_day, 23, 59, 59, 999999)


def end_of_month_offset(date_input: datetime, months: int) -> datetime:
    """Returns the last day of the month that is N months from date_input.

    Description:
        Useful for calculating payment due dates, contract expirations, or
        any scenario requiring the last calendar day of a future/past month.

    Args:
        date_input: The reference date.
        months: Number of months to offset (positive = forward, negative = back).

    Returns:
        datetime: A datetime set to the last day of the target month at 23:59:59.999999.

    Raises:
        TypeError: If date_input is not a datetime or months is not an int.

    Example:
        >>> from datetime import datetime
        >>> end_of_month_offset(datetime(2025, 1, 15), 0)
        datetime.datetime(2025, 1, 31, 23, 59, 59, 999999)
        >>> end_of_month_offset(datetime(2025, 1, 15), 1)
        datetime.datetime(2025, 2, 28, 23, 59, 59, 999999)
        >>> end_of_month_offset(datetime(2024, 1, 15), 1)
        datetime.datetime(2024, 2, 29, 23, 59, 59, 999999)

    Complexity: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("date_input must be a datetime object.")

    if not isinstance(months, int):
        raise TypeError("months must be an integer.")

    target_year = date_input.year + (date_input.month + months - 1) // 12
    target_month = (date_input.month + months - 1) % 12 + 1
    last_day = calendar.monthrange(target_year, target_month)[1]

    return datetime(target_year, target_month, last_day, 23, 59, 59, 999999)


def date_range(
    start: Union[datetime, str, date],
    end: Union[datetime, str, date],
    step: int = 1,
    unit: str = 'days',
) -> List[datetime]:
    """Generates a list of dates between *start* and *end* at regular intervals.

    Args:
        start: Start date (inclusive). Accepts datetime, date, or ISO string.
        end: End date (inclusive). Accepts datetime, date, or ISO string.
        step: Number of *unit* between each generated date. Must be positive.
        unit: Time unit for the step. Supported: 'days', 'weeks', 'hours',
              'minutes', 'seconds'.

    Returns:
        List of datetime objects from *start* up to (and including) *end*.

    Raises:
        TypeError: If inputs cannot be converted to datetime.
        ValueError: If *step* < 1 or *unit* is unsupported.

    Example:
        >>> from datetime import datetime
        >>> date_range(datetime(2025, 1, 1), datetime(2025, 1, 5))
        [datetime.datetime(2025, 1, 1, 0, 0), datetime.datetime(2025, 1, 2, 0, 0), datetime.datetime(2025, 1, 3, 0, 0), datetime.datetime(2025, 1, 4, 0, 0), datetime.datetime(2025, 1, 5, 0, 0)]
        >>> date_range("2025-01-01", "2025-01-10", step=3, unit='days')
        [datetime.datetime(2025, 1, 1, 0, 0), datetime.datetime(2025, 1, 4, 0, 0), datetime.datetime(2025, 1, 7, 0, 0), datetime.datetime(2025, 1, 10, 0, 0)]

    Complexity: O(n) where n is the number of dates produced.
    """
    if not isinstance(step, int) or step < 1:
        raise ValueError("step must be a positive integer.")

    unit_map = {
        'days': 'days',
        'weeks': 'weeks',
        'hours': 'hours',
        'minutes': 'minutes',
        'seconds': 'seconds',
    }

    key = unit.lower()

    if key not in unit_map:
        raise ValueError(
            f"Unsupported unit '{unit}'. Use one of: {', '.join(unit_map)}."
        )

    parsed_start = string_to_date(start)
    parsed_end = string_to_date(end)

    if parsed_start is None:
        raise TypeError(f"Could not parse start date: {start}")

    if parsed_end is None:
        raise TypeError(f"Could not parse end date: {end}")

    # Normalise date -> datetime
    if isinstance(parsed_start, date) and not isinstance(parsed_start, datetime):
        parsed_start = datetime(parsed_start.year, parsed_start.month, parsed_start.day)

    if isinstance(parsed_end, date) and not isinstance(parsed_end, datetime):
        parsed_end = datetime(parsed_end.year, parsed_end.month, parsed_end.day)

    delta = timedelta(**{unit_map[key]: step})
    result: List[datetime] = []
    current = parsed_start

    while current <= parsed_end:
        result.append(current)
        current += delta

    return result


def easter_date(year: int) -> date:
    """Computes the date of Easter Sunday for a given year.

    Uses the Anonymous Gregorian algorithm (Meeus/Jones/Butcher) which is
    valid for years in the Gregorian calendar.

    Args:
        year: The calendar year (e.g. 2025).

    Returns:
        A ``date`` object for Easter Sunday.

    Raises:
        TypeError: If *year* is not an integer.
        ValueError: If *year* < 1.

    Example:
        >>> easter_date(2025)
        datetime.date(2025, 4, 20)
        >>> easter_date(2024)
        datetime.date(2024, 3, 31)
        >>> easter_date(2000)
        datetime.date(2000, 4, 23)

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    if year < 1:
        raise ValueError("year must be a positive integer.")

    # Anonymous Gregorian algorithm
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    el = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * el) // 451
    month, day = divmod(h + el - 7 * m + 114, 31)

    return date(year, month, day + 1)


# --- Private helpers for weekend/holiday resolution ---

def _build_holiday_set(holidays: Optional[List[datetime]]) -> Set[date]:
    """Converts optional list of datetime holidays to a set of date objects.

    Args:
        holidays: Optional list of datetime objects.

    Returns:
        Set of date objects for efficient lookup.

    Raises:
        TypeError: If holidays is not a list of datetime objects.
    """
    if holidays is None:
        return set()

    if not isinstance(holidays, list):
        raise TypeError("holidays must be a list of datetime objects or None.")

    result: Set[date] = set()

    for h in holidays:

        if not isinstance(h, datetime):
            raise TypeError("All items in holidays must be datetime objects.")

        result.add(h.date())

    return result


def _resolve_weekend_days(weekend: Union[int, str]) -> Set[int]:
    """Resolves weekend parameter into a set of weekday indices (0=Mon, 6=Sun).

    Args:
        weekend: Integer preset (1-7) or 7-char string of 0/1 (Mon-Sun).

    Returns:
        Set of weekday integers considered as weekend days.

    Raises:
        ValueError: If the weekend value is not recognized.
    """
    if isinstance(weekend, int):
        presets = {
            1: {5, 6},  # Sat-Sun
            2: {6, 0},  # Sun-Mon
            3: {0, 1},  # Mon-Tue
            4: {1, 2},  # Tue-Wed
            5: {2, 3},  # Wed-Thu
            6: {3, 4},  # Thu-Fri
            7: {4, 5},  # Fri-Sat
        }

        if weekend not in presets:
            raise ValueError("weekend integer must be between 1 and 7.")

        return presets[weekend]

    if isinstance(weekend, str):

        if len(weekend) != 7 or not all(c in '01' for c in weekend):
            raise ValueError("weekend string must be 7 characters of '0' and '1' (Mon-Sun).")

        return {i for i, ch in enumerate(weekend) if ch == '1'}

    raise ValueError("weekend must be an integer (1-7) or a 7-character '0'/'1' string.")


def age(birthdate: Union[str, date, datetime]) -> int:
    """Calculates the age in complete years from a birth date to today.

    Args:
        birthdate: A date, datetime, or parseable date string.

    Returns:
        The number of complete years elapsed.

    Raises:
        TypeError: If birthdate cannot be interpreted as a date.
        ValueError: If birthdate is in the future.

    Example:
        >>> from datetime import date
        >>> age(date(2000, 1, 1))  # assuming today is 2026-04-04
        26

    Complexity: O(1)
    """
    if isinstance(birthdate, str):
        birthdate = string_to_date(birthdate)

    if isinstance(birthdate, datetime):
        birthdate = birthdate.date()

    if not isinstance(birthdate, date):
        raise TypeError("birthdate must be a date, datetime, or date string.")

    today = date.today()

    if birthdate > today:
        raise ValueError("birthdate cannot be in the future.")

    years = today.year - birthdate.year

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1

    return years


def overlap_dates(
    start1: Union[str, date, datetime],
    end1: Union[str, date, datetime],
    start2: Union[str, date, datetime],
    end2: Union[str, date, datetime],
) -> bool:
    """Checks whether two date ranges overlap.

    Two ranges overlap when one starts before the other ends, and vice versa.

    Args:
        start1: Start of the first range.
        end1: End of the first range.
        start2: Start of the second range.
        end2: End of the second range.

    Returns:
        True if the ranges share at least one common day.

    Example:
        >>> from datetime import date
        >>> overlap_dates(date(2026, 1, 1), date(2026, 1, 10), date(2026, 1, 5), date(2026, 1, 15))
        True
        >>> overlap_dates(date(2026, 1, 1), date(2026, 1, 10), date(2026, 1, 11), date(2026, 1, 20))
        False

    Complexity: O(1)
    """
    def _to_date(d: Union[str, date, datetime]) -> date:
        if isinstance(d, str):
            d = string_to_date(d)

        if isinstance(d, datetime):
            return d.date()

        return d

    s1, e1, s2, e2 = _to_date(start1), _to_date(end1), _to_date(start2), _to_date(end2)
    return s1 <= e2 and s2 <= e1


def relative_time_description(
    dt_value: datetime,
    reference: Optional[datetime] = None,
    language: str = "en",
) -> str:
    """Returns a human-readable relative time string.

    Computes the difference between *dt_value* and *reference* and produces
    a short description such as ``"2 hours ago"`` or ``"hace 3 dias"``.

    Args:
        dt_value: The target datetime.
        reference: The baseline datetime (defaults to ``datetime.now()``).
        language: ``"en"`` for English, ``"es"`` for Spanish.

    Returns:
        A human-readable relative time string.

    Raises:
        TypeError: If *dt_value* is not a datetime.

    Example:
        >>> from datetime import datetime, timedelta
        >>> ref = datetime(2026, 4, 4, 12, 0)
        >>> relative_time_description(ref - timedelta(hours=2), ref)
        '2 hours ago'

    Complexity: O(1)
    """
    if not isinstance(dt_value, datetime):
        raise TypeError("dt_value must be a datetime object.")

    if reference is None:
        reference = datetime.now()

    delta = dt_value - reference
    total_seconds = int(delta.total_seconds())
    is_future = total_seconds >= 0
    total_seconds = abs(total_seconds)

    units_en = [
        (86400 * 365, "year", "years"),
        (86400 * 30, "month", "months"),
        (86400, "day", "days"),
        (3600, "hour", "hours"),
        (60, "minute", "minutes"),
        (1, "second", "seconds"),
    ]
    units_es = [
        (86400 * 365, "a\u00f1o", "a\u00f1os"),
        (86400 * 30, "mes", "meses"),
        (86400, "d\u00eda", "d\u00edas"),
        (3600, "hora", "horas"),
        (60, "minuto", "minutos"),
        (1, "segundo", "segundos"),
    ]
    units = units_es if language == "es" else units_en

    for threshold, singular, plural in units:

        if total_seconds >= threshold:
            count = total_seconds // threshold
            name = singular if count == 1 else plural

            if is_future:
                return f"en {count} {name}" if language == "es" else f"in {count} {name}"

            return f"hace {count} {name}" if language == "es" else f"{count} {name} ago"

    if language == "es":
        return "ahora mismo"

    return "just now"


def round_datetime(
    dt_value: datetime,
    unit: Literal["minute", "hour", "day"] = "hour",
) -> datetime:
    """Rounds a datetime to the nearest unit.

    Args:
        dt_value: The datetime to round.
        unit: ``"minute"``, ``"hour"`` or ``"day"``.

    Returns:
        The rounded datetime.

    Raises:
        TypeError: If *dt_value* is not a datetime.
        ValueError: If *unit* is invalid.

    Example:
        >>> round_datetime(datetime(2026, 4, 4, 14, 35), "hour")
        datetime.datetime(2026, 4, 4, 15, 0)

    Complexity: O(1)
    """
    if not isinstance(dt_value, datetime):
        raise TypeError("dt_value must be a datetime object.")

    if unit == "minute":

        if dt_value.second >= 30:
            dt_value += timedelta(minutes=1)

        return dt_value.replace(second=0, microsecond=0)

    if unit == "hour":

        if dt_value.minute >= 30:
            dt_value += timedelta(hours=1)

        return dt_value.replace(minute=0, second=0, microsecond=0)

    if unit == "day":

        if dt_value.hour >= 12:
            dt_value += timedelta(days=1)

        return dt_value.replace(hour=0, minute=0, second=0, microsecond=0)

    raise ValueError(f"Invalid unit '{unit}'. Use 'minute', 'hour' or 'day'.")


def recurring_dates(
    start: date,
    end: date,
    frequency: Literal["daily", "weekly", "biweekly", "monthly", "yearly"] = "monthly",
    weekday: Optional[int] = None,
) -> List[date]:
    """Generates recurring dates within a range.

    Args:
        start: First date of the range (inclusive).
        end: Last date of the range (inclusive).
        frequency: One of ``"daily"``, ``"weekly"``, ``"biweekly"``,
            ``"monthly"`` or ``"yearly"``.
        weekday: For ``"weekly"``/``"biweekly"`` -- ISO weekday
            (1=Monday ... 7=Sunday). Defaults to the weekday of *start*.

    Returns:
        A sorted list of dates matching the recurrence rule.

    Raises:
        ValueError: If *start* > *end* or frequency is invalid.

    Example:
        >>> from datetime import date
        >>> recurring_dates(date(2026, 1, 1), date(2026, 3, 1), "monthly")
        [datetime.date(2026, 1, 1), datetime.date(2026, 2, 1), datetime.date(2026, 3, 1)]

    Complexity: O(n) where n is the number of occurrences.
    """
    if start > end:
        raise ValueError("start must be <= end.")

    result: List[date] = []

    if frequency == "daily":
        current = start

        while current <= end:
            result.append(current)
            current += timedelta(days=1)

    elif frequency in ("weekly", "biweekly"):
        step = 7 if frequency == "weekly" else 14
        target_wd = (weekday or start.isoweekday()) % 7
        current_wd = start.isoweekday() % 7
        offset = (target_wd - current_wd) % 7
        current = start + timedelta(days=offset)

        while current <= end:
            result.append(current)
            current += timedelta(days=step)

    elif frequency == "monthly":
        current = start

        while current <= end:
            result.append(current)
            month = current.month + 1
            year = current.year

            if month > 12:
                month = 1
                year += 1

            day_val = min(start.day, calendar.monthrange(year, month)[1])
            current = date(year, month, day_val)

    elif frequency == "yearly":
        current = start

        while current <= end:
            result.append(current)
            year = current.year + 1
            day_val = min(start.day, calendar.monthrange(year, start.month)[1])
            current = date(year, start.month, day_val)

    else:
        raise ValueError(
            f"Invalid frequency '{frequency}'. Use 'daily', 'weekly', "
            "'biweekly', 'monthly' or 'yearly'."
        )

    return result


def overlap_days(
    start1: date, end1: date,
    start2: date, end2: date,
) -> int:
    """Counts the overlapping days between two date ranges.

    Both ranges are inclusive on both ends.

    Args:
        start1: Start of the first range.
        end1: End of the first range.
        start2: Start of the second range.
        end2: End of the second range.

    Returns:
        Number of overlapping days (0 if no overlap).

    Example:
        >>> from datetime import date
        >>> overlap_days(date(2026, 1, 1), date(2026, 1, 10),
        ...             date(2026, 1, 5), date(2026, 1, 15))
        6

    Complexity: O(1)
    """
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    delta = (overlap_end - overlap_start).days + 1
    return max(delta, 0)


def business_hours_between(
    start_dt: datetime,
    end_dt: datetime,
    work_start: time = time(9, 0),
    work_end: time = time(17, 0),
) -> float:
    """Calculates the number of business hours between two datetimes.

    Counts only Mon--Fri hours within the ``[work_start, work_end)`` window.

    Args:
        start_dt: Start datetime.
        end_dt: End datetime.
        work_start: Daily work-start time (default 09:00).
        work_end: Daily work-end time (default 17:00).

    Returns:
        Total business hours as a float.

    Raises:
        ValueError: If *start_dt* > *end_dt* or *work_start* >= *work_end*.

    Example:
        >>> business_hours_between(
        ...     datetime(2026, 4, 6, 10, 0),
        ...     datetime(2026, 4, 6, 15, 30))
        5.5

    Complexity: O(d) where d is the number of calendar days spanned.
    """
    if start_dt > end_dt:
        raise ValueError("start_dt must be <= end_dt.")

    if work_start >= work_end:
        raise ValueError("work_start must be before work_end.")

    total = 0.0
    current_date = start_dt.date()

    while current_date <= end_dt.date():

        if current_date.weekday() < 5:
            day_start = datetime.combine(current_date, work_start)
            day_end = datetime.combine(current_date, work_end)
            eff_start = max(start_dt, day_start)
            eff_end = min(end_dt, day_end)

            if eff_start < eff_end:
                total += (eff_end - eff_start).total_seconds()

        current_date += timedelta(days=1)

    return round(total / 3600, 2)


# ---------------------------------------------------------------------------
# Human-readable duration & relative time
# ---------------------------------------------------------------------------


def human_readable_duration(seconds: Union[int, float]) -> str:
    """Format a number of seconds as a human-readable duration string.

    Produces compact output like ``"2h 30m 15s"``, ``"3 days 4h"``, or
    ``"1.5s"`` depending on magnitude.

    Args:
        seconds: Total seconds (can be float for sub-second precision).

    Returns:
        Human-readable duration string.

    Example:
        >>> human_readable_duration(9015)
        '2h 30m 15s'
        >>> human_readable_duration(90061)
        '1 day 1h 1m 1s'
        >>> human_readable_duration(45)
        '45s'

    Complexity: O(1)
    """

    if seconds < 0:
        return "-" + human_readable_duration(-seconds)

    if seconds < 1:
        return f"{seconds:.2f}s"

    total = int(seconds)
    days, remainder = divmod(total, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, secs = divmod(remainder, 60)

    parts: List[str] = []

    if days:
        parts.append(f"{days} day{'s' if days != 1 else ''}")

    if hours:
        parts.append(f"{hours}h")

    if minutes:
        parts.append(f"{minutes}m")

    if secs or not parts:
        parts.append(f"{secs}s")

    return " ".join(parts)


def relative_time(dt_input: Union[datetime, date],
                  reference: Optional[Union[datetime, date]] = None,
                  lang: str = "en") -> str:
    """Describe a datetime relative to a reference point.

    Produces output like ``"2 hours ago"``, ``"in 3 days"``,
    ``"hace 2 horas"``, ``"en 3 días"``.

    Args:
        dt_input: Target date/datetime.
        reference: Reference point (defaults to now).
        lang: Language code (``'en'`` or ``'es'``). Defaults to ``'en'``.

    Returns:
        Human-readable relative time string.

    Example:
        >>> from datetime import datetime, timedelta
        >>> ref = datetime(2025, 6, 15, 12, 0, 0)
        >>> relative_time(ref - timedelta(hours=2), ref)
        '2 hours ago'
        >>> relative_time(ref + timedelta(days=3), ref, 'es')
        'en 3 días'

    Complexity: O(1)
    """

    if isinstance(dt_input, date) and not isinstance(dt_input, datetime):
        dt_input = datetime(dt_input.year, dt_input.month, dt_input.day)

    if reference is None:
        reference = datetime.now()
    elif isinstance(reference, date) and not isinstance(reference, datetime):
        reference = datetime(reference.year, reference.month, reference.day)

    delta = dt_input - reference
    total_seconds = delta.total_seconds()
    past = total_seconds < 0
    mag = abs(total_seconds)

    # Determine unit and count
    if mag < 60:
        count, unit_en, unit_es = int(mag), "second", "segundo"
    elif mag < 3600:
        count, unit_en, unit_es = int(mag // 60), "minute", "minuto"
    elif mag < 86400:
        count, unit_en, unit_es = int(mag // 3600), "hour", "hora"
    elif mag < 2_592_000:
        count, unit_en, unit_es = int(mag // 86400), "day", "día"
    elif mag < 31_536_000:
        count, unit_en, unit_es = int(mag // 2_592_000), "month", "mes"
    else:
        count, unit_en, unit_es = int(mag // 31_536_000), "year", "año"

    count = max(count, 1)

    if lang == "es":
        plural = unit_es if count == 1 else (unit_es + "s" if unit_es != "mes" else "meses")

        if past:
            return f"hace {count} {plural}"

        return f"en {count} {plural}"

    # English
    plural = unit_en if count == 1 else unit_en + "s"

    if past:
        return f"{count} {plural} ago"

    return f"in {count} {plural}"


def is_same_business_day(date1: Union[datetime, date],
                         date2: Union[datetime, date],
                         holidays: Optional[List] = None) -> bool:
    """Check whether two dates fall on the same business day.

    A date that falls on a weekend or listed holiday is **not** considered a
    business day, so two dates can only be the "same business day" if they
    share the same calendar date **and** that date is Mon–Fri and not a
    holiday.

    Args:
        date1: First date.
        date2: Second date.
        holidays: Optional list of holiday dates.

    Returns:
        True if both dates share the same business day.

    Example:
        >>> from datetime import date
        >>> is_same_business_day(date(2025, 6, 16), date(2025, 6, 16))
        True
        >>> is_same_business_day(date(2025, 6, 14), date(2025, 6, 14))
        False

    Complexity: O(h) where h = len(holidays)
    """

    d1 = date1.date() if isinstance(date1, datetime) else date1
    d2 = date2.date() if isinstance(date2, datetime) else date2

    if d1 != d2:
        return False

    if d1.weekday() >= 5:
        return False

    if holidays:

        for h in holidays:
            hd = h.date() if isinstance(h, datetime) else h

            if hd == d1:
                return False

    return True


def snap_to_weekday(date_input: Union[datetime, date],
                    target_weekday: int,
                    direction: str = "next") -> Union[datetime, date]:
    """Snap a date to the nearest specified weekday.

    Args:
        date_input: Starting date.
        target_weekday: Target weekday (0=Monday … 6=Sunday).
        direction: ``'next'`` to move forward or ``'previous'`` to move backward.
            If date_input is already on the target weekday, returns as-is.

    Returns:
        Date snapped to the target weekday (same type as input).

    Raises:
        ValueError: If target_weekday is not in [0, 6] or direction is invalid.

    Example:
        >>> from datetime import date
        >>> snap_to_weekday(date(2025, 6, 11), 0)
        datetime.date(2025, 6, 16)
        >>> snap_to_weekday(date(2025, 6, 11), 0, 'previous')
        datetime.date(2025, 6, 9)

    Complexity: O(1)
    """

    if not 0 <= target_weekday <= 6:
        raise ValueError(f"target_weekday ({target_weekday}) must be in [0, 6].")

    if direction not in ("next", "previous"):
        raise ValueError(f"direction must be 'next' or 'previous', got '{direction}'.")

    d = date_input.date() if isinstance(date_input, datetime) else date_input
    current_wd = d.weekday()

    if current_wd == target_weekday:
        return date_input

    if direction == "next":
        days_ahead = (target_weekday - current_wd) % 7

        if days_ahead == 0:
            days_ahead = 7

    else:
        days_back = (current_wd - target_weekday) % 7

        if days_back == 0:
            days_back = 7

        days_ahead = -days_back

    result_date = d + timedelta(days=days_ahead)

    if isinstance(date_input, datetime):
        return datetime.combine(result_date, date_input.time())

    return result_date


def networkdays(
    start_date: Union[date, datetime],
    end_date: Union[date, datetime],
    holidays: Union[List[Union[date, datetime]], None] = None,
) -> int:
    """Counts working days (Mon-Fri) between two dates, excluding holidays.

    Description:
        Returns the number of business days between start_date and end_date,
        both inclusive. Weekends (Saturday, Sunday) and optional holidays are
        excluded. Equivalent to Excel NETWORKDAYS.

    Args:
        start_date: The start date.
        end_date: The end date.
        holidays: Optional list of holiday dates to exclude.

    Returns:
        int: Number of working days.

    Raises:
        TypeError: If dates are not date/datetime objects.

    Example:
        >>> from datetime import date
        >>> networkdays(date(2025, 1, 1), date(2025, 1, 10))
        8
        >>> networkdays(date(2025, 1, 1), date(2025, 1, 10), [date(2025, 1, 6)])
        7

    Complexity: O(n) where n is the number of days in the range
    """
    if isinstance(start_date, datetime):
        start_date = start_date.date()

    if isinstance(end_date, datetime):
        end_date = end_date.date()

    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise TypeError("start_date and end_date must be date or datetime objects.")

    holiday_set: Set[date] = set()

    if holidays:

        for h in holidays:
            holiday_set.add(h.date() if isinstance(h, datetime) else h)

    sign = 1

    if start_date > end_date:
        start_date, end_date = end_date, start_date
        sign = -1

    count = 0
    current = start_date

    while current <= end_date:

        if current.weekday() < 5 and current not in holiday_set:
            count += 1

        current += timedelta(days=1)

    return count * sign


def networkdays_intl(
    start_date: Union[date, datetime],
    end_date: Union[date, datetime],
    weekend: Union[int, str] = 1,
    holidays: Optional[List[Union[date, datetime]]] = None,
) -> int:
    """Counts working days between two dates with custom weekends.

    Description:
        Like networkdays but allows specifying which days count as weekends
        via an integer preset (1-7) or a 7-character binary string.
        Equivalent to Excel NETWORKDAYS.INTL.

    Args:
        start_date: The start date (inclusive).
        end_date: The end date (inclusive).
        weekend: Weekend definition. Integer 1-7 for presets or a 7-char
                 string of '0'/'1' (Mon-Sun) where '1' = weekend day.
        holidays: Optional list of holiday dates to exclude.

    Returns:
        int: Number of working days.

    Raises:
        TypeError: If dates are not date/datetime objects.
        ValueError: If weekend parameter is invalid.

    Example:
        >>> from datetime import date
        >>> networkdays_intl(date(2025, 1, 6), date(2025, 1, 10))
        5
        >>> networkdays_intl(date(2025, 1, 6), date(2025, 1, 10), weekend=2)
        4

    Complexity: O(n) where n is the number of days in the range
    """
    if isinstance(start_date, datetime):
        start_date = start_date.date()

    if isinstance(end_date, datetime):
        end_date = end_date.date()

    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise TypeError("start_date and end_date must be date or datetime objects.")

    weekend_days = _resolve_weekend_days(weekend)

    holiday_set: Set[date] = set()

    if holidays:

        for h in holidays:
            holiday_set.add(h.date() if isinstance(h, datetime) else h)

    sign = 1

    if start_date > end_date:
        start_date, end_date = end_date, start_date
        sign = -1

    count = 0
    current = start_date

    while current <= end_date:

        if current.weekday() not in weekend_days and current not in holiday_set:
            count += 1

        current += timedelta(days=1)

    return count * sign


def datedif(
    start_date: Union[date, datetime],
    end_date: Union[date, datetime],
    unit: str,
) -> int:
    """Calculates the difference between two dates in specified units.

    Description:
        Returns the difference measured in complete years ("Y"), months ("M"),
        days ("D"), months ignoring years ("YM"), days ignoring months and
        years ("MD"), or days ignoring years ("YD").
        Equivalent to Excel DATEDIF.

    Args:
        start_date: The earlier date.
        end_date: The later date.
        unit: One of "Y", "M", "D", "YM", "MD", "YD".

    Returns:
        int: The difference in the requested unit.

    Raises:
        TypeError: If dates are not date/datetime objects.
        ValueError: If start_date > end_date or unit is invalid.

    Example:
        >>> from datetime import date
        >>> datedif(date(2020, 3, 15), date(2025, 7, 20), "Y")
        5
        >>> datedif(date(2020, 3, 15), date(2025, 7, 20), "M")
        64
        >>> datedif(date(2020, 3, 15), date(2025, 7, 20), "D")
        1953

    Complexity: O(1)
    """
    if isinstance(start_date, datetime):
        start_date = start_date.date()

    if isinstance(end_date, datetime):
        end_date = end_date.date()

    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise TypeError("Both dates must be date or datetime objects.")

    if start_date > end_date:
        raise ValueError("start_date must be on or before end_date.")

    unit = unit.upper()

    if unit not in ("Y", "M", "D", "YM", "MD", "YD"):
        raise ValueError("unit must be one of 'Y', 'M', 'D', 'YM', 'MD', 'YD'.")

    if unit == "D":
        return (end_date - start_date).days

    year_diff = end_date.year - start_date.year
    month_diff = end_date.month - start_date.month
    day_diff = end_date.day - start_date.day

    total_months = year_diff * 12 + month_diff

    if day_diff < 0:
        total_months -= 1

    if unit == "Y":
        return total_months // 12

    if unit == "M":
        return total_months

    if unit == "YM":
        return total_months % 12

    if unit == "MD":
        # Days ignoring month and year differences
        if end_date.day >= start_date.day:
            return end_date.day - start_date.day

        prev_month = end_date.month - 1 if end_date.month > 1 else 12
        prev_year = end_date.year if end_date.month > 1 else end_date.year - 1
        days_in_prev = calendar.monthrange(prev_year, prev_month)[1]
        return days_in_prev - start_date.day + end_date.day

    # unit == "YD"
    start_same_year = start_date.replace(year=end_date.year)

    if start_same_year > end_date:
        start_same_year = start_date.replace(year=end_date.year - 1)

    return (end_date - start_same_year).days


def days_between(
    start_date: datetime,
    end_date: datetime,
    basis: int = 0,
) -> int:
    """Calculates days between two dates based on a day-count basis.

    Provides a single implementation for the five standard day-count
    conventions used in financial calculations.

    Args:
        start_date: The start date.
        end_date: The end date.
        basis: Day-count convention:
            0 — 30/360 US (NASD).
            1 — Actual/Actual.
            2 — Actual/360.
            3 — Actual/365.
            4 — 30/360 European.

    Returns:
        Number of days according to the chosen basis.

    Example:
        >>> from datetime import datetime
        >>> days_between(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=0)
        180

    Complexity: O(1)
    """
    if basis == 0:
        return days_360(start_date, end_date, method='us')

    if basis == 4:
        return days_360(start_date, end_date, method='eu')

    # basis 1, 2, 3 — all use actual day count
    return (end_date - start_date).days


def next_business_day(
    d: Union[datetime, date],
    holidays: Optional[List[Union[datetime, date]]] = None,
) -> date:
    """Returns the next business day after the given date.

    Skips weekends (Saturday/Sunday) and optionally provided holidays.

    Args:
        d: Starting date.
        holidays: Optional list of holiday dates to skip.

    Returns:
        The next business day as a date object.

    Raises:
        TypeError: If d is not a date/datetime.

    Example:
        >>> from datetime import date
        >>> next_business_day(date(2026, 4, 3))  # Friday
        datetime.date(2026, 4, 6)
        >>> next_business_day(date(2026, 4, 4))  # Saturday
        datetime.date(2026, 4, 6)

    Complexity: O(h) where h is the number of consecutive holidays.
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime object.")

    from datetime import timedelta

    holiday_set = set()

    if holidays:
        holiday_set = {
            h.date() if isinstance(h, datetime) else h for h in holidays
        }

    current = d.date() if isinstance(d, datetime) else d
    current += timedelta(days=1)

    while current.weekday() >= 5 or current in holiday_set:
        current += timedelta(days=1)

    return current


def previous_business_day(
    d: Union[datetime, date],
    holidays: Optional[List[Union[datetime, date]]] = None,
) -> date:
    """Returns the previous business day before the given date.

    Skips weekends (Saturday/Sunday) and optionally provided holidays.

    Args:
        d: Starting date.
        holidays: Optional list of holiday dates to skip.

    Returns:
        The previous business day as a date object.

    Raises:
        TypeError: If d is not a date/datetime.

    Example:
        >>> from datetime import date
        >>> previous_business_day(date(2026, 4, 6))  # Monday
        datetime.date(2026, 4, 3)
        >>> previous_business_day(date(2026, 4, 5))  # Sunday
        datetime.date(2026, 4, 3)

    Complexity: O(h) where h is the number of consecutive holidays.
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime object.")

    from datetime import timedelta

    holiday_set = set()

    if holidays:
        holiday_set = {
            h.date() if isinstance(h, datetime) else h for h in holidays
        }

    current = d.date() if isinstance(d, datetime) else d
    current -= timedelta(days=1)

    while current.weekday() >= 5 or current in holiday_set:
        current -= timedelta(days=1)

    return current


def date_sequence(
    start: Union[datetime, date],
    end: Union[datetime, date],
    step_days: int = 1,
) -> List[date]:
    """Generates a list of dates from start to end (inclusive).

    Args:
        start: First date in the sequence.
        end: Last date in the sequence (inclusive if reached by step).
        step_days: Number of days between consecutive dates (default 1).

    Returns:
        A list of date objects.

    Raises:
        TypeError: If start/end are not dates or step_days is not int.
        ValueError: If step_days == 0 or step direction doesn't match date order.

    Example:
        >>> from datetime import date
        >>> date_sequence(date(2026, 1, 1), date(2026, 1, 5))
        [datetime.date(2026, 1, 1), datetime.date(2026, 1, 2), datetime.date(2026, 1, 3), datetime.date(2026, 1, 4), datetime.date(2026, 1, 5)]

    Complexity: O(n) where n is the number of dates generated.
    """
    if not isinstance(start, (datetime, date)) or not isinstance(end, (datetime, date)):
        raise TypeError("start and end must be date or datetime objects.")

    if not isinstance(step_days, int):
        raise TypeError("step_days must be an integer.")

    if step_days == 0:
        raise ValueError("step_days cannot be zero.")

    from datetime import timedelta

    s = start.date() if isinstance(start, datetime) else start
    e = end.date() if isinstance(end, datetime) else end

    if step_days > 0 and s > e:
        raise ValueError("start must be <= end when step_days > 0.")

    if step_days < 0 and s < e:
        raise ValueError("start must be >= end when step_days < 0.")

    result = []
    current = s
    delta = timedelta(days=step_days)

    if step_days > 0:

        while current <= e:
            result.append(current)
            current += delta

    else:

        while current >= e:
            result.append(current)
            current += delta

    return result


def fiscal_quarter(
    d: Union[datetime, date],
    fiscal_start_month: int = 1,
) -> int:
    """Returns the fiscal quarter (1-4) for a given date.

    Args:
        d: A datetime or date object.
        fiscal_start_month: The month the fiscal year starts (1-12).
            Default 1 = calendar year.

    Returns:
        An integer 1-4 representing the fiscal quarter.

    Raises:
        TypeError: If d is not a datetime/date or fiscal_start_month not int.
        ValueError: If fiscal_start_month not in 1-12.

    Example:
        >>> from datetime import date
        >>> fiscal_quarter(date(2026, 3, 15))
        1
        >>> fiscal_quarter(date(2026, 3, 15), fiscal_start_month=4)
        4
        >>> fiscal_quarter(date(2026, 7, 1), fiscal_start_month=4)
        2

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("Input must be a datetime or date object.")

    if not isinstance(fiscal_start_month, int):
        raise TypeError("fiscal_start_month must be an integer.")

    if not 1 <= fiscal_start_month <= 12:
        raise ValueError("fiscal_start_month must be between 1 and 12.")

    month = d.month
    adjusted = (month - fiscal_start_month) % 12
    return adjusted // 3 + 1


def countdown_days(
    target: Union[datetime, date],
    from_date: Union[datetime, date, None] = None,
) -> int:
    """Counts the number of days until a target date.

    Positive means target is in the future; negative means it is in the past.

    Args:
        target: The target date.
        from_date: The start date (defaults to today).

    Returns:
        Number of days between from_date and target.

    Raises:
        TypeError: If inputs are not datetime or date objects.

    Example:
        >>> from datetime import date
        >>> countdown_days(date(2026, 12, 31), date(2026, 1, 1))
        364

    Complexity: O(1)
    """
    if not isinstance(target, (datetime, date)):
        raise TypeError("target must be a datetime or date object.")

    if from_date is not None and not isinstance(from_date, (datetime, date)):
        raise TypeError("from_date must be a datetime or date object.")

    t = target.date() if isinstance(target, datetime) else target

    if from_date is None:
        f = date.today()
    else:
        f = from_date.date() if isinstance(from_date, datetime) else from_date

    return (t - f).days


def decimal_hours_between(
    dt1: Union[datetime, date],
    dt2: Union[datetime, date],
) -> float:
    """Returns the decimal number of hours between two datetimes.

    If plain ``date`` objects are given they are treated as midnight.

    Args:
        dt1: Start datetime.
        dt2: End datetime.

    Returns:
        Decimal hours (positive when dt2 > dt1, negative otherwise).

    Raises:
        TypeError: If arguments are not datetime or date.

    Example:
        >>> from datetime import datetime
        >>> decimal_hours_between(
        ...     datetime(2024, 1, 1, 8, 0),
        ...     datetime(2024, 1, 1, 9, 30),
        ... )
        1.5

    Complexity: O(1)
    """
    if not isinstance(dt1, (datetime, date)):
        raise TypeError("dt1 must be a datetime or date object.")

    if not isinstance(dt2, (datetime, date)):
        raise TypeError("dt2 must be a datetime or date object.")

    d1 = dt1 if isinstance(dt1, datetime) else datetime(dt1.year, dt1.month, dt1.day)
    d2 = dt2 if isinstance(dt2, datetime) else datetime(dt2.year, dt2.month, dt2.day)

    return (d2 - d1).total_seconds() / 3600.0


def semester(d: Union[datetime, date, str]) -> int:
    """Returns which semester (1 or 2) a date falls in.

    Semester 1 = January–June, Semester 2 = July–December.

    Args:
        d: A date, datetime, or ISO-format string (``YYYY-MM-DD``).

    Returns:
        ``1`` or ``2``.

    Raises:
        TypeError: If the argument is not a valid date type.

    Example:
        >>> from datetime import date
        >>> semester(date(2024, 3, 15))
        1

    Complexity: O(1)
    """
    if isinstance(d, str):
        d = datetime.strptime(d, "%Y-%m-%d").date()

    if isinstance(d, datetime):
        d = d.date()

    if not isinstance(d, date):
        raise TypeError("d must be a datetime, date, or ISO-format string.")

    return 1 if d.month <= 6 else 2


def elapsed_business_days(
    start: Union[datetime, date],
    end: Union[datetime, date],
    holidays: Optional[List[Union[datetime, date]]] = None,
) -> int:
    """Counts business days (Mon–Fri) between two dates, excluding holidays.

    Both ``start`` and ``end`` are included when counting.

    Args:
        start: Start date (inclusive).
        end: End date (inclusive).
        holidays: Optional list of holiday dates to exclude.

    Returns:
        Number of business days.

    Raises:
        TypeError: If dates are not datetime or date objects.

    Example:
        >>> from datetime import date
        >>> elapsed_business_days(date(2024, 1, 1), date(2024, 1, 5))
        5

    Complexity: O(n) where n is number of days in range
    """
    if not isinstance(start, (datetime, date)):
        raise TypeError("start must be a datetime or date object.")

    if not isinstance(end, (datetime, date)):
        raise TypeError("end must be a datetime or date object.")

    s = start.date() if isinstance(start, datetime) else start
    e = end.date() if isinstance(end, datetime) else end

    if s > e:
        s, e = e, s

    hol_set: set = set()

    if holidays:

        for h in holidays:

            if isinstance(h, datetime):
                hol_set.add(h.date())

            elif isinstance(h, date):
                hol_set.add(h)

    count = 0
    current = s

    while current <= e:

        if current.weekday() < 5 and current not in hol_set:
            count += 1

        current += timedelta(days=1)

    return count


def day_of_year(d: Union[datetime, date]) -> int:
    """Returns the ordinal day of the year (1–366).

    Args:
        d: A date or datetime.

    Returns:
        The day number within the year.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> day_of_year(date(2024, 3, 1))
        61

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a datetime or date object.")

    dt = d.date() if isinstance(d, datetime) else d
    return dt.timetuple().tm_yday


def days_remaining_in_year(d: Union[datetime, date]) -> int:
    """Returns the number of days remaining until 31 December.

    Args:
        d: A date or datetime.

    Returns:
        Days remaining in the year (0 on Dec 31).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> days_remaining_in_year(date(2024, 12, 30))
        1

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a datetime or date object.")

    dt = d.date() if isinstance(d, datetime) else d
    end_of_year = date(dt.year, 12, 31)
    return (end_of_year - dt).days


# ---------------------------------------------------------------------------
# Cron scheduling helpers
# ---------------------------------------------------------------------------

_CRON_MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _cron_field_matches(value: int, field: str, lo: int, hi: int) -> bool:
    """Return True if *value* satisfies a single cron field expression."""

    for part in field.split(","):
        step = 1

        if "/" in part:
            part, step_s = part.split("/", 1)
            step = int(step_s)

        if part == "*":
            rng = range(lo, hi + 1)
        elif "-" in part:
            a, b = part.split("-", 1)
            rng = range(int(a), int(b) + 1)
        else:
            rng = range(int(part), int(part) + 1)

        if value in range(rng.start, rng.stop, step):
            return True

    return False


def cron_next_run(
    cron_expr: str,
    from_dt: Union[datetime, None] = None,
) -> datetime:
    """Returns the next datetime that matches a 5-field cron expression.

    Fields: ``minute hour day month weekday`` (standard POSIX cron,
    weekday 0=Sunday or 0=Monday both accepted via mod-7).

    Args:
        cron_expr: Five space-separated cron fields.
        from_dt: Reference datetime (defaults to now).

    Returns:
        The next matching datetime (seconds/microseconds zeroed).

    Raises:
        TypeError: If cron_expr is not a string.
        ValueError: If cron_expr does not have exactly 5 fields.

    Example:
        >>> from datetime import datetime
        >>> cron_next_run("0 9 * * *", datetime(2026, 4, 8, 10, 0))
        datetime.datetime(2026, 4, 9, 9, 0)

    Complexity: O(k) where k is minutes until next match (bounded by ~1 year)
    """
    if not isinstance(cron_expr, str):
        raise TypeError("cron_expr must be a string")

    fields = cron_expr.strip().split()

    if len(fields) != 5:
        raise ValueError("cron_expr must have exactly 5 fields: minute hour day month weekday")

    f_min, f_hour, f_dom, f_mon, f_dow = fields
    dt_cur = (from_dt or datetime.now()).replace(second=0, microsecond=0) + timedelta(minutes=1)

    # Search up to ~2 years of minutes (safety cap)
    for _ in range(366 * 24 * 60):

        if (
            _cron_field_matches(dt_cur.month, f_mon, 1, 12)
            and _cron_field_matches(dt_cur.day, f_dom, 1, 31)
            and _cron_field_matches(dt_cur.weekday(), f_dow.replace("7", "0"), 0, 6)
            and _cron_field_matches(dt_cur.hour, f_hour, 0, 23)
            and _cron_field_matches(dt_cur.minute, f_min, 0, 59)
        ):
            return dt_cur

        dt_cur += timedelta(minutes=1)

    raise ValueError("No matching datetime found within search window")


def cron_previous_run(
    cron_expr: str,
    from_dt: Union[datetime, None] = None,
) -> datetime:
    """Returns the most recent past datetime matching a 5-field cron expression.

    Args:
        cron_expr: Five space-separated cron fields.
        from_dt: Reference datetime (defaults to now).

    Returns:
        The most recent past matching datetime.

    Raises:
        TypeError: If cron_expr is not a string.
        ValueError: If cron_expr does not have exactly 5 fields.

    Example:
        >>> from datetime import datetime
        >>> cron_previous_run("0 9 * * *", datetime(2026, 4, 8, 10, 0))
        datetime.datetime(2026, 4, 8, 9, 0)

    Complexity: O(k) where k is minutes since last match
    """
    if not isinstance(cron_expr, str):
        raise TypeError("cron_expr must be a string")

    fields = cron_expr.strip().split()

    if len(fields) != 5:
        raise ValueError("cron_expr must have exactly 5 fields: minute hour day month weekday")

    f_min, f_hour, f_dom, f_mon, f_dow = fields
    dt_cur = (from_dt or datetime.now()).replace(second=0, microsecond=0) - timedelta(minutes=1)

    for _ in range(366 * 24 * 60):

        if (
            _cron_field_matches(dt_cur.month, f_mon, 1, 12)
            and _cron_field_matches(dt_cur.day, f_dom, 1, 31)
            and _cron_field_matches(dt_cur.weekday(), f_dow.replace("7", "0"), 0, 6)
            and _cron_field_matches(dt_cur.hour, f_hour, 0, 23)
            and _cron_field_matches(dt_cur.minute, f_min, 0, 59)
        ):
            return dt_cur

        dt_cur -= timedelta(minutes=1)

    raise ValueError("No matching datetime found within search window")


# ---------------------------------------------------------------------------
# Astronomy approximations
# ---------------------------------------------------------------------------

def sunrise_sunset(
    latitude: float,
    longitude: float,
    d: Union[date, datetime],
) -> Tuple:
    """Approximate sunrise and sunset times for a location (UTC).

    Uses the NOAA simplified solar equations. Accuracy is typically
    within a few minutes.

    Args:
        latitude: Latitude in decimal degrees (positive North).
        longitude: Longitude in decimal degrees (positive East).
        d: The date for calculation.

    Returns:
        Tuple of (sunrise, sunset) as datetime objects in UTC.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If latitude or longitude is out of range.

    Example:
        >>> from datetime import date
        >>> sr, ss = sunrise_sunset(40.4168, -3.7038, date(2026, 6, 21))
        >>> sr.hour  # ~5 UTC for Madrid summer
        5

    Complexity: O(1)
    """
    if not isinstance(latitude, (int, float)):
        raise TypeError("latitude must be numeric")

    if not isinstance(longitude, (int, float)):
        raise TypeError("longitude must be numeric")

    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    if not -90 <= latitude <= 90:
        raise ValueError("latitude must be between -90 and 90")

    if not -180 <= longitude <= 180:
        raise ValueError("longitude must be between -180 and 180")

    dt_date = d.date() if isinstance(d, datetime) else d
    n = (dt_date - date(2000, 1, 1)).days + 0.5

    # Solar mean anomaly
    m_deg = (357.5291 + 0.98560028 * n) % 360
    m_rad = math.radians(m_deg)

    # Equation of center
    c = 1.9148 * math.sin(m_rad) + 0.02 * math.sin(2 * m_rad) + 0.0003 * math.sin(3 * m_rad)

    # Ecliptic longitude
    lam_deg = (m_deg + c + 180 + 102.9372) % 360
    lam_rad = math.radians(lam_deg)

    # Declination
    decl = math.asin(math.sin(lam_rad) * math.sin(math.radians(23.4393)))

    # Hour angle
    lat_rad = math.radians(latitude)
    cos_ha = (
        math.sin(math.radians(-0.83)) - math.sin(lat_rad) * math.sin(decl)
    ) / (math.cos(lat_rad) * math.cos(decl))

    # Clamp for polar regions
    if cos_ha < -1 or cos_ha > 1:
        raise ValueError("Sun does not rise or set on this date at this latitude")

    ha_deg = math.degrees(math.acos(cos_ha))

    # Solar transit (noon)
    j_transit = 2451545.0 + n + ((-longitude / 360) - round(-longitude / 360))
    j_transit += 0.0053 * math.sin(m_rad) - 0.0069 * math.sin(2 * lam_rad)

    j_rise = j_transit - ha_deg / 360
    j_set = j_transit + ha_deg / 360

    def _jd_to_datetime(jd: float) -> datetime:
        """Convert Julian date to datetime (UTC)."""
        epoch = datetime(2000, 1, 1, 12, 0, 0)
        delta = timedelta(days=jd - 2451545.0)
        return epoch + delta

    return _jd_to_datetime(j_rise), _jd_to_datetime(j_set)


def daylight_hours(latitude: float, d: Union[date, datetime]) -> float:
    """Estimates hours of daylight for a given latitude and date.

    Args:
        latitude: Latitude in decimal degrees (positive North).
        d: The date for calculation.

    Returns:
        Approximate hours of daylight.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If latitude is out of range.

    Example:
        >>> round(daylight_hours(40.4168, date(2026, 6, 21)), 1)  # Madrid summer
        15.1

    Complexity: O(1)
    """
    if not isinstance(latitude, (int, float)):
        raise TypeError("latitude must be numeric")

    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    if not -90 <= latitude <= 90:
        raise ValueError("latitude must be between -90 and 90")

    dt_date = d.date() if isinstance(d, datetime) else d
    day_of_year = (dt_date - date(dt_date.year, 1, 1)).days + 1

    # Solar declination approximation
    decl = math.radians(23.44) * math.sin(math.radians((360 / 365) * (day_of_year + 284)))
    lat_rad = math.radians(latitude)

    cos_ha = -math.tan(lat_rad) * math.tan(decl)

    if cos_ha <= -1:
        return 24.0  # Midnight sun

    if cos_ha >= 1:
        return 0.0  # Polar night

    ha = math.acos(cos_ha)
    return (2 * ha / math.pi) * 12.0


def shift_schedule(
    start_date: Union[date, datetime],
    shift_days: int,
    rest_days: int,
    target_date: Union[date, datetime],
) -> str:
    """Determines if a target date is a work or rest day in a cyclic rotation.

    Models a rotating shift pattern like "4 days on, 2 days off" starting
    from *start_date*.

    Args:
        start_date: First day of the first shift cycle.
        shift_days: Number of consecutive working days per cycle.
        rest_days: Number of consecutive rest days per cycle.
        target_date: The date to evaluate.

    Returns:
        ``"work"`` or ``"rest"``.

    Raises:
        TypeError: If dates or integers have wrong types.
        ValueError: If shift_days or rest_days are not positive.

    Example:
        >>> from datetime import date
        >>> shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 5))
        'work'
        >>> shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 6))
        'rest'

    Complexity: O(1)
    """
    if not isinstance(start_date, (date, datetime)):
        raise TypeError("start_date must be a date or datetime")

    if not isinstance(target_date, (date, datetime)):
        raise TypeError("target_date must be a date or datetime")

    if not isinstance(shift_days, int) or not isinstance(rest_days, int):
        raise TypeError("shift_days and rest_days must be integers")

    if shift_days <= 0 or rest_days <= 0:
        raise ValueError("shift_days and rest_days must be positive")

    s = start_date.date() if isinstance(start_date, datetime) else start_date
    t = target_date.date() if isinstance(target_date, datetime) else target_date
    delta = (t - s).days

    if delta < 0:
        raise ValueError("target_date must be on or after start_date")

    cycle = shift_days + rest_days
    position = delta % cycle

    return "work" if position < shift_days else "rest"


def time_zone_abbreviation(tz_name: str, ref: datetime | None = None) -> str:
    """Return the common abbreviation for a timezone at a given moment.

    Uses only the standard library ``zoneinfo`` (Python 3.9+).

    Args:
        tz_name: IANA timezone name (e.g. ``"Europe/Madrid"``).
        ref: Reference datetime. Defaults to now (UTC).

    Returns:
        Timezone abbreviation string (e.g. ``"CET"``, ``"CEST"``).

    Raises:
        TypeError: If *tz_name* is not a string.
        ValueError: If *tz_name* is not a recognized timezone.

    Example:
        >>> time_zone_abbreviation("US/Eastern", datetime(2026, 1, 15))
        'EST'

    Complexity: O(1)
    """
    if not isinstance(tz_name, str):
        raise TypeError("tz_name must be a string")

    try:
        from zoneinfo import ZoneInfo
    except ImportError:
        raise ImportError("zoneinfo requires Python 3.9+")

    try:
        tz = ZoneInfo(tz_name)
    except KeyError:
        raise ValueError(f"Unknown timezone: {tz_name!r}")

    if ref is None:
        ref = datetime.now(tz)
    elif ref.tzinfo is None:
        ref = ref.replace(tzinfo=ZoneInfo("UTC"))

    return ref.astimezone(tz).strftime("%Z")


def next_occurrence(
    weekday: int,
    hour: int = 0,
    minute: int = 0,
    ref: date | datetime | None = None,
) -> datetime:
    """Find the next occurrence of a given weekday and time.

    Args:
        weekday: ISO weekday (1=Monday … 7=Sunday).
        hour: Hour component (0-23). Default 0.
        minute: Minute component (0-59). Default 0.
        ref: Reference date/datetime. Defaults to today.

    Returns:
        A ``datetime`` representing the next occurrence (always in the future
        relative to *ref*).

    Raises:
        TypeError: If *weekday* is not an integer.
        ValueError: If *weekday* not in 1-7 or hour/minute out of range.

    Example:
        >>> from datetime import date
        >>> # Next Monday after 2026-04-08 (Wednesday)
        >>> next_occurrence(1, ref=date(2026, 4, 8))
        datetime.datetime(2026, 4, 13, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(weekday, int):
        raise TypeError("weekday must be an integer")

    if weekday < 1 or weekday > 7:
        raise ValueError("weekday must be 1 (Mon) to 7 (Sun)")

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        raise ValueError("hour must be 0-23, minute must be 0-59")

    if ref is None:
        ref_dt = datetime.now()
    elif isinstance(ref, datetime):
        ref_dt = ref
    elif isinstance(ref, date):
        ref_dt = datetime(ref.year, ref.month, ref.day)
    else:
        raise TypeError("ref must be a date or datetime")

    target_iso = weekday  # 1=Mon..7=Sun
    current_iso = ref_dt.isoweekday()
    days_ahead = (target_iso - current_iso) % 7

    if days_ahead == 0:
        candidate = ref_dt.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if candidate <= ref_dt:
            days_ahead = 7

    target_date = ref_dt + timedelta(days=days_ahead)
    return target_date.replace(hour=hour, minute=minute, second=0, microsecond=0)


def business_days_until(
    start: date | datetime,
    end: date | datetime,
    holidays: list | None = None,
) -> int:
    """Count working days between two dates, excluding weekends and holidays.

    Args:
        start: Start date (inclusive).
        end: End date (exclusive).
        holidays: Optional list of ``date`` objects to exclude.

    Returns:
        Number of business days.

    Raises:
        TypeError: If *start* or *end* are not date/datetime.

    Example:
        >>> from datetime import date
        >>> business_days_until(date(2026, 4, 6), date(2026, 4, 13))
        5

    Complexity: O(d), d = days between start and end.
    """
    if not isinstance(start, (date, datetime)):
        raise TypeError("start must be a date or datetime")

    if not isinstance(end, (date, datetime)):
        raise TypeError("end must be a date or datetime")

    s = start.date() if isinstance(start, datetime) else start
    e = end.date() if isinstance(end, datetime) else end

    holiday_set: set[date] = set(holidays) if holidays else set()
    count = 0
    current = s

    while current < e:

        if current.weekday() < 5 and current not in holiday_set:
            count += 1

        current += timedelta(days=1)

    return count


def trading_days_between(
    start: date | datetime,
    end: date | datetime,
    holidays: list[date] | None = None,
    weekend: tuple[int, ...] = (5, 6),
) -> int:
    """Count trading days between two dates.

    Similar to :func:`business_days_between` but allows a configurable
    weekend tuple, making it suitable for markets that trade on
    Saturdays or close on Sundays/Fridays.

    Args:
        start: Start date (inclusive).
        end: End date (exclusive).
        holidays: Optional market holidays to exclude.
        weekend: Weekday numbers considered non-trading (Mon=0).

    Returns:
        Number of trading days.

    Raises:
        TypeError: If *start* or *end* are not date/datetime.

    Example:
        >>> from datetime import date
        >>> trading_days_between(date(2026, 4, 6), date(2026, 4, 13))
        5

    Complexity: O(d), d = days between start and end.
    """
    if not isinstance(start, (date, datetime)):
        raise TypeError("start must be a date or datetime")

    if not isinstance(end, (date, datetime)):
        raise TypeError("end must be a date or datetime")

    s = start.date() if isinstance(start, datetime) else start
    e = end.date() if isinstance(end, datetime) else end

    holiday_set: set[date] = set(holidays) if holidays else set()
    weekend_set = set(weekend)
    count = 0
    current = s

    while current < e:

        if current.weekday() not in weekend_set and current not in holiday_set:
            count += 1

        current += timedelta(days=1)

    return count


def iso_week_start(year: int, week: int) -> date:
    """Return the Monday that starts a given ISO week.

    Args:
        year: ISO year.
        week: ISO week number (1-53).

    Returns:
        ``date`` object for the Monday of that ISO week.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If *week* is outside [1, 53].

    Example:
        >>> iso_week_start(2026, 1)
        datetime.date(2025, 12, 29)

    Complexity: O(1)
    """
    if not isinstance(year, int) or not isinstance(week, int):
        raise TypeError("year and week must be integers")

    if week < 1 or week > 53:
        raise ValueError("week must be between 1 and 53")

    # Jan 4 is always in ISO week 1
    jan4 = date(year, 1, 4)
    # Monday of week 1
    week1_monday = jan4 - timedelta(days=jan4.weekday())

    return week1_monday + timedelta(weeks=week - 1)


def time_overlap(
    start1: datetime,
    end1: datetime,
    start2: datetime,
    end2: datetime,
) -> float:
    """Return overlapping seconds between two time intervals.

    If the intervals do not overlap, returns ``0.0``.

    Args:
        start1: Start of first interval.
        end1: End of first interval.
        start2: Start of second interval.
        end2: End of second interval.

    Returns:
        Overlap duration in seconds.

    Raises:
        TypeError: If arguments are not datetime instances.

    Example:
        >>> from datetime import datetime
        >>> a, b = datetime(2026, 1, 1, 8, 0), datetime(2026, 1, 1, 12, 0)
        >>> c, d = datetime(2026, 1, 1, 10, 0), datetime(2026, 1, 1, 14, 0)
        >>> time_overlap(a, b, c, d)
        7200.0

    Complexity: O(1)
    """
    for name, val in (("start1", start1), ("end1", end1),
                      ("start2", start2), ("end2", end2)):

        if not isinstance(val, datetime):
            raise TypeError(f"{name} must be a datetime")

    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)

    delta = (overlap_end - overlap_start).total_seconds()

    return max(0.0, delta)


def next_full_moon(d: date | datetime) -> date:
    """Approximate date of the next full moon after *d*.

    Uses the mean synodic month (29.53058867 days) anchored to a
    known full moon (2000-01-06 18:14 UTC).

    Args:
        d: Reference date.

    Returns:
        ``date`` of the next full moon.

    Raises:
        TypeError: If *d* is not a date or datetime.

    Example:
        >>> next_full_moon(date(2026, 1, 1))
        datetime.date(2026, 1, 3)

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    known_full = datetime(2000, 1, 6, 18, 14)
    synodic = 29.53058867

    target = datetime(d.year, d.month, d.day) if not isinstance(d, datetime) else d

    diff_days = (target - known_full).total_seconds() / 86400.0
    cycles = diff_days / synodic
    next_cycle = math.ceil(cycles)

    next_full_dt = known_full + timedelta(days=next_cycle * synodic)

    return next_full_dt.date()


def working_hours_in_month(
    year: int,
    month: int,
    hours_per_day: float = 8.0,
    holidays: list[date] | None = None,
) -> float:
    """Calculate total working hours in a given month.

    Counts weekdays (Mon-Fri) excluding holidays, then multiplies
    by *hours_per_day*.

    Args:
        year: Calendar year.
        month: Calendar month (1-12).
        hours_per_day: Working hours per business day.
        holidays: Optional list of holidays to exclude.

    Returns:
        Total working hours as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If *month* is outside [1, 12].

    Example:
        >>> working_hours_in_month(2026, 1)
        176.0

    Complexity: O(d), d = days in month.
    """
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("year and month must be integers")

    if month < 1 or month > 12:
        raise ValueError("month must be between 1 and 12")

    if not isinstance(hours_per_day, (int, float)):
        raise TypeError("hours_per_day must be numeric")

    holiday_set: set[date] = set(holidays) if holidays else set()
    days_in_month = calendar.monthrange(year, month)[1]
    count = 0

    for day in range(1, days_in_month + 1):
        d = date(year, month, day)

        if d.weekday() < 5 and d not in holiday_set:
            count += 1

    return float(count * hours_per_day)


def business_quarter_label(d: date) -> str:
    """Returns a business quarter label for a date.

    Args:
        d: A ``date`` or ``datetime`` instance.

    Returns:
        String in the form ``'Q1 2024'``.

    Raises:
        TypeError: If d is not a date/datetime.

    Example:
        >>> from datetime import date
        >>> business_quarter_label(date(2024, 3, 15))
        'Q1 2024'

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()

    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime")

    q = (d.month - 1) // 3 + 1

    return f"Q{q} {d.year}"


def academic_year(d: date, start_month: int = 9) -> str:
    """Returns the academic year label for a date.

    An academic year that starts in September 2023 runs until
    August 2024 and is labelled ``'2023/2024'``.

    Args:
        d: A ``date`` or ``datetime`` instance.
        start_month: Month the academic year begins (default 9).

    Returns:
        String in the form ``'2023/2024'``.

    Raises:
        TypeError: If d is not a date/datetime.

    Example:
        >>> from datetime import date
        >>> academic_year(date(2024, 2, 1))
        '2023/2024'

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()

    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime")

    if d.month >= start_month:
        return f"{d.year}/{d.year + 1}"

    return f"{d.year - 1}/{d.year}"


def date_to_week_label(d: date) -> str:
    """Returns an ISO week label for a date.

    Args:
        d: A ``date`` or ``datetime`` instance.

    Returns:
        String in the form ``'W02-2024'``.

    Raises:
        TypeError: If d is not a date/datetime.

    Example:
        >>> from datetime import date
        >>> date_to_week_label(date(2024, 1, 8))
        'W02-2024'

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()

    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime")

    iso_year, iso_week, _ = d.isocalendar()

    return f"W{iso_week:02d}-{iso_year}"


# ---------------------------------------------------------------------------
# Phase 21 – Batch 35: Date Operations
# ---------------------------------------------------------------------------

def format_date_iso(d) -> str:
    """Format a date or datetime as ISO 8601 string (YYYY-MM-DD).

    Args:
        d: A ``date`` or ``datetime`` object.

    Returns:
        ISO 8601 date string.

    Raises:
        TypeError: If *d* is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> format_date_iso(date(2024, 3, 15))
        '2024-03-15'

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime.")
    return d.isoformat()


def format_datetime_iso(dt) -> str:
    """Format a datetime as ISO 8601 string (YYYY-MM-DDTHH:MM:SS).

    Args:
        dt: A ``datetime`` object.

    Returns:
        ISO 8601 datetime string.

    Raises:
        TypeError: If *dt* is not a datetime.

    Example:
        >>> from datetime import datetime
        >>> format_datetime_iso(datetime(2024, 3, 15, 10, 30, 0))
        '2024-03-15T10:30:00'

    Complexity: O(1)
    """
    if not isinstance(dt, datetime):
        raise TypeError("dt must be a datetime.")
    return dt.isoformat()


def clamp_date(d, min_date, max_date):
    """Clamp a date to the range [min_date, max_date].

    Args:
        d: Date to clamp.
        min_date: Lower bound.
        max_date: Upper bound.

    Returns:
        Clamped date.

    Raises:
        TypeError: If arguments are not date/datetime.

    Example:
        >>> from datetime import date
        >>> clamp_date(date(2024, 6, 15), date(2024, 1, 1), date(2024, 3, 31))
        datetime.date(2024, 3, 31)

    Complexity: O(1)
    """
    for name, val in [("d", d), ("min_date", min_date), ("max_date", max_date)]:
        if not isinstance(val, (date, datetime)):
            raise TypeError(f"{name} must be a date or datetime.")
    if d < min_date:
        return min_date
    if d > max_date:
        return max_date
    return d


def midpoint_date(d1, d2):
    """Return the midpoint date between two dates.

    Args:
        d1: First date.
        d2: Second date.

    Returns:
        Midpoint as a ``date``.

    Raises:
        TypeError: If arguments are not date/datetime.

    Example:
        >>> from datetime import date
        >>> midpoint_date(date(2024, 1, 1), date(2024, 1, 11))
        datetime.date(2024, 1, 6)

    Complexity: O(1)
    """
    if isinstance(d1, datetime):
        d1 = d1.date()
    if isinstance(d2, datetime):
        d2 = d2.date()
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise TypeError("Both arguments must be date or datetime.")
    delta = (d2 - d1).days
    return d1 + timedelta(days=delta // 2)


def date_to_ordinal(d) -> int:
    """Return the proleptic Gregorian ordinal of a date.

    Args:
        d: A ``date`` or ``datetime`` object.

    Returns:
        Ordinal integer (1 = January 1 of year 1).

    Raises:
        TypeError: If *d* is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> date_to_ordinal(date(2024, 1, 1))
        738886

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime.")
    return d.toordinal()