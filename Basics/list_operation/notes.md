# Python List Operations

## 1. Creating a List

A list is a collection of elements stored in a single variable.

**Syntax:**
```python
list_name = [element1, element2, element3]
```

**Example:**
```python
items = ["pen", "book", "pencil", "note"]
print(items)
```

**Output:**
```text
['pen', 'book', 'pencil', 'note']
```

## 2. Updating List Elements

We can change an existing element using its index.

**Example:**
```python
items = ["pen", "book", "pencil", "note"]

items[0] = "bench"
print(items)
```

**Output:**
```text
['bench', 'book', 'pencil', 'note']
```

## 3. insert() Method

The `insert()` method adds an element at a specific position.

**Syntax:**
```python
list_name.insert(index, element)
```

**Example:**
```python
items = ["pen", "book", "pencil", "note"]

items.insert(2, "vix")
print(items)
```

**Output:**
```text
['pen', 'book', 'vix', 'pencil', 'note']
```

## 4. append() Method

The `append()` method adds an element at the end of the list.

**Example:**
```python
items = ["pen", "book", "pencil"]

items.append("max")
print(items)
```

**Output:**
```text
['pen', 'book', 'pencil', 'max']
```

## 5. List Slicing

List slicing is used to access a particular range of elements.

**Syntax:**
```python
list_name[start:end:step]
```

**Example:**
```python
items = ["pen", "book", "pencil", "note"]

print(items[0::2])
```

**Output:**
```text
['pen', 'pencil']
```

Here:
- `0` – Starting index.
- No end value – Continue until the end.
- `2` – Skip every alternate element.

## 6. sorted() Function

The `sorted()` function arranges list elements in ascending order.

**Example:**
```python
l = [1, 5, 2, 1, 2, 3, 4, 5, 6]

print(sorted(l))
```

**Output:**
```text
[1, 1, 2, 2, 3, 4, 5, 5, 6]
```

Note: `sorted()` returns a new sorted list. It does not modify the original list.

## 7. sum() Function

The `sum()` function calculates the total of all numerical elements in a list.

**Example:**
```python
l = [1, 5, 2, 1, 2, 3, 4, 5, 6]

print(sum(l))
```

**Output:**
```text
29
```

## 8. Nested Lists

A list inside another list is called a nested list.

**Example:**
```python
m = [[1, 2], [3, 4]]

print(m)
print(m[1][0])
```

**Output:**
```text
[[1, 2], [3, 4]]
3
```

Explanation:
- `m[1]` accesses the second list `[3, 4]`.
- `m[1][0]` accesses the first element of that list (`3`).

## 9. pop() Method

The `pop()` method removes an element from the list using its index.

**Syntax:**
```python
list_name.pop(index)
```

**Example:**
```python
l = ["book", "pen", "pencil", "mobile", "laptop"]

l.pop(2)
print(l)
```

**Output:**
```text
['book', 'pen', 'mobile', 'laptop']
```

Note: If no index is provided, `pop()` removes the last element.

## 10. sort() Method

The `sort()` method arranges the original list in ascending order.

**Example:**
```python
numb = [1, 8, 3, 4, 6, 2, 0, 3, 1, 3, 1]

numb.sort()
print(numb)
```

**Output:**
```text
[0, 1, 1, 1, 2, 3, 3, 3, 4, 6, 8]
```

## 11. sort(reverse=True)

The `sort(reverse=True)` method arranges elements in descending order.

**Example:**
```python
numb = [1, 8, 3, 4, 6, 2, 0]

numb.sort(reverse=True)
print(numb)
```

**Output:**
```text
[8, 6, 4, 3, 2, 1, 0]
```

## 12. reverse() Method

The `reverse()` method reverses the current order of elements in the list.

**Example:**
```python
numb = [1, 8, 3, 4, 6, 2, 0]

numb.reverse()
print(numb)
```

**Output:**
```text
[0, 2, 6, 4, 3, 8, 1]
```

Note: `reverse()` does not sort the elements. It simply reverses their existing order.

---

## 13. Quick Revision

| Operation | Description |
|---|---|
| `print(list)` | Displays the list |
| `list[index] = value` | Updates an element |
| `insert()` | Adds an element at a specific position |
| `append()` | Adds an element at the end |
| `list[start:end:step]` | Accesses elements using slicing |
| `sorted()` | Returns a new sorted list |
| `sum()` | Calculates the sum of elements |
| `pop()` | Removes an element using its index |
| `sort()` | Sorts the original list in ascending order |
| `sort(reverse=True)` | Sorts the original list in descending order |
| `reverse()` | Reverses the existing order |

**Remember:**
- `sorted()` returns a new list.
- `sort()` modifies the original list.
- `reverse()` reverses the existing order.
- `append()` adds at the end.
- `insert()` adds at a specified position.
- `pop()` removes an element.
- `sum()` calculates the total.
