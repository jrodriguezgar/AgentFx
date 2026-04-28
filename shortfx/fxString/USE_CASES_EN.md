# fxString - Practical Use Cases

This document presents real-world use cases for the **fxString** module in shortfx, with special emphasis on **word similarity** and **spellcheck** functionality.

## 📋 Table of Contents

- [Word Similarity](#word-similarity)
  - [1. Fuzzy Database Search](#1-fuzzy-database-search)
  - [2. Duplicate Detection](#2-duplicate-detection)
  - [3. Person Name Validation](#3-person-name-validation)
  - [4. Error-Tolerant Search](#4-error-tolerant-search)
  - [5. Document Comparison](#5-document-comparison)
  - [6. Intelligent Autocomplete System](#6-intelligent-autocomplete-system)
  - [7. Sentence Similarity Analysis](#7-sentence-similarity-analysis)
  - [8. Multi-Algorithm Fuzzy Search](#8-multi-algorithm-fuzzy-search)
  - [9. Algorithm Comparison Tool](#9-algorithm-comparison-tool)
- [Spellcheck](#spellcheck)
  - [1. Proper Name Correction](#1-proper-name-correction)
  - [2. User Input Normalization](#2-user-input-normalization)
  - [3. Form Data Cleaning](#3-form-data-cleaning)
  - [4. Custom Dictionary Correction](#4-custom-dictionary-correction)
  - [5. Real-Time Input Validation](#5-real-time-input-validation)
- [Combined Use Cases](#combined-use-cases)
  - [Case 1: Resume Matching System](#case-1-resume-matching-system)
  - [Case 2: Contact Deduplication and Cleaning](#case-2-contact-deduplication-and-cleaning)
  - [Case 3: Massive Name Deduplication](#case-3-massive-name-deduplication)

---

## Word Similarity

### 1. Fuzzy Database Search

**Problem:** A user searches for "Marti" in a customer system, but the actual name is "Martín" or "Martha".

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

# Customer database
customers = ["Martín García", "Martha Rodríguez", "María López", "Marco Sánchez"]
search = "Marti"

# Find matches using Jaro-Winkler (ideal for names)
results = []
for customer in customers:
    name = customer.split()[0]  # Get first name
    result = calculate_similarity(search, name, algorithm='jaro_winkler')
    
    if result['score'] > 0.75:  # Similarity threshold
        results.append({
            'customer': customer,
            'score': result['score'],
            'match': result['score'] > 0.9
        })

# Sort by score descending
results.sort(key=lambda x: x['score'], reverse=True)

for r in results:
    print(f"{r['customer']}: {r['score']:.2%} - {'✓ High' if r['match'] else 'Possible'}")
```

**Output:**
```
Martín García: 95.56% - ✓ High
Martha Rodríguez: 93.33% - ✓ High
Marco Sánchez: 76.67% - Possible
```

---

### 2. Duplicate Detection

**Problem:** Identify duplicate records in a product list with similar names written differently.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

products = [
    "Laptop HP Pavilion 15",
    "Laptop HP Pavillion 15",  # Spelling error
    "Laptop HP Pavilion 15.6",
    "Mouse Logitech MX Master",
    "Mouse Logitec MX Master"   # Spelling error
]

# Detect duplicates using Levenshtein
duplicates = []
visited = set()

for i, prod1 in enumerate(products):
    if i in visited:
        continue
    
    group = [prod1]
    
    for j, prod2 in enumerate(products[i+1:], start=i+1):
        if j in visited:
            continue
        
        # Use Levenshtein to detect similarity
        ratio = calculate_similarity(prod1, prod2, algorithm='levenshtein')
        
        if ratio > 0.85:  # 85% similarity
            group.append(prod2)
            visited.add(j)
    
    if len(group) > 1:
        duplicates.append(group)

# Display results
for idx, group in enumerate(duplicates, 1):
    print(f"\nGroup {idx} (possible duplicates):")
    for product in group:
        print(f"  - {product}")
```

**Output:**
```
Group 1 (possible duplicates):
  - Laptop HP Pavilion 15
  - Laptop HP Pavillion 15
  - Laptop HP Pavilion 15.6

Group 2 (possible duplicates):
  - Mouse Logitech MX Master
  - Mouse Logitec MX Master
```

---

### 3. Person Name Validation

**Problem:** Verify if two names probably refer to the same person, considering spelling and phonetic variations.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def are_same_name(name1, name2):
    """
    Determines if two names probably refer to the same person.
    """
    result, metrics = calculate_similarity(
        name1, 
        name2, 
        algorithm='effective_same',
        levenshtein_threshold=0.80,
        jaro_winkler_threshold=0.85,
        metaphone_required=False  # Allow more flexibility
    )
    
    return result, metrics

# Test cases
name_pairs = [
    ("José García", "Jose Garcia"),      # Without accent
    ("María López", "Maria Lopez"),      # Without accent
    ("Julián", "Julian"),                # Without accent
    ("Catherine", "Katherine"),          # Phonetic variation
    ("John", "Juan"),                    # Different names
    ("Chris", "Christopher")             # Diminutive
]

for name1, name2 in name_pairs:
    is_same, metrics = are_same_name(name1, name2)
    
    print(f"\n'{name1}' vs '{name2}'")
    print(f"  Same person? {is_same}")
    print(f"  Levenshtein: {metrics['levenshtein_ratio']:.2%}")
    print(f"  Jaro-Winkler: {metrics['jaro_winkler_score']:.2%}")
    print(f"  Metaphone: {metrics['metaphone_match']}")
```

**Output:**
```
'José García' vs 'Jose Garcia'
  Same person? True
  Levenshtein: 91.67%
  Jaro-Winkler: 95.56%
  Metaphone: True

'Catherine' vs 'Katherine'
  Same person? True
  Levenshtein: 88.89%
  Jaro-Winkler: 92.22%
  Metaphone: True

'John' vs 'Juan'
  Same person? False
  Levenshtein: 50.00%
  Jaro-Winkler: 63.33%
  Metaphone: False
```

---

### 4. Error-Tolerant Search

**Problem:** Implement a search system that tolerates common typing errors.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def intelligent_search(query, catalog, threshold=0.75):
    """
    Search that tolerates typing errors using multiple algorithms.
    """
    results = []
    
    for item in catalog:
        # First pass: fast filter with Metaphone (phonetic)
        if calculate_similarity(query, item, algorithm='metaphone'):
            # Second pass: similarity score with Levenshtein
            score = calculate_similarity(query, item, algorithm='levenshtein')
            
            if score >= threshold:
                results.append({
                    'item': item,
                    'score': score,
                    'type': 'phonetic + lexical'
                })
        else:
            # Alternative: Jaro-Winkler for cases without phonetic match
            jw_result = calculate_similarity(query, item, algorithm='jaro_winkler')
            
            if jw_result['score'] >= threshold:
                results.append({
                    'item': item,
                    'score': jw_result['score'],
                    'type': 'visual similarity'
                })
    
    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)
    return results

# Example usage
product_catalog = [
    "Python Programming",
    "Java Development",
    "JavaScript Essentials",
    "Machine Learning Basics",
    "Data Science Fundamentals"
]

# Search with typing errors
queries = ["Pyton", "Javascrip", "Machien Lerning"]

for query in queries:
    print(f"\nSearch: '{query}'")
    results = intelligent_search(query, product_catalog)
    
    if results:
        print("  Results found:")
        for r in results[:3]:  # Top 3
            print(f"    - {r['item']}: {r['score']:.2%} ({r['type']})")
    else:
        print("  No results found")
```

---

### 5. Document Comparison

**Problem:** Determine if two descriptions or texts are similar using token comparison.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def compare_texts(text1, text2):
    """
    Compare two texts using Sorensen-Dice and Jaccard.
    """
    # Sorensen-Dice (better for short texts)
    dice = calculate_similarity(text1, text2, algorithm='sorensen_dice')
    
    # Jaccard (good for word sets)
    jaccard = calculate_similarity(text1, text2, algorithm='jaccard')
    
    return {
        'sorensen_dice': dice['score'],
        'jaccard': jaccard['score'],
        'average_similarity': (dice['score'] + jaccard['score']) / 2
    }

# Example: Compare product descriptions
desc1 = "High-performance gaming laptop with Intel Core i7 processor"
desc2 = "Gaming laptop with high performance and Intel i7 processor"
desc3 = "Tablet with touchscreen and long-lasting battery"

print("Description comparison:")
print("\nDesc1 vs Desc2 (similar):")
result = compare_texts(desc1, desc2)
for metric, value in result.items():
    print(f"  {metric}: {value:.2%}")

print("\nDesc1 vs Desc3 (different):")
result = compare_texts(desc1, desc3)
for metric, value in result.items():
    print(f"  {metric}: {value:.2%}")
```

**Output:**
```
Description comparison:

Desc1 vs Desc2 (similar):
  sorensen_dice: 68.42%
  jaccard: 52.00%
  average_similarity: 60.21%

Desc1 vs Desc3 (different):
  sorensen_dice: 9.09%
  jaccard: 4.76%
  average_similarity: 6.93%
```

---

### 6. Intelligent Autocomplete System

**Problem:** Implement an autocomplete system that suggests relevant options while the user types, even with spelling errors.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

class IntelligentAutocomplete:
    """Autocomplete system with error tolerance."""
    
    def __init__(self, vocabulary, min_chars=2):
        self.vocabulary = vocabulary
        self.min_chars = min_chars
    
    def suggest(self, partial_text, max_suggestions=5, threshold=0.60):
        """
        Generate suggestions based on partial input text.
        
        Args:
            partial_text: Text user has typed
            max_suggestions: Maximum number of suggestions to return
            threshold: Minimum similarity threshold (0.0 - 1.0)
        
        Returns:
            List of suggestions ordered by relevance
        """
        if len(partial_text) < self.min_chars:
            return []
        
        suggestions = []
        
        for word in self.vocabulary:
            # Check if it starts with text (exact prefix match)
            if word.lower().startswith(partial_text.lower()):
                suggestions.append({
                    'text': word,
                    'score': 1.0,  # Maximum priority for exact prefixes
                    'type': 'exact_prefix'
                })
            else:
                # Use Jaro-Winkler (favors matches at beginning)
                result = calculate_similarity(
                    partial_text,
                    word,
                    algorithm='jaro_winkler'
                )
                
                if result['score'] >= threshold:
                    suggestions.append({
                        'text': word,
                        'score': result['score'],
                        'type': 'fuzzy_similarity'
                    })
        
        # Sort by score descending
        suggestions.sort(key=lambda x: x['score'], reverse=True)
        
        return suggestions[:max_suggestions]

# Example usage: Product autocomplete
products = [
    "iPhone 15 Pro Max",
    "iPad Air",
    "iPad Pro",
    "MacBook Pro",
    "MacBook Air",
    "Apple Watch Series 9",
    "AirPods Pro",
    "AirPods Max",
    "Apple TV 4K",
    "iMac 24 inch"
]

autocomplete = IntelligentAutocomplete(products)

# Simulate user input
user_inputs = ["iPh", "Macbok", "Airp", "ipad", "Aple"]

print("Intelligent Autocomplete System")
print("=" * 60)

for input_text in user_inputs:
    suggestions = autocomplete.suggest(input_text, max_suggestions=3)
    
    print(f"\nUser types: '{input_text}'")
    if suggestions:
        print("  Suggestions:")
        for idx, sug in enumerate(suggestions, 1):
            type_icon = "⭐" if sug['type'] == 'exact_prefix' else "🔍"
            print(f"    {idx}. {type_icon} {sug['text']} ({sug['score']:.1%})")
    else:
        print("  No suggestions available")
```

**Output:**
```
Intelligent Autocomplete System
============================================================

User types: 'iPh'
  Suggestions:
    1. ⭐ iPhone 15 Pro Max (100.0%)

User types: 'Macbok'
  Suggestions:
    1. 🔍 MacBook Pro (92.9%)
    2. 🔍 MacBook Air (92.9%)

User types: 'Airp'
  Suggestions:
    1. ⭐ AirPods Pro (100.0%)
    2. ⭐ AirPods Max (100.0%)

User types: 'ipad'
  Suggestions:
    1. ⭐ iPad Air (100.0%)
    2. ⭐ iPad Pro (100.0%)

User types: 'Aple'
  Suggestions:
    1. 🔍 Apple Watch Series 9 (84.0%)
    2. 🔍 Apple TV 4K (80.0%)
```

---

### 7. Sentence Similarity Analysis

**Problem:** Compare complete sentences to detect plagiarism, duplicate content, or variations of the same idea.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity

def analyze_sentences(sentence1, sentence2):
    """
    Complete similarity analysis between two sentences using multiple metrics.
    """
    # Run all algorithms
    results = calculate_similarity(sentence1, sentence2, algorithm='all')
    
    # Calculate weighted composite score
    composite_score = (
        results['levenshtein_ratio'] * 0.30 +
        results['jaro_winkler_score'] * 0.30 +
        results['sorensen_dice_score'] * 0.20 +
        results['jaccard_score'] * 0.20
    )
    
    # Classify similarity level
    if composite_score >= 0.90:
        level = "Very High (Possible Duplicate)"
        color = "🔴"
    elif composite_score >= 0.75:
        level = "High (Similar Content)"
        color = "🟠"
    elif composite_score >= 0.50:
        level = "Medium (Some Similarity)"
        color = "🟡"
    else:
        level = "Low (Different Content)"
        color = "🟢"
    
    return {
        'composite_score': composite_score,
        'level': level,
        'color': color,
        'metrics': results
    }

# Test cases
cases = [
    {
        'sentence1': "Python is a versatile and powerful programming language",
        'sentence2': "Python is a versatile and potent programming language",
        'description': "Same sentence with small variations"
    },
    {
        'sentence1': "Artificial intelligence is revolutionizing technology",
        'sentence2': "AI is transforming the world of technology",
        'description': "Same idea, different wording"
    },
    {
        'sentence1': "Machine learning uses algorithms to learn from data",
        'sentence2': "Cats are very popular domestic animals",
        'description': "Completely different sentences"
    }
]

print("Sentence Similarity Analysis")
print("=" * 70)

for idx, case in enumerate(cases, 1):
    print(f"\n{idx}. {case['description']}")
    print(f"   Sentence A: \"{case['sentence1']}\"")
    print(f"   Sentence B: \"{case['sentence2']}\"")
    print()
    
    analysis = analyze_sentences(case['sentence1'], case['sentence2'])
    
    print(f"   {analysis['color']} Similarity Level: {analysis['level']}")
    print(f"   Composite Score: {analysis['composite_score']:.1%}")
    print(f"   Detailed Metrics:")
    print(f"      - Levenshtein: {analysis['metrics']['levenshtein_ratio']:.1%}")
    print(f"      - Jaro-Winkler: {analysis['metrics']['jaro_winkler_score']:.1%}")
    print(f"      - Sorensen-Dice: {analysis['metrics']['sorensen_dice_score']:.1%}")
    print(f"      - Jaccard: {analysis['metrics']['jaccard_score']:.1%}")
    print(f"      - Metaphone Match: {analysis['metrics']['metaphone_match']}")
```

---

### 8. Multi-Algorithm Fuzzy Search

**Problem:** Implement a search engine that combines multiple algorithms to maximize precision and recall.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity
from typing import List, Dict

class MultiAlgorithmSearch:
    """
    Advanced search engine that combines multiple similarity algorithms.
    """
    
    def __init__(self, catalog: List[str]):
        self.catalog = catalog
    
    def search(
        self,
        query: str,
        algorithms: List[str] = None,
        threshold: float = 0.70,
        top_n: int = 5
    ) -> List[Dict]:
        """
        Search catalog using multiple algorithms.
        
        Args:
            query: Search text
            algorithms: List of algorithms to use (None = all)
            threshold: Minimum similarity threshold
            top_n: Number of results to return
        
        Returns:
            List of results with scores from each algorithm
        """
        if algorithms is None:
            algorithms = ['levenshtein', 'jaro_winkler', 'metaphone', 'sorensen_dice']
        
        results_by_item = {}
        
        for item in self.catalog:
            scores = {}
            
            for algorithm in algorithms:
                result = calculate_similarity(query, item, algorithm=algorithm)
                
                # Normalize result (some return dict, others float/bool)
                if isinstance(result, dict):
                    score = result.get('score', result.get('ratio', 0))
                elif isinstance(result, bool):
                    score = 1.0 if result else 0.0
                else:
                    score = result
                
                scores[algorithm] = score
            
            # Calculate weighted average score
            final_score = sum(scores.values()) / len(scores)
            
            if final_score >= threshold:
                results_by_item[item] = {
                    'item': item,
                    'final_score': final_score,
                    'individual_scores': scores,
                    'matching_algorithms': sum(1 for s in scores.values() if s >= threshold)
                }
        
        # Sort by final score
        results = sorted(
            results_by_item.values(),
            key=lambda x: (x['final_score'], x['matching_algorithms']),
            reverse=True
        )
        
        return results[:top_n]

# Example usage: Search in knowledge base
knowledge_base = [
    "How to install Python on Windows",
    "Python programming tutorial",
    "Python quick start guide",
    "Python for beginners step by step",
    "Setting up Python development environment",
    "Installing Python libraries with pip",
    "JavaScript: basic concepts for beginners",
    "Introduction to Machine Learning with Python",
    "Data analysis with pandas in Python"
]

searcher = MultiAlgorithmSearch(knowledge_base)

# Searches with errors and variations
queries = [
    "how to install pyton",   # Spelling error
    "tutorial pythn",         # Incomplete word
    "python to start",        # Wording variation
]

print("Multi-Algorithm Search in Knowledge Base")
print("=" * 70)

for query in queries:
    print(f"\n🔍 Search: '{query}'")
    print("-" * 70)
    
    results = searcher.search(query, threshold=0.50, top_n=3)
    
    if results:
        for idx, res in enumerate(results, 1):
            print(f"\n{idx}. {res['item']}")
            print(f"   Final Score: {res['final_score']:.1%}")
            print(f"   Matching algorithms: {res['matching_algorithms']}/4")
            print(f"   Individual scores:")
            for alg, score in res['individual_scores'].items():
                bar = "█" * int(score * 20)
                print(f"      {alg:15} {score:.1%} {bar}")
    else:
        print("   No results found")
```

---

### 9. Algorithm Comparison Tool

**Problem:** You need to decide which similarity algorithm is best for your specific use case.

**Solution:**

```python
from shortfx.fxString.string_similarity import calculate_similarity
import time

class AlgorithmComparator:
    """
    Tool to evaluate and compare different similarity algorithms.
    """
    
    AVAILABLE_ALGORITHMS = [
        'levenshtein', 'jaro_winkler', 'metaphone', 'hamming',
        'sorensen_dice', 'jaccard', 'mra', 'lcs', 'ratcliff_obershelp'
    ]
    
    def compare(self, word1: str, word2: str, show_time: bool = True):
        """
        Compare two words using all available algorithms.
        
        Args:
            word1: First word to compare
            word2: Second word to compare
            show_time: Whether to show execution time
        
        Returns:
            Dict with results from each algorithm
        """
        results = {}
        
        for algorithm in self.AVAILABLE_ALGORITHMS:
            try:
                # Measure time if enabled
                if show_time:
                    start = time.perf_counter()
                
                result = calculate_similarity(word1, word2, algorithm=algorithm)
                
                if show_time:
                    time_ms = (time.perf_counter() - start) * 1000
                else:
                    time_ms = None
                
                # Normalize result
                if isinstance(result, dict):
                    score = result.get('score', result.get('ratio', 0))
                elif isinstance(result, bool):
                    score = 1.0 if result else 0.0
                else:
                    score = result
                
                results[algorithm] = {
                    'score': score,
                    'time_ms': time_ms,
                    'complete_result': result
                }
                
            except Exception as e:
                results[algorithm] = {
                    'score': None,
                    'time_ms': None,
                    'error': str(e)
                }
        
        return results
    
    def show_report(self, word1: str, word2: str):
        """Generate a visual comparison report."""
        print(f"\n{'=' * 80}")
        print(f"ALGORITHM COMPARISON")
        print(f"{'=' * 80}")
        print(f"Word 1: '{word1}'")
        print(f"Word 2: '{word2}'")
        print(f"{'-' * 80}")
        
        results = self.compare(word1, word2)
        
        # Sort by score descending
        sorted_results = sorted(
            results.items(),
            key=lambda x: x[1]['score'] if x[1]['score'] is not None else -1,
            reverse=True
        )
        
        print(f"\n{'Algorithm':<20} {'Score':<12} {'Time (ms)':<15} {'Visual Bar'}")
        print(f"{'-' * 80}")
        
        for algorithm, data in sorted_results:
            if data['score'] is not None:
                score_str = f"{data['score']:.2%}"
                time_str = f"{data['time_ms']:.3f}" if data['time_ms'] else "N/A"
                bar = "█" * int(data['score'] * 30)
                
                print(f"{algorithm:<20} {score_str:<12} {time_str:<15} {bar}")
            else:
                print(f"{algorithm:<20} {'ERROR':<12} {'N/A':<15} {data.get('error', 'N/A')}")
        
        # Recommendation
        best = sorted_results[0]
        print(f"\n{'=' * 80}")
        print(f"✓ Best result: {best[0]} with {best[1]['score']:.2%}")
        print(f"{'=' * 80}")

# Example usage
comparator = AlgorithmComparator()

# Case 1: Names with spelling variation
print("\n📊 CASE 1: Names with spelling variation")
comparator.show_report("Martínez", "Martinez")

# Case 2: Words with typing error
print("\n📊 CASE 2: Words with typing error")
comparator.show_report("Python", "Pyton")

# Case 3: Phonetically similar words
print("\n📊 CASE 3: Phonetically similar words")
comparator.show_report("Catherine", "Katherine")

# Case 4: Short phrases
print("\n📊 CASE 4: Short phrases")
comparator.show_report("machine learning", "machine lerning")
```

---

## Spellcheck

### 1. Proper Name Correction

**Problem:** Correct typing errors in person names from a registration form.

**Solution:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# List of valid names in the company
valid_names = [
    "Juan", "María", "José", "Ana", "Carlos", "Laura",
    "Pedro", "Carmen", "Miguel", "Isabel", "Antonio", "Rosa"
]

# Create corrector with custom vocabulary
corrector = UniversalSpellChecker(language="es", custom_vocabulary=valid_names)

# Names with typing errors
names_with_errors = ["Juaan", "Mria", "Crlos", "Lara", "Pedr", "Migeul"]

print("Proper name correction:")
for wrong_name in names_with_errors:
    corrected_name = corrector.correct(wrong_name)
    
    if wrong_name != corrected_name:
        print(f"  '{wrong_name}' → '{corrected_name}' ✓")
    else:
        print(f"  '{wrong_name}' → No correction found")
```

**Output:**
```
Proper name correction:
  'Juaan' → 'Juan' ✓
  'Mria' → 'María' ✓
  'Crlos' → 'Carlos' ✓
  'Lara' → 'Laura' ✓
  'Pedr' → 'Pedro' ✓
  'Migeul' → 'Miguel' ✓
```

---

### 2. User Input Normalization

**Problem:** Users enter city names with spelling errors in a shipping system.

**Solution:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Major cities in Spain
spanish_cities = [
    "Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza",
    "Málaga", "Murcia", "Palma", "Bilbao", "Alicante",
    "Córdoba", "Valladolid", "Vigo", "Gijón", "Granada"
]

city_corrector = UniversalSpellChecker(
    language="es",
    custom_vocabulary=spanish_cities
)

# User inputs with errors
user_inputs = [
    "Madrd",      # Missing 'i'
    "Barselona",  # 's' instead of 'c'
    "Sevila",     # Missing double 'l'
    "Malaga",     # Without accent
    "Bilbao",     # Correct
    "Cordoba"     # Without accent
]

print("City correction:")
print("-" * 40)
for input_text in user_inputs:
    correction = city_corrector.correct(input_text)
    
    if input_text == correction:
        print(f"✓ '{input_text}' → Already correct")
    else:
        print(f"✎ '{input_text}' → '{correction}'")
```

**Output:**
```
City correction:
----------------------------------------
✎ 'Madrd' → 'Madrid'
✎ 'Barselona' → 'Barcelona'
✎ 'Sevila' → 'Sevilla'
✎ 'Malaga' → 'Málaga'
✓ 'Bilbao' → Already correct
✎ 'Cordoba' → 'Córdoba'
```

---

### 3. Form Data Cleaning

**Problem:** Process and correct multiple fields of a contact form.

**Solution:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Vocabulary of common first and last names
complete_vocabulary = [
    # First names
    "Juan", "María", "José", "Ana", "Carlos", "Laura", "Pedro", "Carmen",
    # Last names
    "García", "Rodríguez", "Martínez", "López", "González", "Fernández",
    "Sánchez", "Pérez", "Martín", "Gómez"
]

corrector = UniversalSpellChecker(language="es", custom_vocabulary=complete_vocabulary)

# Form data with errors
form = {
    "nombre": "Jse",
    "apellido1": "Garsia",
    "apellido2": "Rodrguez",
    "email": "jose.garcia@example.com"
}

# Correct fields
corrected_form = {}
text_fields = ["nombre", "apellido1", "apellido2"]

for field in text_fields:
    original_value = form[field]
    corrected_value = corrector.correct(original_value)
    corrected_form[field] = corrected_value

# Keep email unchanged
corrected_form["email"] = form["email"]

# Display results
print("Form correction:")
print("\nBefore:")
for field, value in form.items():
    print(f"  {field}: {value}")

print("\nAfter:")
for field, value in corrected_form.items():
    print(f"  {field}: {value}")

# Summary of changes
print("\nChanges made:")
for field in text_fields:
    if form[field] != corrected_form[field]:
        print(f"  {field}: '{form[field]}' → '{corrected_form[field]}'")
```

**Output:**
```
Form correction:

Before:
  nombre: Jse
  apellido1: Garsia
  apellido2: Rodrguez
  email: jose.garcia@example.com

After:
  nombre: José
  apellido1: García
  apellido2: Rodríguez
  email: jose.garcia@example.com

Changes made:
  nombre: 'Jse' → 'José'
  apellido1: 'Garsia' → 'García'
  apellido2: 'Rodrguez' → 'Rodríguez'
```

---

### 4. Custom Dictionary Correction

**Problem:** Correct technical or domain-specific terms (e.g., company departments).

**Solution:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Company departments
departments = [
    "Sales", "Marketing", "Human Resources", "Accounting",
    "Technology", "Operations", "Logistics", "Customer Service"
]

dept_corrector = UniversalSpellChecker(
    language="en",
    custom_vocabulary=departments
)

# Employee inputs with errors
assignments = [
    {"employee": "Ana López", "dept_input": "Sales"},
    {"employee": "Carlos Ruiz", "dept_input": "Markeeting"},
    {"employee": "Laura Díaz", "dept_input": "Hman Resources"},
    {"employee": "Pedro Sanz", "dept_input": "Technlogy"},
    {"employee": "María Gil", "dept_input": "Logistiks"}
]

print("Department correction:")
print("=" * 60)

for assignment in assignments:
    dept_original = assignment["dept_input"]
    dept_corrected = dept_corrector.correct(dept_original)
    
    print(f"\nEmployee: {assignment['employee']}")
    print(f"  Input: '{dept_original}'")
    
    if dept_original != dept_corrected:
        print(f"  Corrected to: '{dept_corrected}' ✓")
    else:
        print(f"  Status: Correct ✓")
```

**Output:**
```
Department correction:
============================================================

Employee: Ana López
  Input: 'Sales'
  Status: Correct ✓

Employee: Carlos Ruiz
  Input: 'Markeeting'
  Corrected to: 'Marketing' ✓

Employee: Laura Díaz
  Input: 'Hman Resources'
  Corrected to: 'Human Resources' ✓

Employee: Pedro Sanz
  Input: 'Technlogy'
  Corrected to: 'Technology' ✓

Employee: María Gil
  Input: 'Logistiks'
  Corrected to: 'Logistics' ✓
```

---

### 5. Real-Time Input Validation

**Problem:** Validate and correct user input in real-time while typing in a web form or application.

**Solution:**

```python
from shortfx.fxString.string_spellcheck import UniversalSpellChecker
from shortfx.fxString.string_similarity import calculate_similarity

class RealTimeValidator:
    """
    Validator that corrects and suggests while user types.
    """
    
    def __init__(self, valid_vocabulary, language="es"):
        self.corrector = UniversalSpellChecker(
            language=language,
            custom_vocabulary=valid_vocabulary
        )
        self.vocabulary = valid_vocabulary
    
    def validate_field(self, value: str, min_similarity: float = 0.85):
        """
        Validate a field and suggest corrections.
        
        Args:
            value: Text entered by user
            min_similarity: Minimum threshold to accept value
        
        Returns:
            Dict with validation status and suggestions
        """
        # Correct the value
        corrected_value = self.corrector.correct(value)
        
        # Check if it's in valid vocabulary
        is_valid = corrected_value in self.vocabulary
        
        # If not valid, look for close matches
        suggestions = []
        if not is_valid:
            for valid_word in self.vocabulary:
                score = calculate_similarity(
                    corrected_value,
                    valid_word,
                    algorithm='jaro_winkler'
                )['score']
                
                if score >= min_similarity:
                    suggestions.append({
                        'text': valid_word,
                        'score': score
                    })
            
            # Sort suggestions by score
            suggestions.sort(key=lambda x: x['score'], reverse=True)
        
        return {
            'original_value': value,
            'corrected_value': corrected_value,
            'is_valid': is_valid,
            'has_corrections': value != corrected_value,
            'suggestions': suggestions[:3]  # Top 3
        }

# Example usage: Country validation
valid_countries = [
    "Spain", "France", "Germany", "Italy", "Portugal",
    "United Kingdom", "Netherlands", "Belgium", "Switzerland", "Austria"
]

validator = RealTimeValidator(valid_countries, language="en")

# Simulate user input in real-time
simulated_inputs = [
    ("Spa", "User typing..."),
    ("Spian", "Keyboard error"),
    ("Spain", "Correct"),
    ("Frnce", "Missing letter"),
    ("Germny", "Spelling error"),
]

print("Real-Time Validation")
print("=" * 70)

for input_text, description in simulated_inputs:
    result = validator.validate_field(input_text)
    
    print(f"\n📝 '{input_text}' ({description})")
    
    if result['is_valid']:
        print(f"   ✅ VALID")
        if result['has_corrections']:
            print(f"   Auto-corrected: '{result['corrected_value']}'")
    else:
        print(f"   ⚠️  NEEDS CORRECTION")
        if result['has_corrections']:
            print(f"   Auto-correction: '{result['corrected_value']}'")
        
        if result['suggestions']:
            print(f"   Suggestions:")
            for idx, sug in enumerate(result['suggestions'], 1):
                print(f"      {idx}. {sug['text']} ({sug['score']:.1%})")
```

---

## Combined Use Cases

### Case 1: Resume Matching System

Combines word similarity and spell checking to match candidate skills with job requirements.

```python
from shortfx.fxString.string_similarity import calculate_similarity
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Required skills for position
required_skills = [
    "Python", "JavaScript", "SQL", "Docker", "Kubernetes",
    "React", "Node.js", "MongoDB", "AWS", "Git"
]

# Create corrector with technical vocabulary
tech_corrector = UniversalSpellChecker(
    language="en",
    custom_vocabulary=required_skills
)

# Candidate skills (with possible errors)
candidate_skills = [
    "Pyhton",      # Typo
    "Javascrip",   # Incomplete
    "SQL",         # Correct
    "Dokcer",      # Typo
    "React",       # Correct
    "Nodejs",      # Different format
    "PostgreSQL"   # Similar to SQL but different
]

print("Candidate Skills Analysis:")
print("=" * 60)

matches = []
for skill in candidate_skills:
    # First correct spelling
    corrected_skill = tech_corrector.correct(skill)
    
    # Look for best match in requirements
    best_match = None
    best_score = 0
    
    for required in required_skills:
        score = calculate_similarity(
            corrected_skill,
            required,
            algorithm='jaro_winkler'
        )['score']
        
        if score > best_score:
            best_score = score
            best_match = required
    
    # Determine if there's a match
    is_match = best_score >= 0.85
    
    result = {
        'original': skill,
        'corrected': corrected_skill,
        'match': best_match if is_match else None,
        'score': best_score,
        'is_match': is_match
    }
    
    matches.append(result)
    
    # Show result
    print(f"\nSkill: '{skill}'")
    if skill != corrected_skill:
        print(f"  Correction: '{corrected_skill}'")
    
    if is_match:
        print(f"  ✓ Match with: '{best_match}' ({best_score:.1%})")
    else:
        print(f"  ✗ No match (best: '{best_match}' {best_score:.1%})")

# Summary
total_matches = sum(1 for m in matches if m['is_match'])
print(f"\n{'=' * 60}")
print(f"Summary: {total_matches}/{len(candidate_skills)} matching skills")
print(f"Match percentage: {(total_matches/len(candidate_skills))*100:.1f}%")
```

---

### Case 2: Contact Deduplication and Cleaning

Identifies and merges duplicate contacts with name variations and error correction.

```python
from shortfx.fxString.string_similarity import calculate_similarity
from shortfx.fxString.string_spellcheck import UniversalSpellChecker

# Contact database with potential duplicates
contacts = [
    {"id": 1, "name": "Juan García", "email": "juan.garcia@email.com"},
    {"id": 2, "name": "Jua Garcia", "email": "j.garcia@email.com"},  # Duplicate with error
    {"id": 3, "name": "María López", "email": "maria.lopez@email.com"},
    {"id": 4, "name": "Maria Lopes", "email": "m.lopez@email.com"},  # Duplicate without accent
    {"id": 5, "name": "Carlos Ruiz", "email": "carlos.ruiz@email.com"}
]

# Common names for correction
common_names = ["Juan", "María", "Carlos", "García", "López", "Ruiz"]
corrector = UniversalSpellChecker(language="es", custom_vocabulary=common_names)

def normalize_contact(contact):
    """Normalize contact name by correcting errors."""
    words = contact["name"].split()
    corrected_words = [corrector.correct(w) for w in words]
    return " ".join(corrected_words)

# Detect duplicates
print("Duplicate Analysis:")
print("=" * 70)

duplicates = []
processed = set()

for i, contact1 in enumerate(contacts):
    if i in processed:
        continue
    
    name1_norm = normalize_contact(contact1)
    group = [contact1]
    
    for j, contact2 in enumerate(contacts[i+1:], start=i+1):
        if j in processed:
            continue
        
        name2_norm = normalize_contact(contact2)
        
        # Compare normalized names
        is_same, metrics = calculate_similarity(
            name1_norm,
            name2_norm,
            algorithm='effective_same',
            levenshtein_threshold=0.80
        )
        
        if is_same:
            group.append(contact2)
            processed.add(j)
    
    if len(group) > 1:
        duplicates.append(group)

# Show results
for idx, group in enumerate(duplicates, 1):
    print(f"\nGroup {idx} - Duplicates detected:")
    for contact in group:
        name_norm = normalize_contact(contact)
        print(f"  ID {contact['id']}: '{contact['name']}' → '{name_norm}'")
        print(f"           Email: {contact['email']}")
    
    # Suggest merge
    main_contact = group[0]
    final_name = normalize_contact(main_contact)
    print(f"  → Suggestion: Keep ID {main_contact['id']} as '{final_name}'")

print(f"\n{'=' * 70}")
print(f"Total duplicate groups found: {len(duplicates)}")
```

---

### Case 3: Massive Name Deduplication

Complete system for deduplication with intelligent normalization.

```python
from shortfx.fxString.string_similarity import calculate_similarity
from shortfx.fxString.string_spellcheck import UniversalSpellChecker
from collections import defaultdict

class NameDeduplicator:
    """
    Advanced name deduplication system with intelligent normalization.
    """
    
    def __init__(self, name_vocabulary=None):
        self.vocabulary = name_vocabulary or []
        if self.vocabulary:
            self.corrector = UniversalSpellChecker(
                language="es",
                custom_vocabulary=self.vocabulary
            )
        else:
            self.corrector = None
    
    def normalize_name(self, name: str) -> str:
        """Normalize a name applying rules and correction."""
        # Remove extra spaces
        name = " ".join(name.split())
        
        # Capitalize each word
        words = name.split()
        
        # Correct if vocabulary available
        if self.corrector:
            words = [self.corrector.correct(w) for w in words]
        
        # Capitalize
        return " ".join(p.title() for p in words)
    
    def are_duplicates(self, name1: str, name2: str, threshold: float = 0.85) -> bool:
        """Determine if two names are duplicates."""
        # Normalize both names
        norm1 = self.normalize_name(name1)
        norm2 = self.normalize_name(name2)
        
        # Compare using effective_same
        is_same, _ = calculate_similarity(
            norm1,
            norm2,
            algorithm='effective_same',
            levenshtein_threshold=threshold,
            metaphone_required=False
        )
        
        return is_same
    
    def deduplicate(self, name_list: list, threshold: float = 0.85):
        """
        Deduplicate a name list by grouping variants.
        
        Returns:
            Dict with canonical names and their variants
        """
        # Group duplicate names
        groups = []
        processed = set()
        
        for i, name1 in enumerate(name_list):
            if i in processed:
                continue
            
            group = {
                'canonical': self.normalize_name(name1),
                'variants': [name1],
                'indices': [i]
            }
            
            for j, name2 in enumerate(name_list[i+1:], start=i+1):
                if j in processed:
                    continue
                
                if self.are_duplicates(name1, name2, threshold):
                    group['variants'].append(name2)
                    group['indices'].append(j)
                    processed.add(j)
            
            groups.append(group)
        
        return groups

# Example usage: Employee list deduplication
employees_raw = [
    "Juan García López",
    "Jua Garcia Lopez",      # Error + without accents
    "juan garcia lopez",     # Lowercase
    "María Fernández",
    "Maria Fernandez",       # Without accent
    "Mria Fernandez",        # Typo
    "Carlos Ruiz Sánchez",
    "Carlos Ruiz Sanchez",   # Without accent
    "Pedro Martínez",
    "Ana López García",
    "Ana Lopez Garcia",      # Without accent
    "Pedro Martinez",        # Without accent
    "Laura González",
    "laura gonzalez"         # Lowercase + without accent
]

# Vocabulary of common Spanish names and surnames
spanish_vocabulary = [
    "Juan", "María", "José", "Ana", "Carlos", "Laura", "Pedro",
    "García", "López", "Fernández", "Martínez", "González", "Ruiz", "Sánchez"
]

deduplicator = NameDeduplicator(spanish_vocabulary)

print("Massive Name Deduplication")
print("=" * 80)
print(f"\nTotal original records: {len(employees_raw)}")

# Run deduplication
groups = deduplicator.deduplicate(employees_raw, threshold=0.85)

# Filter only groups with duplicates
duplicate_groups = [g for g in groups if len(g['variants']) > 1]
unique_names = [g for g in groups if len(g['variants']) == 1]

print(f"Unique names (no duplicates): {len(unique_names)}")
print(f"Groups with duplicates: {len(duplicate_groups)}")
print(f"Total names after deduplication: {len(groups)}")

# Show duplicate groups
if duplicate_groups:
    print(f"\n{'=' * 80}")
    print("DUPLICATE GROUPS DETECTED")
    print(f"{'=' * 80}")
    
    for idx, group in enumerate(duplicate_groups, 1):
        print(f"\nGroup {idx}:")
        print(f"  Canonical name: {group['canonical']}")
        print(f"  Variants found ({len(group['variants'])}):")
        for variant in group['variants']:
            print(f"    - '{variant}'")

# Generate consolidated list
print(f"\n{'=' * 80}")
print("CONSOLIDATED LIST (without duplicates)")
print(f"{'=' * 80}")

for idx, group in enumerate(groups, 1):
    print(f"{idx:2d}. {group['canonical']:30} ({len(group['variants'])} record(s))")

# Final statistics
total_variants = sum(len(g['variants']) for g in groups)
deduplication_rate = (1 - len(groups) / total_variants) * 100

print(f"\n{'=' * 80}")
print("STATISTICS")
print(f"{'=' * 80}")
print(f"Original records:      {total_variants}")
print(f"Unique records:        {len(groups)}")
print(f"Duplicates removed:    {total_variants - len(groups)}")
print(f"Deduplication rate:    {deduplication_rate:.1f}%")
```

---

## 📌 Best Practices

### For Word Similarity

1. **Choose the right algorithm:**
   - `metaphone`: Fast phonetic comparison (names, spoken words)
   - `levenshtein`: General edit distance (error detection)
   - `jaro_winkler`: Proper names (prioritizes word beginning)
   - `sorensen_dice` / `jaccard`: Texts and documents
   - `effective_same`: Robust combined validation

2. **Adjust thresholds according to context:**
   - Proper names: 0.85 - 0.90
   - Tolerant search: 0.70 - 0.80
   - Strict detection: 0.90 - 0.95

3. **Optimize performance:**
   - Use `metaphone` as initial filter for large datasets
   - Apply more expensive algorithms only to pre-selected candidates

### For Spellcheck

1. **Custom vocabularies:**
   - Always provide a domain-specific vocabulary
   - Include common variations (with/without accents, singular/plural)

2. **Result validation:**
   - Verify correction makes sense in context
   - Maintain a correction log to review patterns

3. **Handling special cases:**
   - Proper names: preserve original capitalization
   - Acronyms and initialisms: add them to custom vocabulary
   - Technical terms: use specific dictionaries

---

## 🎯 Conclusion

The **fxString** module in shortfx provides powerful and flexible tools for:

- 🔍 **Intelligent search** with error tolerance
- 🔄 **Duplicate detection** with high precision
- ✍️ **Automatic correction** of typing errors
- 📊 **Similarity analysis** with multiple algorithms
- 🎯 **Robust validation** of input data

These use cases demonstrate how to apply these functions in real-world business and application development scenarios.
