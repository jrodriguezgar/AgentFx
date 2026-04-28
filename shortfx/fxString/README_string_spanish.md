# string_spanish - Funciones para Procesamiento de Texto en Español

Módulo especializado para el procesamiento de cadenas de texto en español, incluyendo validación de documentos de identidad españoles (DNI/NIE/CIF), reducción fonética, y normalización de texto según las reglas del idioma español.

## 📋 Tabla de Contenidos

- [Características Principales](#características-principales)
- [Instalación](#instalación)
- [Funciones Disponibles](#funciones-disponibles)
  - [Procesamiento de Texto](#procesamiento-de-texto)
  - [Validación de Documentos de Identidad](#validación-de-documentos-de-identidad)
  - [Utilidades de Formato](#utilidades-de-formato)
- [Casos de Uso](#casos-de-uso)
- [Referencia de la API](#referencia-de-la-api)
- [Algoritmos de Validación](#algoritmos-de-validación)

---

## Características Principales

### 🔤 Procesamiento de Texto
- **Eliminación de palabras vacías** (stop words) en español
- **Reducción fonética** con múltiples niveles de intensidad
- **Normalización de caracteres** españoles
- **Limpieza de caracteres especiales** con preservación de acentos

### 🆔 Validación de Documentos
- **DNI** (Documento Nacional de Identidad)
- **NIE** (Número de Identidad de Extranjero)
- **CIF** (Certificado de Identificación Fiscal)
- Validación de dígitos de control
- Parsing y normalización de formatos

### 🛠️ Utilidades
- Formateo automático de NIFs
- Conversión de mayúsculas/minúsculas preservando formato original
- Eliminación de acentos con restauración de casing

---

## Instalación

```python
from shortfx.fxString.string_spanish import (
    remove_spanish_stop_words,
    reduce_spanish_letters,
    is_valid_dni,
    is_valid_nie,
    is_valid_cif,
    validate_spanish_nif,
    nif_parse,
    nif_padding,
    nif_letter,
    fix_spanish
)
```

---

## Funciones Disponibles

### Procesamiento de Texto

#### `remove_spanish_stop_words(input_string: str) -> str | None`

Elimina artículos, conjunciones y preposiciones comunes del español.

**Palabras eliminadas:**
- Artículos: `el, la, los, las, un, una, unos, unas`
- Conjunciones: `y, e, o, u`
- Preposiciones: `a, de, en, por, al, del`

**Ejemplo:**
```python
>>> remove_spanish_stop_words("El coche de la casa es grande y azul")
'coche casa es grande azul'

>>> remove_spanish_stop_words("Un perro y un gato")
'perro gato'
```

**Complejidad:** O(n) donde n es la longitud del texto

---

#### `reduce_spanish_letters(input_string: str, strength: int) -> str | None`

Reduce variaciones fonéticas y ortográficas del español para normalización y comparación.

**Niveles de Intensidad:**

**Nivel 0** - Solo normalización básica
```python
>>> reduce_spanish_letters("Coche", 0)
'COCHE'  # Elimina acentos y convierte a mayúsculas
```

**Nivel 1** - Reducciones fonéticas básicas
- Elimina H silenciosa
- RR → R
- QU → C
- GÜ → G, GU → G
- LL → Y
- Y → I
- Z → C
- K → C
- B → V

```python
>>> reduce_spanish_letters("Guerrero", 1)
'GERERO'

>>> reduce_spanish_letters("Bogotá", 1)
'VOGOTA'
```

**Nivel 2** - Reducciones fonéticas avanzadas
- Todas las de nivel 1, más:
- X → S
- C → S (seseo)

```python
>>> reduce_spanish_letters("Excelente", 2)
'ESSELENTE'

>>> reduce_spanish_letters("México", 2)
'MESISO'
```

**Nivel 3** - Reducciones más agresivas
- Todas las de nivel 1 y 2, más:
- Ç → S
- Ñ → N
- W → V
- G → J

```python
>>> reduce_spanish_letters("Ñandú", 3)
'NANDU'

>>> reduce_spanish_letters("Gigante", 3)
'JIJANTE'
```

**Casos de Uso:**
- Búsqueda tolerante a variaciones ortográficas
- Matching de nombres con diferentes grafías
- Normalización para comparaciones fonéticas
- Deduplicación de registros

**Complejidad:** O(n) donde n es la longitud del texto

---

#### `fix_spanish(input_string: str | None, additional_allowed_chars: str = '') -> str | None`

Limpia texto reemplazando caracteres especiales y filtrando caracteres no permitidos.

**Reemplazos automáticos:**
- Comillas diversas (`'`, `'`, `` ` ``, `´`) → `'`
- `§` → `º`
- `¥` → `Ñ`

**Caracteres permitidos por defecto:**
- Alfabeto español completo (a-z, A-Z)
- Caracteres especiales españoles: `ñ, Ñ, á, é, í, ó, ú, ü, Á, É, Í, Ó, Ú, Ü, ç, Ç`
- Espacios

**Ejemplo:**
```python
>>> fix_spanish("Hello, 'world'§ with ¥ and other €!")
"Hello, 'world'º with Ñ and other "

>>> fix_spanish("Precio: 100€", additional_allowed_chars="€0123456789:")
"Precio: 100€"
```

**Complejidad:** O(n) donde n es la longitud del texto

---

### Validación de Documentos de Identidad

#### `is_valid_dni(dni_value: str) -> bool`

Valida un DNI español (8 dígitos + letra de control).

**Formato válido:** `12345678Z`

**Validaciones:**
1. Formato: 8 dígitos seguidos de 1 letra
2. Letra de control correcta según algoritmo oficial

**Ejemplo:**
```python
>>> is_valid_dni("12345678Z")
True

>>> is_valid_dni("12345678A")  # Letra incorrecta
False

>>> is_valid_dni("1234567Z")   # Faltan dígitos
False
```

**Complejidad:** O(1)

---

#### `is_valid_nie(nie_value: str) -> bool`

Valida un NIE español (Número de Identidad de Extranjero).

**Formato válido:** `X1234567L` (X/Y/Z + 7 dígitos + letra)

**Prefijos válidos:**
- `X` = 0
- `Y` = 1
- `Z` = 2

**Validaciones:**
1. Formato: Letra inicial (X/Y/Z) + 7 dígitos + letra de control
2. Letra de control correcta

**Ejemplo:**
```python
>>> is_valid_nie("X1234567L")
True

>>> is_valid_nie("A1234567L")  # Letra inicial inválida
False
```

**Complejidad:** O(1)

---

#### `is_valid_cif(cif_value: str) -> bool`

Valida un CIF español (Certificado de Identificación Fiscal).

**Formato válido:** `A12345674` (Letra + 7 dígitos + dígito/letra de control)

**Letras iniciales válidas:**
- `A-H, J, N, P, Q, R, S, U, V, W`

**Validaciones:**
1. Formato: Letra inicial válida + 7 dígitos + dígito/letra de control
2. Dígito de control correcto según algoritmo oficial

**Ejemplo:**
```python
>>> is_valid_cif("A12345674")
True

>>> is_valid_cif("I12345674")  # Letra inicial inválida
False
```

**Complejidad:** O(1)

---

#### `validate_spanish_nif(nif_type: str, nif_value: str) -> bool`

Validador genérico que selecciona el método correcto según el tipo de documento.

**Tipos válidos:** `'DNI'`, `'NIE'`, `'CIF'`

**Ejemplo:**
```python
>>> validate_spanish_nif('DNI', '12345678Z')
True

>>> validate_spanish_nif('NIE', 'X1234567L')
True

>>> validate_spanish_nif('CIF', 'A12345674')
True

>>> validate_spanish_nif('PASSPORT', '123456')  # Tipo inválido
ValueError: Invalid NIF type. Expected {'DNI', 'NIE', 'CIF'}.
```

**Complejidad:** O(1)

---

### Utilidades de Formato

#### `nif_parse(nif: Optional[str]) -> Optional[str]`

Parsea y normaliza un NIF/NIE/CIF eliminando guiones, espacios y caracteres especiales.

**Transformaciones:**
- Elimina guiones, puntos, espacios
- Convierte a mayúsculas
- Valida formato básico

**Ejemplo:**
```python
>>> nif_parse("12345678-Z")
'12345678Z'

>>> nif_parse("12.345.678-Z")
'12345678Z'

>>> nif_parse("x-1234567-l")
'X1234567L'

>>> nif_parse("invalid")
None
```

**Complejidad:** O(n) donde n es la longitud del NIF

---

#### `nif_padding(p_nif: Optional[str]) -> Optional[str]`

Rellena un NIF con ceros a la izquierda hasta alcanzar el formato estándar de 11 caracteres.

**Ejemplo:**
```python
>>> nif_padding("12345678Z")
'0012345678Z'

>>> nif_padding("1234567")
'000001234567'

>>> nif_padding(None)
None
```

**Complejidad:** O(1)

---

#### `nif_letter(p_dni: str) -> str`

Calcula la letra de control para un DNI dado.

**Algoritmo:**
- Divide el número del DNI entre 23
- Usa el resto para indexar en la tabla de letras de control

**Tabla de letras:** `TRWAGMYFPDXBNJZSQVHLCKE`

**Ejemplo:**
```python
>>> nif_letter("12345678")
'Z'

>>> nif_letter("00000000")
'T'
```

**Complejidad:** O(1)

---

## Casos de Uso

### 1. Validación de Formularios Web

```python
def validar_formulario_registro(dni: str, nombre: str) -> dict:
    """Valida datos de registro de usuario."""
    
    errores = []
    
    # Parsear y validar DNI
    dni_limpio = nif_parse(dni)
    if not dni_limpio:
        errores.append("Formato de DNI inválido")
    elif not is_valid_dni(dni_limpio):
        errores.append("DNI inválido - letra de control incorrecta")
    
    # Limpiar nombre
    nombre_limpio = fix_spanish(nombre)
    if not nombre_limpio or len(nombre_limpio) < 2:
        errores.append("Nombre inválido")
    
    return {
        'valido': len(errores) == 0,
        'errores': errores,
        'dni_normalizado': dni_limpio,
        'nombre_normalizado': nombre_limpio
    }

# Ejemplo de uso
resultado = validar_formulario_registro("12.345.678-Z", "José María")
print(resultado)
# {'valido': True, 'errores': [], 'dni_normalizado': '12345678Z', 'nombre_normalizado': 'José María'}
```

---

### 2. Búsqueda Fonética de Nombres

```python
def buscar_nombre_fonetico(busqueda: str, base_datos: list, threshold: int = 1) -> list:
    """
    Busca nombres usando reducción fonética para encontrar variaciones.
    
    Args:
        busqueda: Nombre a buscar
        base_datos: Lista de nombres en la base de datos
        threshold: Nivel de reducción fonética (0-3)
    
    Returns:
        Lista de nombres que coinciden fonéticamente
    """
    # Normalizar búsqueda
    busqueda_normalizada = reduce_spanish_letters(busqueda, threshold)
    
    resultados = []
    for nombre in base_datos:
        nombre_normalizado = reduce_spanish_letters(nombre, threshold)
        
        if busqueda_normalizada == nombre_normalizado:
            resultados.append({
                'nombre': nombre,
                'normalizado': nombre_normalizado,
                'coincidencia': 'exacta'
            })
    
    return resultados

# Ejemplo de uso
nombres_db = ["María", "Maria", "Mario", "Mariano", "Guerrero", "Gerero"]

# Nivel 1: Detecta María/Maria
print(buscar_nombre_fonetico("María", nombres_db, 1))
# [{'nombre': 'María', 'normalizado': 'MARIA', 'coincidencia': 'exacta'},
#  {'nombre': 'Maria', 'normalizado': 'MARIA', 'coincidencia': 'exacta'}]

# Nivel 1: Detecta Guerrero/Gerero
print(buscar_nombre_fonetico("Guerrero", nombres_db, 1))
# [{'nombre': 'Guerrero', 'normalizado': 'GERERO', 'coincidencia': 'exacta'},
#  {'nombre': 'Gerero', 'normalizado': 'GERERO', 'coincidencia': 'exacta'}]
```

---

### 3. Limpieza de Datos de CRM

```python
from shortfx.fxString.string_spanish import (
    remove_spanish_stop_words,
    fix_spanish,
    nif_parse,
    is_valid_dni
)

def limpiar_registro_cliente(cliente: dict) -> dict:
    """
    Limpia y normaliza datos de cliente.
    
    Args:
        cliente: Diccionario con datos del cliente
    
    Returns:
        Diccionario con datos normalizados
    """
    cliente_limpio = {}
    
    # Limpiar y normalizar nombre de empresa
    if 'empresa' in cliente:
        # Eliminar palabras vacías
        empresa_sin_stopwords = remove_spanish_stop_words(cliente['empresa'])
        # Limpiar caracteres especiales
        cliente_limpio['empresa'] = fix_spanish(empresa_sin_stopwords)
    
    # Normalizar DNI/CIF
    if 'nif' in cliente:
        nif_normalizado = nif_parse(cliente['nif'])
        cliente_limpio['nif'] = nif_normalizado
        cliente_limpio['nif_valido'] = is_valid_dni(nif_normalizado) if nif_normalizado else False
    
    # Limpiar dirección
    if 'direccion' in cliente:
        cliente_limpio['direccion'] = fix_spanish(cliente['direccion'], additional_allowed_chars='0123456789,.-º')
    
    return cliente_limpio

# Ejemplo de uso
cliente_raw = {
    'empresa': 'La Empresa de Servicios y Tecnología, S.L.',
    'nif': '12.345.678-Z',
    'direccion': 'Calle de la Rosa, nº 42, 3º A'
}

cliente_limpio = limpiar_registro_cliente(cliente_raw)
print(cliente_limpio)
# {
#   'empresa': 'Empresa Servicios Tecnología, SL',
#   'nif': '12345678Z',
#   'nif_valido': True,
#   'direccion': 'Calle de la Rosa, nº 42, 3º A'
# }
```

---

### 4. Deduplicación de Registros

```python
def detectar_duplicados_dni(registros: list) -> dict:
    """
    Detecta registros duplicados basándose en DNI normalizado.
    
    Args:
        registros: Lista de diccionarios con datos de personas
    
    Returns:
        Diccionario con duplicados agrupados
    """
    from collections import defaultdict
    
    dni_grupos = defaultdict(list)
    
    for idx, registro in enumerate(registros):
        # Normalizar DNI
        dni_normalizado = nif_parse(registro.get('dni', ''))
        
        if dni_normalizado and is_valid_dni(dni_normalizado):
            # Agrupar por DNI normalizado
            dni_grupos[dni_normalizado].append({
                'indice': idx,
                'dni_original': registro.get('dni'),
                'nombre': registro.get('nombre')
            })
    
    # Filtrar solo grupos con duplicados
    duplicados = {
        dni: registros_grupo 
        for dni, registros_grupo in dni_grupos.items() 
        if len(registros_grupo) > 1
    }
    
    return duplicados

# Ejemplo de uso
registros = [
    {'dni': '12345678Z', 'nombre': 'Juan García'},
    {'dni': '12.345.678-Z', 'nombre': 'Juan Garcia'},  # Duplicado (mismo DNI)
    {'dni': '87654321X', 'nombre': 'María López'},
    {'dni': '12-345-678-Z', 'nombre': 'J. García'},    # Duplicado (mismo DNI)
]

duplicados = detectar_duplicados_dni(registros)
for dni, grupo in duplicados.items():
    print(f"\nDNI: {dni} - {len(grupo)} registros duplicados:")
    for reg in grupo:
        print(f"  - Índice {reg['indice']}: {reg['nombre']} (original: {reg['dni_original']})")

# Salida:
# DNI: 12345678Z - 3 registros duplicados:
#   - Índice 0: Juan García (original: 12345678Z)
#   - Índice 1: Juan Garcia (original: 12.345.678-Z)
#   - Índice 2: J. García (original: 12-345-678-Z)
```

---

### 5. Generador de Búsquedas Tolerantes

```python
def generar_variantes_busqueda(termino: str) -> list:
    """
    Genera variantes de un término para búsqueda tolerante.
    
    Args:
        termino: Término original de búsqueda
    
    Returns:
        Lista de variantes normalizadas
    """
    variantes = set()
    
    # Agregar original
    variantes.add(termino.upper())
    
    # Agregar variantes con diferentes niveles de reducción
    for nivel in range(4):
        variante = reduce_spanish_letters(termino, nivel)
        if variante:
            variantes.add(variante)
    
    # Agregar sin stop words
    sin_stopwords = remove_spanish_stop_words(termino)
    if sin_stopwords:
        variantes.add(sin_stopwords.upper())
        # También con reducción
        for nivel in [1, 2]:
            variante_reducida = reduce_spanish_letters(sin_stopwords, nivel)
            if variante_reducida:
                variantes.add(variante_reducida)
    
    return sorted(list(variantes))

# Ejemplo de uso
variantes = generar_variantes_busqueda("El coche rojo")
print("Variantes generadas:")
for v in variantes:
    print(f"  - {v}")

# Salida:
# Variantes generadas:
#   - COCHE ROJO
#   - COSE ROJO
#   - EL COCHE ROJO
#   - EL COSE ROJO
#   - EL COXE ROJO
#   - ...
```

---

## Referencia de la API

### Funciones de Texto

| Función | Descripción | Complejidad |
|---------|-------------|-------------|
| `remove_spanish_stop_words` | Elimina palabras vacías en español | O(n) |
| `reduce_spanish_letters` | Reducción fonética con niveles | O(n) |
| `fix_spanish` | Limpia y normaliza caracteres | O(n) |

### Funciones de Validación

| Función | Descripción | Formato | Complejidad |
|---------|-------------|---------|-------------|
| `is_valid_dni` | Valida DNI español | 8 dígitos + letra | O(1) |
| `is_valid_nie` | Valida NIE español | X/Y/Z + 7 dígitos + letra | O(1) |
| `is_valid_cif` | Valida CIF español | Letra + 7 dígitos + control | O(1) |
| `validate_spanish_nif` | Validador genérico | Según tipo | O(1) |

### Funciones Utilitarias

| Función | Descripción | Complejidad |
|---------|-------------|-------------|
| `nif_parse` | Normaliza formato de NIF | O(n) |
| `nif_padding` | Rellena NIF con ceros | O(1) |
| `nif_letter` | Calcula letra de control DNI | O(1) |

---

## Algoritmos de Validación

### DNI - Algoritmo de Letra de Control

```
1. Tomar los 8 dígitos del DNI
2. Calcular: resto = número % 23
3. Usar resto como índice en tabla: "TRWAGMYFPDXBNJZSQVHLCKE"
4. La letra en esa posición es la letra de control válida

Ejemplo: DNI 12345678
  12345678 % 23 = 14
  Tabla[14] = 'Z'
  DNI válido: 12345678Z
```

### NIE - Algoritmo de Letra de Control

```
1. Convertir letra inicial a número: X→0, Y→1, Z→2
2. Concatenar con los 7 dígitos siguientes
3. Aplicar el mismo algoritmo que DNI
4. Validar letra de control

Ejemplo: NIE X1234567
  X → 0
  01234567 % 23 = 14
  Tabla[14] = 'L'
  NIE válido: X1234567L
```

### CIF - Algoritmo de Dígito de Control

```
1. Sumar posiciones pares del número
2. Duplicar cada dígito en posiciones impares
3. Si duplicación > 9, sumar sus dígitos
4. Sumar todos los resultados
5. Obtener dígito de control: (10 - (suma % 10)) % 10

Nota: Algunos CIFs usan letra de control según la organización
```

---

## 🎯 Mejores Prácticas

### 1. Validación de DNI/NIE/CIF

```python
# ✅ CORRECTO: Normalizar antes de validar
dni_normalizado = nif_parse(dni_usuario)
if dni_normalizado and is_valid_dni(dni_normalizado):
    procesar_dni(dni_normalizado)

# ❌ INCORRECTO: Validar sin normalizar
if is_valid_dni(dni_usuario):  # Fallará si tiene guiones o espacios
    procesar_dni(dni_usuario)
```

### 2. Reducción Fonética

```python
# ✅ CORRECTO: Elegir nivel según el caso de uso
# Nivel 1: Para nombres propios con variaciones comunes
nombre_norm = reduce_spanish_letters(nombre, 1)

# Nivel 2-3: Para búsquedas muy tolerantes
# (Puede generar muchos falsos positivos)
termino_norm = reduce_spanish_letters(termino, 3)

# ❌ INCORRECTO: Siempre usar nivel máximo
# Genera demasiados falsos positivos
```

### 3. Limpieza de Texto

```python
# ✅ CORRECTO: Preservar caracteres necesarios
direccion = fix_spanish(texto, additional_allowed_chars='0123456789,.-º')

# ✅ CORRECTO: Combinar con otras funciones
texto_limpio = remove_spanish_stop_words(fix_spanish(texto))

# ❌ INCORRECTO: Aplicar fix_spanish sin caracteres adicionales si los necesitas
precio = fix_spanish("100€")  # Elimina el símbolo €
```

---

## ⚡ Optimización y Rendimiento

### Uso de Caché para Validaciones Repetidas

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def validar_dni_cached(dni: str) -> bool:
    """Valida DNI con caché para mejorar rendimiento."""
    dni_normalizado = nif_parse(dni)
    return bool(dni_normalizado and is_valid_dni(dni_normalizado))

# Uso en lotes grandes
dnis = ["12345678Z"] * 1000
# Primera llamada valida, las siguientes usan caché
resultados = [validar_dni_cached(dni) for dni in dnis]
```

### Procesamiento en Lote

```python
def validar_dnis_lote(dnis: list) -> dict:
    """Valida múltiples DNIs eficientemente."""
    resultados = {
        'validos': [],
        'invalidos': [],
        'errores': []
    }
    
    for dni in dnis:
        try:
            dni_norm = nif_parse(dni)
            if dni_norm and is_valid_dni(dni_norm):
                resultados['validos'].append(dni_norm)
            else:
                resultados['invalidos'].append(dni)
        except Exception as e:
            resultados['errores'].append({'dni': dni, 'error': str(e)})
    
    return resultados
```

---

## 📚 Referencias

- **Ministerio del Interior (España)**: Especificaciones oficiales de DNI/NIE
- **Agencia Tributaria**: Especificaciones oficiales de CIF
- **Real Academia Española (RAE)**: Reglas ortográficas y fonéticas del español
- **BOE**: Normativa oficial sobre documentos de identidad

---

## 🔧 Dependencias

Este módulo requiere solo la biblioteca estándar de Python:
- `re`: Expresiones regulares
- `unicodedata`: Normalización de caracteres Unicode
- `typing`: Type hints

---

## 📄 Licencia

Parte del proyecto **shortfx** - MIT License

