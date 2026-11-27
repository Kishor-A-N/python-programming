# Python – Tuples and Sets

# 1. Tuples

## Introduction to Tuples

A tuple is a collection of elements stored in a single variable.

- Tuples are ordered.
- Tuples are immutable (cannot be modified).
- Tuples allow duplicate values.
- Tuples can store different data types.
- Tuples are created using parentheses `()`.

### Syntax

```python
a = (1, 2, 4, 6)
print(a)
```

**Output:**
```text
(1, 2, 4, 6)
```

## 2. Creating a Tuple with One Element

To create a tuple with a single element, we must use a comma.

### Example

```python
a = (1,)
print(a)
```

**Output:**
```text
(1,)
```

**Note:** `(1)` is an integer, but `(1,)` is a tuple.

## 3. Accessing Tuple Elements (Indexing)

We can access tuple elements using their index numbers.

- Positive indexing starts from 0.
- Negative indexing starts from -1.

### Example

```python
a = (1, 2, 4, 6)

print(a[0])
print(a[2])
```

**Output:**
```text
1
4
```

## 4. Tuple Slicing

Slicing is used to access a particular range of elements.

### Syntax

```python
tuple_name[start:end]
```

### Example

```python
k = (2, 3, 1, 4, 6)

print(k[1:3])
```

**Output:**
```text
(3, 1)
```

Explanation:
- Starting index = 1
- Ending index = 3 (not included)

## 5. Tuple Concatenation

Concatenation means combining two tuples using the `+` operator.

### Example

```python
k1 = (2, 3, 1, 4, 6)
k2 = (3, 5, 7, 8, 1)

k3 = k1 + k2

print(k3)
```

**Output:**
```text
(2, 3, 1, 4, 6, 3, 5, 7, 8, 1)
```

---

# 6. Sets

## Introduction to Sets

A set is a collection of unique elements.

- Sets are unordered.
- Sets do not allow duplicate elements.
- Sets are mutable.
- Sets are created using curly brackets `{}`.
- Sets do not support indexing or slicing.

### Example

```python
s = {1, 3, 42, 4, 2, 6, 7, 4, 8, 0}

print(s)
```

**Output:**
```text
{0, 1, 2, 3, 4, 6, 7, 8, 42}
```

**Note:** Duplicate values are automatically removed. Set output order is not guaranteed.

## 7. Creating an Empty Set

To create an empty set, use `set()`.

### Example

```python
a = set()
print(a)
```

**Output:**
```text
set()
```

**Important:**
- `{}` creates an empty dictionary.
- `set()` creates an empty set.

---

# 8. Set Operations

Set operations are used to compare and combine two sets.

Consider:

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
```

## A. Union ( | )

Union combines all unique elements from both sets.

### Example

```python
print(s1 | s2)
```

**Output:**
```text
{1, 2, 3, 4, 5}
```

## B. Intersection ( & )

Intersection returns the common elements present in both sets.

### Example

```python
print(s1 & s2)
```

**Output:**
```text
{3}
```

## C. Difference ( - )

Difference returns elements present in the first set but not in the second set.

### Example

```python
print(s1 - s2)
```

**Output:**
```text
{1, 2}
```

## D. Symmetric Difference ( ^ )

Symmetric difference returns elements that are present in either set but not in both.

### Example

```python
print(s1 ^ s2)
```

**Output:**
```text
{1, 2, 4, 5}
```

---

# 9. Set Operations Using Strings

We can also perform set operations using string elements.

### Example

```python
fruits = {"banana", "apple", "orange", "pineapple"}

fruits2 = {"pomegranate", "apple", "watermelon", "orange", "dragon fruit"}

print(fruits | fruits2)
print(fruits & fruits2)
print(fruits - fruits2)
print(fruits ^ fruits2)
```

**Explanation:**

1. `fruits | fruits2` – Combines all unique fruits.
2. `fruits & fruits2` – Displays common fruits.
3. `fruits - fruits2` – Displays fruits only in the first set.
4. `fruits ^ fruits2` – Displays fruits that are not common.

---

# 10. Adding Elements to a Set

## add() Method

The `add()` method is used to add a single element to a set.

### Syntax

```python
set_name.add(element)
```

### Example

```python
fruits = {"banana", "apple", "orange"}

fruits.add("kiwi")

print(fruits)
```

**Output:**
```text
{'banana', 'apple', 'orange', 'kiwi'}
```

**Note:** Adding an element that already exists does not create a duplicate.

---

# 11. Difference Between Tuple and Set

| Tuple | Set |
|---|---|
| Uses `()` | Uses `{}` |
| Ordered | Unordered |
| Immutable | Mutable |
| Allows duplicates | Does not allow duplicates |
| Supports indexing | Does not support indexing |
| Supports slicing | Does not support slicing |

---

# 12. Quick Revision

| Concept | Operator / Syntax | Description |
|---|---|---|
| Tuple creation | `()` | Creates a tuple |
| Single-element tuple | `(1,)` | Creates a tuple with one element |
| Tuple indexing | `a[0]` | Accesses an element |
| Tuple slicing | `a[1:3]` | Accesses a range |
| Tuple concatenation | `a + b` | Combines two tuples |
| Set creation | `{1, 2, 3}` | Creates a set |
| Empty set | `set()` | Creates an empty set |
| Union | `A \| B` | Combines unique elements |
| Intersection | `A & B` | Finds common elements |
| Difference | `A - B` | Finds elements in the first set only |
| Symmetric difference | `A ^ B` | Finds non-common elements |
| Add | `A.add(5)` | Adds an element |

---

# 13. Practice Questions

1. Create a tuple containing five numbers.
2. Create a tuple with only one element.
3. Access the second element of a tuple.
4. Perform slicing on a tuple.
5. Combine two tuples using `+`.
6. Create two sets containing numbers.
7. Find the union of two sets.
8. Find the intersection of two sets.
9. Find the difference between two sets.
10. Find the symmetric difference between two sets.
11. Add a new element to a set using `add()`.
12. Create a set with duplicate values and observe the output.

---

**Happy Coding! 🐍**
