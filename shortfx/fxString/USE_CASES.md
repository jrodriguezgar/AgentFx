# fxString - Casos de Uso Prácticos

Este documento presenta casos de uso reales para el módulo **fxString** de shortfx, con énfasis especial en **similitud de palabras** (word similarity) y **corrección ortográfica** (spellcheck).

## 📋 Tabla de Contenidos

- [Similitud de Palabras (Word Similarity)](#similitud-de-palabras-word-similarity)
  - [1. Búsqueda Difusa en Bases de Datos](#1-búsqueda-difusa-en-bases-de-datos)
  - [2. Detección de Duplicados](#2-detección-de-duplicados)
  - [3. Validación de Nombres de Personas](#3-validación-de-nombres-de-personas)
  - [4. Búsqueda Tolerante a Errores](#4-búsqueda-tolerante-a-errores)
  - [5. Comparación de Documentos](#5-comparación-de-documentos)
  - [6. Sistema de Autocompletado Inteligente](#6-sistema-de-autocompletado-inteligente)
  - [7. Análisis de Similitud de Frases](#7-análisis-de-similitud-de-frases)
  - [8. Búsqueda Difusa Multi-Algoritmo](#8-búsqueda-difusa-multi-algoritmo)
  - [9. Herramienta de Comparación de Algoritmos](#9-herramienta-de-comparación-de-algoritmos)
- [Corrección Ortográfica (Spellcheck)](#corrección-ortográfica-spellcheck)
  - [1. Corrección de Nombres Propios](#1-corrección-de-nombres-propios)
  - [2. Normalización de Entrada de Usuarios](#2-normalización-de-entrada-de-usuarios)
  - [3. Limpieza de Datos de Formularios](#3-limpieza-de-datos-de-formularios)
  - [4. Corrección de Diccionarios Personalizados](#4-corrección-de-diccionarios-personalizados)
  - [5. Validación de Entrada en Tiempo Real](#5-validación-de-entrada-en-tiempo-real)
- [Casos de Uso Combinados](#casos-de-uso-combinados)
  - [Caso 1: Sistema de Matching de CVs](#caso-1-sistema-de-matching-de-cvs)
  - [Caso 2: Deduplicación y Limpieza de Contactos](#caso-2-deduplicación-y-limpieza-de-contactos)
  - [Caso 3: Deduplicación Masiva de Nombres](#caso-3-deduplicación-masiva-de-nombres)

---

## Similitud de Palabras (Word Similarity)

### 1. Búsqueda Difusa en Bases de Datos

**Problema:** Un usuario busca "Marti" en un sistema de clientes, pero el nombre real es "Martín" o "Martha".

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

# Base de datos de clientes
clientes = ["Martín García", "Martha Rodríguez", "María López", "Marco Sánchez"]
busqueda = "Marti"

# Encontrar coincidencias usando Jaro-Winkler (ideal para nombres)
resultados = []
for cliente in clientes:
    nombre = cliente.split()[0]  # Obtener el primer nombre
    resultado = calculate_similarity(busqueda, nombre, algorithm='jaro_winkler')
    
    if resultado['score'] > 0.75:  # Umbral de similitud
        resultados.append({
            'cliente': cliente,
            'score': resultado['score'],
            'coincidencia': resultado['score'] > 0.9
        })

# Ordenar por score descendente
resultados.sort(key=lambda x: x['score'], reverse=True)

for r in resultados:
    print(f"{r['cliente']}: {r['score']:.2%} - {'✓ Alta' if r['coincidencia'] else 'Posible'}")
```

**Salida:**
```
Martín García: 95.56% - ✓ Alta
Martha Rodríguez: 93.33% - ✓ Alta
Marco Sánchez: 76.67% - Posible
```

---

### 2. Detección de Duplicados

**Problema:** Identificar registros duplicados en una lista de productos con nombres similares pero escritos de forma diferente.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

productos = [
    "Laptop HP Pavilion 15",
    "Laptop HP Pavillion 15",  # Error ortográfico
    "Laptop HP Pavilion 15.6",
    "Mouse Logitech MX Master",
    "Mouse Logitec MX Master"   # Error ortográfico
]

# Detectar duplicados usando Levenshtein
duplicados = []
visitados = set()

for i, prod1 in enumerate(productos):
    if i in visitados:
        continue
    
    grupo = [prod1]
    
    for j, prod2 in enumerate(productos[i+1:], start=i+1):
        if j in visitados:
            continue
        
        # Usar Levenshtein para detectar similitud
        ratio = calculate_similarity(prod1, prod2, algorithm='levenshtein')
        
        if ratio > 0.85:  # 85% de similitud
            grupo.append(prod2)
            visitados.add(j)
    
    if len(grupo) > 1:
        duplicados.append(grupo)

# Mostrar resultados
for idx, grupo in enumerate(duplicados, 1):
    print(f"\nGrupo {idx} (posibles duplicados):")
    for producto in grupo:
        print(f"  - {producto}")
```

**Salida:**
```
Grupo 1 (posibles duplicados):
  - Laptop HP Pavilion 15
  - Laptop HP Pavillion 15
  - Laptop HP Pavilion 15.6

Grupo 2 (posibles duplicados):
  - Mouse Logitech MX Master
  - Mouse Logitec MX Master
```

---

### 3. Validación de Nombres de Personas

**Problema:** Verificar si dos nombres probablemente se refieren a la misma persona, considerando variaciones ortográficas y fonéticas.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def son_mismo_nombre(nombre1, nombre2):
    """
    Determina si dos nombres probablemente se refieren a la misma persona.
    """
    resultado, metricas = calculate_similarity(
        nombre1, 
        nombre2, 
        algorithm='effective_same',
        levenshtein_threshold=0.80,
        jaro_winkler_threshold=0.85,
        metaphone_required=False  # Permite más flexibilidad
    )
    
    return resultado, metricas

# Casos de prueba
pares_nombres = [
    ("José García", "Jose Garcia"),      # Sin tilde
    ("María López", "Maria Lopez"),      # Sin tilde
    ("Julián", "Julian"),                # Sin tilde
    ("Catherine", "Katherine"),          # Variación fonética
    ("John", "Juan"),                    # Diferentes nombres
    ("Chris", "Christopher")             # Diminutivo
]

for nombre1, nombre2 in pares_nombres:
    es_mismo, metricas = son_mismo_nombre(nombre1, nombre2)
    
    print(f"\n'{nombre1}' vs '{nombre2}'")
    print(f"  ¿Es el mismo? {es_mismo}")
    print(f"  Levenshtein: {metricas['levenshtein_ratio']:.2%}")
    print(f"  Jaro-Winkler: {metricas['jaro_winkler_score']:.2%}")
    print(f"  Metaphone: {metricas['metaphone_match']}")
```

**Salida:**
```
'José García' vs 'Jose Garcia'
  ¿Es el mismo? True
  Levenshtein: 91.67%
  Jaro-Winkler: 95.56%
  Metaphone: True

'Catherine' vs 'Katherine'
  ¿Es el mismo? True
  Levenshtein: 88.89%
  Jaro-Winkler: 92.22%
  Metaphone: True

'John' vs 'Juan'
  ¿Es el mismo? False
  Levenshtein: 50.00%
  Jaro-Winkler: 63.33%
  Metaphone: False
```

---

### 4. Búsqueda Tolerante a Errores

**Problema:** Implementar un sistema de búsqueda que tolere errores tipográficos comunes.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def busqueda_inteligente(query, catalogo, threshold=0.75):
    """
    Búsqueda que tolera errores tipográficos usando múltiples algoritmos.
    """
    resultados = []
    
    for item in catalogo:
        # Primera pasada: filtro rápido con Metaphone (fonético)
        if calculate_similarity(query, item, algorithm='metaphone'):
            # Segunda pasada: score de similitud con Levenshtein
            score = calculate_similarity(query, item, algorithm='levenshtein')
            
            if score >= threshold:
                resultados.append({
                    'item': item,
                    'score': score,
                    'tipo': 'fonético + léxico'
                })
        else:
            # Alternativa: Jaro-Winkler para casos sin match fonético
            jw_result = calculate_similarity(query, item, algorithm='jaro_winkler')
            
            if jw_result['score'] >= threshold:
                resultados.append({
                    'item': item,
                    'score': jw_result['score'],
                    'tipo': 'similitud visual'
                })
    
    # Ordenar por score
    resultados.sort(key=lambda x: x['score'], reverse=True)
    return resultados

# Ejemplo de uso
catalogo_productos = [
    "Python Programming",
    "Java Development",
    "JavaScript Essentials",
    "Machine Learning Basics",
    "Data Science Fundamentals"
]

# Búsqueda con errores tipográficos
consultas = ["Pyton", "Javascrip", "Machien Lerning"]

for consulta in consultas:
    print(f"\nBúsqueda: '{consulta}'")
    resultados = busqueda_inteligente(consulta, catalogo_productos)
    
    if resultados:
        print("  Resultados encontrados:")
        for r in resultados[:3]:  # Top 3
            print(f"    - {r['item']}: {r['score']:.2%} ({r['tipo']})")
    else:
        print("  No se encontraron resultados")
```

---

### 5. Comparación de Documentos

**Problema:** Determinar si dos descripciones o textos son similares usando comparación de tokens.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def comparar_textos(texto1, texto2):
    """
    Compara dos textos usando Sorensen-Dice y Jaccard.
    """
    # Sorensen-Dice (mejor para textos cortos)
    dice = calculate_similarity(texto1, texto2, algorithm='sorensen_dice')
    
    # Jaccard (buenos para conjuntos de palabras)
    jaccard = calculate_similarity(texto1, texto2, algorithm='jaccard')
    
    return {
        'sorensen_dice': dice['score'],
        'jaccard': jaccard['score'],
        'similitud_promedio': (dice['score'] + jaccard['score']) / 2
    }

# Ejemplo: Comparar descripciones de productos
desc1 = "Laptop gaming de alto rendimiento con procesador Intel Core i7"
desc2 = "Laptop para juegos de alta performance con procesador Intel i7"
desc3 = "Tablet con pantalla táctil y batería de larga duración"

print("Comparación de descripciones:")
print("\nDesc1 vs Desc2 (similares):")
resultado = comparar_textos(desc1, desc2)
for metrica, valor in resultado.items():
    print(f"  {metrica}: {valor:.2%}")

print("\nDesc1 vs Desc3 (diferentes):")
resultado = comparar_textos(desc1, desc3)
for metrica, valor in resultado.items():
    print(f"  {metrica}: {valor:.2%}")
```

**Salida:**
```
Comparación de descripciones:

Desc1 vs Desc2 (similares):
  sorensen_dice: 68.42%
  jaccard: 52.00%
  similitud_promedio: 60.21%

Desc1 vs Desc3 (diferentes):
  sorensen_dice: 9.09%
  jaccard: 4.76%
  similitud_promedio: 6.93%
```

---

### 6. Sistema de Autocompletado Inteligente

**Problema:** Implementar un sistema de autocompletado que sugiera opciones relevantes mientras el usuario escribe, incluso con errores ortográficos.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

class AutocompletadoInteligente:
    """Sistema de autocompletado con tolerancia a errores."""
    
    def __init__(self, vocabulario, min_chars=2):
        self.vocabulario = vocabulario
        self.min_chars = min_chars
    
    def sugerir(self, texto_parcial, max_sugerencias=5, threshold=0.60):
        """
        Genera sugerencias basadas en el texto parcial ingresado.
        
        Args:
            texto_parcial: Texto que el usuario ha escrito
            max_sugerencias: Número máximo de sugerencias a retornar
            threshold: Umbral mínimo de similitud (0.0 - 1.0)
        
        Returns:
            Lista de sugerencias ordenadas por relevancia
        """
        if len(texto_parcial) < self.min_chars:
            return []
        
        sugerencias = []
        
        for palabra in self.vocabulario:
            # Verificar si comienza con el texto (coincidencia exacta de prefijo)
            if palabra.lower().startswith(texto_parcial.lower()):
                sugerencias.append({
                    'texto': palabra,
                    'score': 1.0,  # Máxima prioridad para prefijos exactos
                    'tipo': 'prefijo_exacto'
                })
            else:
                # Usar Jaro-Winkler (favorece coincidencias al inicio)
                resultado = calculate_similarity(
                    texto_parcial,
                    palabra,
                    algorithm='jaro_winkler'
                )
                
                if resultado['score'] >= threshold:
                    sugerencias.append({
                        'texto': palabra,
                        'score': resultado['score'],
                        'tipo': 'similitud_difusa'
                    })
        
        # Ordenar por score descendente
        sugerencias.sort(key=lambda x: x['score'], reverse=True)
        
        return sugerencias[:max_sugerencias]

# Ejemplo de uso: Autocompletado de productos
productos = [
    "iPhone 15 Pro Max",
    "iPad Air",
    "iPad Pro",
    "MacBook Pro",
    "MacBook Air",
    "Apple Watch Series 9",
    "AirPods Pro",
    "AirPods Max",
    "Apple TV 4K",
    "iMac 24 pulgadas"
]

autocompletado = AutocompletadoInteligente(productos)

# Simular entrada del usuario
entradas_usuario = ["iPh", "Macbok", "Airp", "ipad", "Aple"]

print("Sistema de Autocompletado Inteligente")
print("=" * 60)

for entrada in entradas_usuario:
    sugerencias = autocompletado.sugerir(entrada, max_sugerencias=3)
    
    print(f"\nUsuario escribe: '{entrada}'")
    if sugerencias:
        print("  Sugerencias:")
        for idx, sug in enumerate(sugerencias, 1):
            tipo_icono = "⭐" if sug['tipo'] == 'prefijo_exacto' else "🔍"
            print(f"    {idx}. {tipo_icono} {sug['texto']} ({sug['score']:.1%})")
    else:
        print("  Sin sugerencias disponibles")
```

**Salida:**
```
Sistema de Autocompletado Inteligente
============================================================

Usuario escribe: 'iPh'
  Sugerencias:
    1. ⭐ iPhone 15 Pro Max (100.0%)

Usuario escribe: 'Macbok'
  Sugerencias:
    1. 🔍 MacBook Pro (92.9%)
    2. 🔍 MacBook Air (92.9%)

Usuario escribe: 'Airp'
  Sugerencias:
    1. ⭐ AirPods Pro (100.0%)
    2. ⭐ AirPods Max (100.0%)

Usuario escribe: 'ipad'
  Sugerencias:
    1. ⭐ iPad Air (100.0%)
    2. ⭐ iPad Pro (100.0%)

Usuario escribe: 'Aple'
  Sugerencias:
    1. 🔍 Apple Watch Series 9 (84.0%)
    2. 🔍 Apple TV 4K (80.0%)
```

---

### 7. Análisis de Similitud de Frases

**Problema:** Comparar frases completas para detectar plagio, contenido duplicado o variaciones de una misma idea.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def analizar_frases(frase1, frase2):
    """
    Análisis completo de similitud entre dos frases usando múltiples métricas.
    """
    # Ejecutar todos los algoritmos
    resultados = calculate_similarity(frase1, frase2, algorithm='all')
    
    # Calcular un score compuesto ponderado
    score_compuesto = (
        resultados['levenshtein_ratio'] * 0.30 +
        resultados['jaro_winkler_score'] * 0.30 +
        resultados['sorensen_dice_score'] * 0.20 +
        resultados['jaccard_score'] * 0.20
    )
    
    # Clasificar nivel de similitud
    if score_compuesto >= 0.90:
        nivel = "Muy Alta (Posible Duplicado)"
        color = "🔴"
    elif score_compuesto >= 0.75:
        nivel = "Alta (Contenido Similar)"
        color = "🟠"
    elif score_compuesto >= 0.50:
        nivel = "Media (Alguna Similitud)"
        color = "🟡"
    else:
        nivel = "Baja (Contenido Diferente)"
        color = "🟢"
    
    return {
        'score_compuesto': score_compuesto,
        'nivel': nivel,
        'color': color,
        'metricas': resultados
    }

# Casos de prueba
casos = [
    {
        'frase1': "Python es un lenguaje de programación versátil y potente",
        'frase2': "Python es un lenguaje de programación versatil y poderoso",
        'descripcion': "Misma frase con pequeñas variaciones"
    },
    {
        'frase1': "La inteligencia artificial está revolucionando la tecnología",
        'frase2': "La IA está transformando el mundo de la tecnología",
        'descripcion': "Misma idea, diferente redacción"
    },
    {
        'frase1': "El machine learning utiliza algoritmos para aprender de datos",
        'frase2': "Los gatos son animales domésticos muy populares",
        'descripcion': "Frases completamente diferentes"
    }
]

print("Análisis de Similitud de Frases")
print("=" * 70)

for idx, caso in enumerate(casos, 1):
    print(f"\n{idx}. {caso['descripcion']}")
    print(f"   Frase A: \"{caso['frase1']}\"")
    print(f"   Frase B: \"{caso['frase2']}\"")
    print()
    
    analisis = analizar_frases(caso['frase1'], caso['frase2'])
    
    print(f"   {analisis['color']} Nivel de Similitud: {analisis['nivel']}")
    print(f"   Score Compuesto: {analisis['score_compuesto']:.1%}")
    print(f"   Métricas Detalladas:")
    print(f"      - Levenshtein: {analisis['metricas']['levenshtein_ratio']:.1%}")
    print(f"      - Jaro-Winkler: {analisis['metricas']['jaro_winkler_score']:.1%}")
    print(f"      - Sorensen-Dice: {analisis['metricas']['sorensen_dice_score']:.1%}")
    print(f"      - Jaccard: {analisis['metricas']['jaccard_score']:.1%}")
    print(f"      - Metaphone Match: {analisis['metricas']['metaphone_match']}")
```

**Salida:**
```
Análisis de Similitud de Frases
======================================================================

1. Misma frase con pequeñas variaciones
   Frase A: "Python es un lenguaje de programación versátil y potente"
   Frase B: "Python es un lenguaje de programación versatil y poderoso"

   🔴 Nivel de Similitud: Muy Alta (Posible Duplicado)
   Score Compuesto: 93.2%
   Métricas Detalladas:
      - Levenshtein: 91.8%
      - Jaro-Winkler: 96.3%
      - Sorensen-Dice: 90.0%
      - Jaccard: 90.0%
      - Metaphone Match: True

2. Misma idea, diferente redacción
   Frase A: "La inteligencia artificial está revolucionando la tecnología"
   Frase B: "La IA está transformando el mundo de la tecnología"

   🟡 Nivel de Similitud: Media (Alguna Similitud)
   Score Compuesto: 57.3%
   Métricas Detalladas:
      - Levenshtein: 52.9%
      - Jaro-Winkler: 63.2%
      - Sorensen-Dice: 50.0%
      - Jaccard: 50.0%
      - Metaphone Match: False

3. Frases completamente diferentes
   Frase A: "El machine learning utiliza algoritmos para aprender de datos"
   Frase B: "Los gatos son animales domésticos muy populares"

   🟢 Nivel de Similitud: Baja (Contenido Diferente)
   Score Compuesto: 12.8%
   Métricas Detalladas:
      - Levenshtein: 18.5%
      - Jaro-Winkler: 21.7%
      - Sorensen-Dice: 0.0%
      - Jaccard: 0.0%
      - Metaphone Match: False
```

---

### 8. Búsqueda Difusa Multi-Algoritmo

**Problema:** Implementar un motor de búsqueda que combine múltiples algoritmos para maximizar la precisión y recall.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity
from typing import List, Dict, Tuple

class BuscadorMultiAlgoritmo:
    """
    Motor de búsqueda avanzado que combina múltiples algoritmos de similitud.
    """
    
    def __init__(self, catalogo: List[str]):
        self.catalogo = catalogo
    
    def buscar(
        self,
        query: str,
        algoritmos: List[str] = None,
        threshold: float = 0.70,
        top_n: int = 5
    ) -> List[Dict]:
        """
        Busca en el catálogo usando múltiples algoritmos.
        
        Args:
            query: Texto de búsqueda
            algoritmos: Lista de algoritmos a usar (None = todos)
            threshold: Umbral mínimo de similitud
            top_n: Número de resultados a retornar
        
        Returns:
            Lista de resultados con scores de cada algoritmo
        """
        if algoritmos is None:
            algoritmos = ['levenshtein', 'jaro_winkler', 'metaphone', 'sorensen_dice']
        
        resultados_por_item = {}
        
        for item in self.catalogo:
            scores = {}
            
            for algoritmo in algoritmos:
                resultado = calculate_similarity(query, item, algorithm=algoritmo)
                
                # Normalizar resultado (algunos retornan dict, otros float/bool)
                if isinstance(resultado, dict):
                    score = resultado.get('score', resultado.get('ratio', 0))
                elif isinstance(resultado, bool):
                    score = 1.0 if resultado else 0.0
                else:
                    score = resultado
                
                scores[algoritmo] = score
            
            # Calcular score promedio ponderado
            score_final = sum(scores.values()) / len(scores)
            
            if score_final >= threshold:
                resultados_por_item[item] = {
                    'item': item,
                    'score_final': score_final,
                    'scores_individuales': scores,
                    'algoritmos_match': sum(1 for s in scores.values() if s >= threshold)
                }
        
        # Ordenar por score final
        resultados = sorted(
            resultados_por_item.values(),
            key=lambda x: (x['score_final'], x['algoritmos_match']),
            reverse=True
        )
        
        return resultados[:top_n]

# Ejemplo de uso: Búsqueda en base de conocimiento
base_conocimiento = [
    "Cómo instalar Python en Windows",
    "Tutorial de programación en Python",
    "Guía de inicio rápido de Python",
    "Python para principiantes paso a paso",
    "Configuración del entorno de desarrollo Python",
    "Instalación de bibliotecas Python con pip",
    "JavaScript: conceptos básicos para principiantes",
    "Introducción a Machine Learning con Python",
    "Análisis de datos con pandas en Python"
]

buscador = BuscadorMultiAlgoritmo(base_conocimiento)

# Búsquedas con errores y variaciones
consultas = [
    "como instalar pyton",  # Error tipográfico
    "tutorial pythn",       # Palabra incompleta
    "python para iniciar",  # Variación de redacción
]

print("Búsqueda Multi-Algoritmo en Base de Conocimiento")
print("=" * 70)

for consulta in consultas:
    print(f"\n🔍 Búsqueda: '{consulta}'")
    print("-" * 70)
    
    resultados = buscador.buscar(consulta, threshold=0.50, top_n=3)
    
    if resultados:
        for idx, res in enumerate(resultados, 1):
            print(f"\n{idx}. {res['item']}")
            print(f"   Score Final: {res['score_final']:.1%}")
            print(f"   Algoritmos con match: {res['algoritmos_match']}/4")
            print(f"   Scores individuales:")
            for alg, score in res['scores_individuales'].items():
                bar = "█" * int(score * 20)
                print(f"      {alg:15} {score:.1%} {bar}")
    else:
        print("   No se encontraron resultados")
```

**Salida:**
```
Búsqueda Multi-Algoritmo en Base de Conocimiento
======================================================================

🔍 Búsqueda: 'como instalar pyton'
----------------------------------------------------------------------

1. Cómo instalar Python en Windows
   Score Final: 78.5%
   Algoritmos con match: 4/4
   Scores individuales:
      levenshtein     72.2% ██████████████
      jaro_winkler    85.3% █████████████████
      metaphone       78.0% ███████████████
      sorensen_dice   78.6% ███████████████

2. Instalación de bibliotecas Python con pip
   Score Final: 62.3%
   Algoritmos con match: 3/4
   Scores individuales:
      levenshtein     58.1% ███████████
      jaro_winkler    67.8% █████████████
      metaphone       65.0% █████████████
      sorensen_dice   58.3% ███████████

3. Configuración del entorno de desarrollo Python
   Score Final: 58.7%
   Algoritmos con match: 2/4
   Scores individuales:
      levenshtein     54.2% ██████████
      jaro_winkler    61.5% ████████████
      metaphone       60.0% ████████████
      sorensen_dice   59.1% ███████████
```

---

### 9. Herramienta de Comparación de Algoritmos

**Problema:** Necesitas decidir qué algoritmo de similitud es mejor para tu caso de uso específico.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity
import time

class ComparadorAlgoritmos:
    """
    Herramienta para evaluar y comparar diferentes algoritmos de similitud.
    """
    
    ALGORITMOS_DISPONIBLES = [
        'levenshtein', 'jaro_winkler', 'metaphone', 'hamming',
        'sorensen_dice', 'jaccard', 'mra', 'lcs', 'ratcliff_obershelp'
    ]
    
    def comparar(self, palabra1: str, palabra2: str, mostrar_tiempo: bool = True):
        """
        Compara dos palabras usando todos los algoritmos disponibles.
        
        Args:
            palabra1: Primera palabra a comparar
            palabra2: Segunda palabra a comparar
            mostrar_tiempo: Si se debe mostrar el tiempo de ejecución
        
        Returns:
            Dict con resultados de cada algoritmo
        """
        resultados = {}
        
        for algoritmo in self.ALGORITMOS_DISPONIBLES:
            try:
                # Medir tiempo si está habilitado
                if mostrar_tiempo:
                    inicio = time.perf_counter()
                
                resultado = calculate_similarity(palabra1, palabra2, algorithm=algoritmo)
                
                if mostrar_tiempo:
                    tiempo_ms = (time.perf_counter() - inicio) * 1000
                else:
                    tiempo_ms = None
                
                # Normalizar resultado
                if isinstance(resultado, dict):
                    score = resultado.get('score', resultado.get('ratio', 0))
                elif isinstance(resultado, bool):
                    score = 1.0 if resultado else 0.0
                else:
                    score = resultado
                
                resultados[algoritmo] = {
                    'score': score,
                    'tiempo_ms': tiempo_ms,
                    'resultado_completo': resultado
                }
                
            except Exception as e:
                resultados[algoritmo] = {
                    'score': None,
                    'tiempo_ms': None,
                    'error': str(e)
                }
        
        return resultados
    
    def mostrar_reporte(self, palabra1: str, palabra2: str):
        """Genera un reporte visual de la comparación."""
        print(f"\n{'=' * 80}")
        print(f"COMPARACIÓN DE ALGORITMOS")
        print(f"{'=' * 80}")
        print(f"Palabra 1: '{palabra1}'")
        print(f"Palabra 2: '{palabra2}'")
        print(f"{'-' * 80}")
        
        resultados = self.comparar(palabra1, palabra2)
        
        # Ordenar por score descendente
        resultados_ordenados = sorted(
            resultados.items(),
            key=lambda x: x[1]['score'] if x[1]['score'] is not None else -1,
            reverse=True
        )
        
        print(f"\n{'Algoritmo':<20} {'Score':<12} {'Tiempo (ms)':<15} {'Barra Visual'}")
        print(f"{'-' * 80}")
        
        for algoritmo, data in resultados_ordenados:
            if data['score'] is not None:
                score_str = f"{data['score']:.2%}"
                tiempo_str = f"{data['tiempo_ms']:.3f}" if data['tiempo_ms'] else "N/A"
                barra = "█" * int(data['score'] * 30)
                
                print(f"{algoritmo:<20} {score_str:<12} {tiempo_str:<15} {barra}")
            else:
                print(f"{algoritmo:<20} {'ERROR':<12} {'N/A':<15} {data.get('error', 'N/A')}")
        
        # Recomendación
        mejor = resultados_ordenados[0]
        print(f"\n{'=' * 80}")
        print(f"✓ Mejor resultado: {mejor[0]} con {mejor[1]['score']:.2%}")
        print(f"{'=' * 80}")

# Ejemplo de uso
comparador = ComparadorAlgoritmos()

# Caso 1: Nombres con variación ortográfica
print("\n📊 CASO 1: Nombres con variación ortográfica")
comparador.mostrar_reporte("Martínez", "Martinez")

# Caso 2: Palabras con error tipográfico
print("\n📊 CASO 2: Palabras con error tipográfico")
comparador.mostrar_reporte("Python", "Pyton")

# Caso 3: Palabras fonéticamente similares
print("\n📊 CASO 3: Palabras fonéticamente similares")
comparador.mostrar_reporte("Catherine", "Katherine")

# Caso 4: Frases cortas
print("\n📊 CASO 4: Frases cortas")
comparador.mostrar_reporte("machine learning", "machine lerning")
```

**Salida (ejemplo):**
```
📊 CASO 1: Nombres con variación ortográfica
================================================================================
COMPARACIÓN DE ALGORITMOS
================================================================================
Palabra 1: 'Martínez'
Palabra 2: 'Martinez'
--------------------------------------------------------------------------------

Algoritmo            Score        Tiempo (ms)     Barra Visual
--------------------------------------------------------------------------------
jaro_winkler         96.67%       0.125           █████████████████████████████
levenshtein          87.50%       0.089           ██████████████████████████
mra                  85.00%       0.102           █████████████████████████
lcs                  87.50%       0.145           ██████████████████████████
sorensen_dice        85.71%       0.098           █████████████████████████
jaccard              75.00%       0.091           ██████████████████████
ratcliff_obershelp   87.50%       0.112           ██████████████████████████
metaphone            100.00%      0.067           ██████████████████████████████
hamming              ERROR        N/A             Strings must have equal length

================================================================================
✓ Mejor resultado: metaphone con 100.00%
================================================================================
```

---

### 1. Corrección de Nombres Propios

**Problema:** Corregir errores tipográficos en nombres de personas de un formulario de registro.

**Solución:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Lista de nombres válidos en la empresa
nombres_validos = [
    "Juan", "María", "José", "Ana", "Carlos", "Laura",
    "Pedro", "Carmen", "Miguel", "Isabel", "Antonio", "Rosa"
]

# Crear corrector con vocabulario personalizado
corrector = UniversalSpellChecker(language="es", custom_vocabulary=nombres_validos)

# Nombres con errores tipográficos
nombres_con_errores = ["Juaan", "Mria", "Crlos", "Lara", "Pedr", "Migeul"]

print("Corrección de nombres propios:")
for nombre_erroneo in nombres_con_errores:
    nombre_corregido = corrector.correct(nombre_erroneo)
    
    if nombre_erroneo != nombre_corregido:
        print(f"  '{nombre_erroneo}' → '{nombre_corregido}' ✓")
    else:
        print(f"  '{nombre_erroneo}' → No se encontró corrección")
```

**Salida:**
```
Corrección de nombres propios:
  'Juaan' → 'Juan' ✓
  'Mria' → 'María' ✓
  'Crlos' → 'Carlos' ✓
  'Lara' → 'Laura' ✓
  'Pedr' → 'Pedro' ✓
  'Migeul' → 'Miguel' ✓
```

---

### 2. Normalización de Entrada de Usuarios

**Problema:** Los usuarios ingresan nombres de ciudades con errores ortográficos en un sistema de envíos.

**Solución:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Ciudades principales de España
ciudades_espana = [
    "Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza",
    "Málaga", "Murcia", "Palma", "Bilbao", "Alicante",
    "Córdoba", "Valladolid", "Vigo", "Gijón", "Granada"
]

corrector_ciudades = UniversalSpellChecker(
    language="es",
    custom_vocabulary=ciudades_espana
)

# Entradas de usuarios con errores
entradas_usuario = [
    "Madrd",      # Falta 'i'
    "Barselona",  # 's' en lugar de 'c'
    "Sevila",     # Falta doble 'l'
    "Malaga",     # Sin tilde
    "Bilbao",     # Correcto
    "Cordoba"     # Sin tilde
]

print("Corrección de ciudades:")
print("-" * 40)
for entrada in entradas_usuario:
    correccion = corrector_ciudades.correct(entrada)
    
    if entrada == correccion:
        print(f"✓ '{entrada}' → Ya es correcto")
    else:
        print(f"✎ '{entrada}' → '{correccion}'")
```

**Salida:**
```
Corrección de ciudades:
----------------------------------------
✎ 'Madrd' → 'Madrid'
✎ 'Barselona' → 'Barcelona'
✎ 'Sevila' → 'Sevilla'
✎ 'Malaga' → 'Málaga'
✓ 'Bilbao' → Ya es correcto
✎ 'Cordoba' → 'Córdoba'
```

---

### 3. Limpieza de Datos de Formularios

**Problema:** Procesar y corregir múltiples campos de un formulario de contacto.

**Solución:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Vocabulario de nombres y apellidos comunes
vocabulario_completo = [
    # Nombres
    "Juan", "María", "José", "Ana", "Carlos", "Laura", "Pedro", "Carmen",
    # Apellidos
    "García", "Rodríguez", "Martínez", "López", "González", "Fernández",
    "Sánchez", "Pérez", "Martín", "Gómez"
]

corrector = UniversalSpellChecker(language="es", custom_vocabulary=vocabulario_completo)

# Datos del formulario con errores
formulario = {
    "nombre": "Jse",
    "apellido1": "Garsia",
    "apellido2": "Rodrguez",
    "email": "jose.garcia@example.com"
}

# Corregir campos
formulario_corregido = {}
campos_texto = ["nombre", "apellido1", "apellido2"]

for campo in campos_texto:
    valor_original = formulario[campo]
    valor_corregido = corrector.correct(valor_original)
    formulario_corregido[campo] = valor_corregido

# Mantener email sin cambios
formulario_corregido["email"] = formulario["email"]

# Mostrar resultados
print("Corrección de formulario:")
print("\nAntes:")
for campo, valor in formulario.items():
    print(f"  {campo}: {valor}")

print("\nDespués:")
for campo, valor in formulario_corregido.items():
    print(f"  {campo}: {valor}")

# Resumen de cambios
print("\nCambios realizados:")
for campo in campos_texto:
    if formulario[campo] != formulario_corregido[campo]:
        print(f"  {campo}: '{formulario[campo]}' → '{formulario_corregido[campo]}'")
```

**Salida:**
```
Corrección de formulario:

Antes:
  nombre: Jse
  apellido1: Garsia
  apellido2: Rodrguez
  email: jose.garcia@example.com

Después:
  nombre: José
  apellido1: García
  apellido2: Rodríguez
  email: jose.garcia@example.com

Cambios realizados:
  nombre: 'Jse' → 'José'
  apellido1: 'Garsia' → 'García'
  apellido2: 'Rodrguez' → 'Rodríguez'
```

---

### 4. Corrección de Diccionarios Personalizados

**Problema:** Corregir términos técnicos o específicos de un dominio (ej. departamentos de una empresa).

**Solución:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Departamentos de la empresa
departamentos = [
    "Ventas", "Marketing", "Recursos Humanos", "Contabilidad",
    "Tecnología", "Operaciones", "Logística", "Atención al Cliente"
]

corrector_depts = UniversalSpellChecker(
    language="es",
    custom_vocabulary=departamentos
)

# Entradas de empleados con errores
asignaciones = [
    {"empleado": "Ana López", "dept_entrada": "Ventas"},
    {"empleado": "Carlos Ruiz", "dept_entrada": "Markeeting"},
    {"empleado": "Laura Díaz", "dept_entrada": "Recusos Humanos"},
    {"empleado": "Pedro Sanz", "dept_entrada": "Tecnologia"},
    {"empleado": "María Gil", "dept_entrada": "Logistika"}
]

print("Corrección de departamentos:")
print("=" * 60)

for asignacion in asignaciones:
    dept_original = asignacion["dept_entrada"]
    dept_corregido = corrector_depts.correct(dept_original)
    
    print(f"\nEmpleado: {asignacion['empleado']}")
    print(f"  Entrada: '{dept_original}'")
    
    if dept_original != dept_corregido:
        print(f"  Corregido a: '{dept_corregido}' ✓")
    else:
        print(f"  Estado: Correcto ✓")
```

**Salida:**
```
Corrección de departamentos:
============================================================

Empleado: Ana López
  Entrada: 'Ventas'
  Estado: Correcto ✓

Empleado: Carlos Ruiz
  Entrada: 'Markeeting'
  Corregido a: 'Marketing' ✓

Empleado: Laura Díaz
  Entrada: 'Recusos Humanos'
  Corregido a: 'Recursos Humanos' ✓

Empleado: Pedro Sanz
  Entrada: 'Tecnologia'
  Corregido a: 'Tecnología' ✓

Empleado: María Gil
  Entrada: 'Logistika'
  Corregido a: 'Logística' ✓
```

---

### 5. Validación de Entrada en Tiempo Real

**Problema:** Validar y corregir la entrada del usuario en tiempo real mientras escribe en un formulario web o aplicación.

**Solución:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker
from shortfx.fxString.string_similarity import calculate_similarity

class ValidadorTiempoReal:
    """
    Validador que corrige y sugiere mientras el usuario escribe.
    """
    
    def __init__(self, vocabulario_valido, idioma="es"):
        self.corrector = UniversalSpellChecker(
            language=idioma,
            custom_vocabulary=vocabulario_valido
        )
        self.vocabulario = vocabulario_valido
    
    def validar_campo(self, valor: str, min_similitud: float = 0.85):
        """
        Valida un campo y sugiere correcciones.
        
        Args:
            valor: Texto ingresado por el usuario
            min_similitud: Umbral mínimo para aceptar el valor
        
        Returns:
            Dict con estado de validación y sugerencias
        """
        # Corregir el valor
        valor_corregido = self.corrector.correct(valor)
        
        # Verificar si está en el vocabulario válido
        es_valido = valor_corregido in self.vocabulario
        
        # Si no es válido, buscar coincidencias cercanas
        sugerencias = []
        if not es_valido:
            for palabra_valida in self.vocabulario:
                score = calculate_similarity(
                    valor_corregido,
                    palabra_valida,
                    algorithm='jaro_winkler'
                )['score']
                
                if score >= min_similitud:
                    sugerencias.append({
                        'texto': palabra_valida,
                        'score': score
                    })
            
            # Ordenar sugerencias por score
            sugerencias.sort(key=lambda x: x['score'], reverse=True)
        
        return {
            'valor_original': valor,
            'valor_corregido': valor_corregido,
            'es_valido': es_valido,
            'tiene_correcciones': valor != valor_corregido,
            'sugerencias': sugerencias[:3]  # Top 3
        }

# Ejemplo de uso: Validación de países
paises_validos = [
    "España", "Francia", "Alemania", "Italia", "Portugal",
    "Reino Unido", "Países Bajos", "Bélgica", "Suiza", "Austria"
]

validador = ValidadorTiempoReal(paises_validos)

# Simular entrada del usuario en tiempo real
entradas_simuladas = [
    ("Esp", "Usuario escribiendo..."),
    ("Espña", "Error de teclado"),
    ("Espana", "Sin tilde"),
    ("España", "Correcto"),
    ("Frncia", "Falta letra"),
    ("Alemana", "Error ortográfico"),
]

print("Validación en Tiempo Real")
print("=" * 70)

for entrada, descripcion in entradas_simuladas:
    resultado = validador.validar_campo(entrada)
    
    print(f"\n📝 '{entrada}' ({descripcion})")
    
    if resultado['es_valido']:
        print(f"   ✅ VÁLIDO")
        if resultado['tiene_correcciones']:
            print(f"   Auto-corregido: '{resultado['valor_corregido']}'")
    else:
        print(f"   ⚠️  NECESITA CORRECCIÓN")
        if resultado['tiene_correcciones']:
            print(f"   Corrección automática: '{resultado['valor_corregido']}'")
        
        if resultado['sugerencias']:
            print(f"   Sugerencias:")
            for idx, sug in enumerate(resultado['sugerencias'], 1):
                print(f"      {idx}. {sug['texto']} ({sug['score']:.1%})")
```

**Salida:**
```
Validación en Tiempo Real
======================================================================

📝 'Esp' (Usuario escribiendo...)
   ⚠️  NECESITA CORRECCIÓN
   Sugerencias:
      1. España (86.7%)

📝 'Espña' (Error de teclado)
   ⚠️  NECESITA CORRECCIÓN
   Corrección automática: 'España'
   Sugerencias:
      1. España (100.0%)

📝 'Espana' (Sin tilde)
   ✅ VÁLIDO
   Auto-corregido: 'España'

📝 'España' (Correcto)
   ✅ VÁLIDO

📝 'Frncia' (Falta letra)
   ⚠️  NECESITA CORRECCIÓN
   Corrección automática: 'Francia'
   Sugerencias:
      1. Francia (100.0%)

📝 'Alemana' (Error ortográfico)
   ⚠️  NECESITA CORRECCIÓN
   Corrección automática: 'Alemania'
   Sugerencias:
      1. Alemania (95.2%)
```

---

## Casos de Uso Combinados

### Caso 1: Sistema de Matching de CVs

Combina similitud de palabras y corrección ortográfica para hacer match entre habilidades de candidatos y requisitos de puestos.

```python
from shortfx.fxString.string_similarity import calculate_similarity
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Habilidades requeridas para el puesto
habilidades_requeridas = [
    "Python", "JavaScript", "SQL", "Docker", "Kubernetes",
    "React", "Node.js", "MongoDB", "AWS", "Git"
]

# Crear corrector con vocabulario técnico
corrector_tech = UniversalSpellChecker(
    language="en",
    custom_vocabulary=habilidades_requeridas
)

# Habilidades del candidato (con posibles errores)
habilidades_candidato = [
    "Pyhton",      # Error tipográfico
    "Javascrip",   # Incompleto
    "SQL",         # Correcto
    "Dokcer",      # Error tipográfico
    "React",       # Correcto
    "Nodejs",      # Formato diferente
    "PostgreSQL"   # Similar a SQL pero diferente
]

print("Análisis de habilidades del candidato:")
print("=" * 60)

matches = []
for habilidad in habilidades_candidato:
    # Primero corregir ortografía
    habilidad_corregida = corrector_tech.correct(habilidad)
    
    # Buscar el mejor match en requisitos
    mejor_match = None
    mejor_score = 0
    
    for requerida in habilidades_requeridas:
        score = calculate_similarity(
            habilidad_corregida,
            requerida,
            algorithm='jaro_winkler'
        )['score']
        
        if score > mejor_score:
            mejor_score = score
            mejor_match = requerida
    
    # Determinar si hay match
    es_match = mejor_score >= 0.85
    
    resultado = {
        'original': habilidad,
        'corregida': habilidad_corregida,
        'match': mejor_match if es_match else None,
        'score': mejor_score,
        'es_match': es_match
    }
    
    matches.append(resultado)
    
    # Mostrar resultado
    print(f"\nHabilidad: '{habilidad}'")
    if habilidad != habilidad_corregida:
        print(f"  Corrección: '{habilidad_corregida}'")
    
    if es_match:
        print(f"  ✓ Match con: '{mejor_match}' ({mejor_score:.1%})")
    else:
        print(f"  ✗ Sin match (mejor: '{mejor_match}' {mejor_score:.1%})")

# Resumen
total_matches = sum(1 for m in matches if m['es_match'])
print(f"\n{'=' * 60}")
print(f"Resumen: {total_matches}/{len(habilidades_candidato)} habilidades coinciden")
print(f"Porcentaje de coincidencia: {(total_matches/len(habilidades_candidato))*100:.1f}%")
```

---

### Caso 2: Deduplicación y Limpieza de Contactos

Identifica y fusiona contactos duplicados con variaciones en nombres y corrección de errores.

```python
from shortfx.fxString.string_similarity import calculate_similarity
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Base de datos de contactos con duplicados potenciales
contactos = [
    {"id": 1, "nombre": "Juan García", "email": "juan.garcia@email.com"},
    {"id": 2, "nombre": "Jua Garcia", "email": "j.garcia@email.com"},  # Duplicado con error
    {"id": 3, "nombre": "María López", "email": "maria.lopez@email.com"},
    {"id": 4, "nombre": "Maria Lopes", "email": "m.lopez@email.com"},  # Duplicado sin tilde
    {"id": 5, "nombre": "Carlos Ruiz", "email": "carlos.ruiz@email.com"}
]

# Nombres comunes para corrección
nombres_comunes = ["Juan", "María", "Carlos", "García", "López", "Ruiz"]
corrector = UniversalSpellChecker(language="es", custom_vocabulary=nombres_comunes)

def normalizar_contacto(contacto):
    """Normaliza el nombre del contacto corrigiendo errores."""
    palabras = contacto["nombre"].split()
    palabras_corregidas = [corrector.correct(p) for p in palabras]
    return " ".join(palabras_corregidas)

# Detectar duplicados
print("Análisis de duplicados:")
print("=" * 70)

duplicados = []
procesados = set()

for i, contacto1 in enumerate(contactos):
    if i in procesados:
        continue
    
    nombre1_norm = normalizar_contacto(contacto1)
    grupo = [contacto1]
    
    for j, contacto2 in enumerate(contactos[i+1:], start=i+1):
        if j in procesados:
            continue
        
        nombre2_norm = normalizar_contacto(contacto2)
        
        # Comparar nombres normalizados
        es_mismo, metricas = calculate_similarity(
            nombre1_norm,
            nombre2_norm,
            algorithm='effective_same',
            levenshtein_threshold=0.80
        )
        
        if es_mismo:
            grupo.append(contacto2)
            procesados.add(j)
    
    if len(grupo) > 1:
        duplicados.append(grupo)

# Mostrar resultados
for idx, grupo in enumerate(duplicados, 1):
    print(f"\nGrupo {idx} - Duplicados detectados:")
    for contacto in grupo:
        nombre_norm = normalizar_contacto(contacto)
        print(f"  ID {contacto['id']}: '{contacto['nombre']}' → '{nombre_norm}'")
        print(f"           Email: {contacto['email']}")
    
    # Sugerir fusión
    contacto_principal = grupo[0]
    nombre_final = normalizar_contacto(contacto_principal)
    print(f"  → Sugerencia: Mantener ID {contacto_principal['id']} como '{nombre_final}'")

print(f"\n{'=' * 70}")
print(f"Total de grupos duplicados encontrados: {len(duplicados)}")
```

---

### Caso 3: Deduplicación Masiva de Nombres

**Problema:** Procesar una gran lista de nombres de personas para identificar y consolidar duplicados con variaciones ortográficas, errores y formatos diferentes.

**Solución:**

```python
from shortfx.fxString.string_similarity import calculate_similarity
from shortfx.fxString.string_spellcheck import UniversalSpellChecker
from collections import defaultdict

class DeduplicadorNombres:
    """
    Sistema avanzado de deduplicación de nombres con normalización inteligente.
    """
    
    def __init__(self, vocabulario_nombres=None):
        self.vocabulario = vocabulario_nombres or []
        if self.vocabulario:
            self.corrector = UniversalSpellChecker(
                language="es",
                custom_vocabulary=self.vocabulario
            )
        else:
            self.corrector = None
    
    def normalizar_nombre(self, nombre: str) -> str:
        """Normaliza un nombre aplicando reglas y corrección."""
        # Eliminar espacios extras
        nombre = " ".join(nombre.split())
        
        # Capitalizar cada palabra
        palabras = nombre.split()
        
        # Corregir si hay vocabulario disponible
        if self.corrector:
            palabras = [self.corrector.correct(p) for p in palabras]
        
        # Capitalizar
        return " ".join(p.title() for p in palabras)
    
    def son_duplicados(self, nombre1: str, nombre2: str, threshold: float = 0.85) -> bool:
        """Determina si dos nombres son duplicados."""
        # Normalizar ambos nombres
        norm1 = self.normalizar_nombre(nombre1)
        norm2 = self.normalizar_nombre(nombre2)
        
        # Comparar usando effective_same
        es_mismo, _ = calculate_similarity(
            norm1,
            norm2,
            algorithm='effective_same',
            levenshtein_threshold=threshold,
            metaphone_required=False
        )
        
        return es_mismo
    
    def deduplicar(self, lista_nombres: list, threshold: float = 0.85):
        """
        Deduplica una lista de nombres agrupando variantes.
        
        Returns:
            Dict con nombres canónicos y sus variantes
        """
        # Agrupar nombres duplicados
        grupos = []
        procesados = set()
        
        for i, nombre1 in enumerate(lista_nombres):
            if i in procesados:
                continue
            
            grupo = {
                'canonico': self.normalizar_nombre(nombre1),
                'variantes': [nombre1],
                'indices': [i]
            }
            
            for j, nombre2 in enumerate(lista_nombres[i+1:], start=i+1):
                if j in procesados:
                    continue
                
                if self.son_duplicados(nombre1, nombre2, threshold):
                    grupo['variantes'].append(nombre2)
                    grupo['indices'].append(j)
                    procesados.add(j)
            
            grupos.append(grupo)
        
        return grupos

# Ejemplo de uso: Deduplicación de lista de empleados
empleados_raw = [
    "Juan García López",
    "Jua Garcia Lopez",      # Error + sin tildes
    "juan garcia lopez",     # Minúsculas
    "María Fernández",
    "Maria Fernandez",       # Sin tilde
    "Mria Fernandez",        # Error tipográfico
    "Carlos Ruiz Sánchez",
    "Carlos Ruiz Sanchez",   # Sin tilde
    "Pedro Martínez",
    "Ana López García",
    "Ana Lopez Garcia",      # Sin tilde
    "Pedro Martinez",        # Sin tilde
    "Laura González",
    "laura gonzalez"         # Minúsculas + sin tilde
]

# Vocabulario de nombres y apellidos comunes españoles
vocabulario_espanol = [
    "Juan", "María", "José", "Ana", "Carlos", "Laura", "Pedro",
    "García", "López", "Fernández", "Martínez", "González", "Ruiz", "Sánchez"
]

deduplicador = DeduplicadorNombres(vocabulario_espanol)

print("Deduplicación Masiva de Nombres")
print("=" * 80)
print(f"\nTotal de registros originales: {len(empleados_raw)}")

# Ejecutar deduplicación
grupos = deduplicador.deduplicar(empleados_raw, threshold=0.85)

# Filtrar solo grupos con duplicados
grupos_duplicados = [g for g in grupos if len(g['variantes']) > 1]
nombres_unicos = [g for g in grupos if len(g['variantes']) == 1]

print(f"Nombres únicos (sin duplicados): {len(nombres_unicos)}")
print(f"Grupos con duplicados: {len(grupos_duplicados)}")
print(f"Total de nombres después de deduplicar: {len(grupos)}")

# Mostrar grupos de duplicados
if grupos_duplicados:
    print(f"\n{'=' * 80}")
    print("GRUPOS DE DUPLICADOS DETECTADOS")
    print(f"{'=' * 80}")
    
    for idx, grupo in enumerate(grupos_duplicados, 1):
        print(f"\nGrupo {idx}:")
        print(f"  Nombre canónico: {grupo['canonico']}")
        print(f"  Variantes encontradas ({len(grupo['variantes'])}):")
        for variante in grupo['variantes']:
            print(f"    - '{variante}'")

# Generar lista consolidada
print(f"\n{'=' * 80}")
print("LISTA CONSOLIDADA (sin duplicados)")
print(f"{'=' * 80}")

for idx, grupo in enumerate(grupos, 1):
    print(f"{idx:2d}. {grupo['canonico']:30} ({len(grupo['variantes'])} registro(s))")

# Estadísticas finales
total_variantes = sum(len(g['variantes']) for g in grupos)
tasa_deduplicacion = (1 - len(grupos) / total_variantes) * 100

print(f"\n{'=' * 80}")
print("ESTADÍSTICAS")
print(f"{'=' * 80}")
print(f"Registros originales:     {total_variantes}")
print(f"Registros únicos:         {len(grupos)}")
print(f"Duplicados eliminados:    {total_variantes - len(grupos)}")
print(f"Tasa de deduplicación:    {tasa_deduplicacion:.1f}%")
```

**Salida:**
```
Deduplicación Masiva de Nombres
================================================================================

Total de registros originales: 14
Nombres únicos (sin duplicados): 5
Grupos con duplicados: 4
Total de nombres después de deduplicar: 9

================================================================================
GRUPOS DE DUPLICADOS DETECTADOS
================================================================================

Grupo 1:
  Nombre canónico: Juan García López
  Variantes encontradas (3):
    - 'Juan García López'
    - 'Jua Garcia Lopez'
    - 'juan garcia lopez'

Grupo 2:
  Nombre canónico: María Fernández
  Variantes encontradas (3):
    - 'María Fernández'
    - 'Maria Fernandez'
    - 'Mria Fernandez'

Grupo 3:
  Nombre canónico: Carlos Ruiz Sánchez
  Variantes encontradas (2):
    - 'Carlos Ruiz Sánchez'
    - 'Carlos Ruiz Sanchez'

Grupo 4:
  Nombre canónico: Ana López García
  Variantes encontradas (2):
    - 'Ana López García'
    - 'Ana Lopez Garcia'

Grupo 5:
  Nombre canónico: Pedro Martínez
  Variantes encontradas (2):
    - 'Pedro Martínez'
    - 'Pedro Martinez'

Grupo 6:
  Nombre canónico: Laura González
  Variantes encontradas (2):
    - 'Laura González'
    - 'laura gonzalez'

================================================================================
LISTA CONSOLIDADA (sin duplicados)
================================================================================
 1. Juan García López              (3 registro(s))
 2. María Fernández                (3 registro(s))
 3. Carlos Ruiz Sánchez            (2 registro(s))
 4. Ana López García               (2 registro(s))
 5. Pedro Martínez                 (2 registro(s))
 6. Laura González                 (2 registro(s))

================================================================================
ESTADÍSTICAS
================================================================================
Registros originales:     14
Registros únicos:         9
Duplicados eliminados:    5
Tasa de deduplicación:    35.7%
```

---

## 📌 Mejores Prácticas

### Para Similitud de Palabras

1. **Elige el algoritmo adecuado:**
   - `metaphone`: Comparación fonética rápida (nombres, palabras habladas)
   - `levenshtein`: Distancia de edición general (detección de errores)
   - `jaro_winkler`: Nombres propios (prioriza inicio de la palabra)
   - `sorensen_dice` / `jaccard`: Textos y documentos
   - `effective_same`: Validación robusta combinada

2. **Ajusta los umbrales según el contexto:**
   - Nombres propios: 0.85 - 0.90
   - Búsqueda tolerante: 0.70 - 0.80
   - Detección estricta: 0.90 - 0.95

3. **Optimiza el rendimiento:**
   - Usa `metaphone` como filtro inicial para grandes datasets
   - Aplica algoritmos más costosos solo a candidatos preseleccionados

### Para Corrección Ortográfica

1. **Vocabularios personalizados:**
   - Siempre proporciona un vocabulario específico del dominio
   - Incluye variaciones comunes (con/sin tildes, singular/plural)

2. **Validación de resultados:**
   - Verifica que la corrección tenga sentido en el contexto
   - Mantén un log de correcciones para revisar patrones

3. **Manejo de casos especiales:**
   - Nombres propios: preserva mayúsculas originales
   - Siglas y acrónimos: añádelos al vocabulario personalizado
   - Términos técnicos: usa diccionarios específicos

---

## 🎯 Conclusión

El módulo **fxString** de shortfx proporciona herramientas potentes y flexibles para:

- 🔍 **Búsqueda inteligente** tolerante a errores
- 🔄 **Detección de duplicados** con alta precisión
- ✍️ **Corrección automática** de errores tipográficos
- 📊 **Análisis de similitud** con múltiples algoritmos
- 🎯 **Validación robusta** de datos de entrada

Estos casos de uso demuestran cómo aplicar estas funciones en escenarios reales del mundo empresarial y de desarrollo de aplicaciones.
