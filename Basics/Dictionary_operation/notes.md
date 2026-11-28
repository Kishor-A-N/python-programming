# Python Dictionary

## 1. What is a Dictionary in Python?

A dictionary is a collection of data stored in **key-value pairs**.

- **Key:** Used to identify the data.
- **Value:** The data associated with the key.

### Syntax
```python
dictionary_name = {
    "key1": "value1",
    "key2": "value2"
}
```

### Example
```python
dates = {
    "a": "28-05-2006",
    "b": "09-10-2006"
}

print(dates)
```

**Output:**
```text
{'a': '28-05-2006', 'b': '09-10-2006'}
```

## 2. Accessing Dictionary Elements

We can access dictionary values using their keys.

### Example
```python
dates = {
    "a": "28-05-2006",
    "b": "09-10-2006"
}

print(dates["a"])
```

**Output:**
```text
28-05-2006
```

### Using get()

The `get()` method is used to access a value using its key.

If the key does not exist, we can display a default message.

```python
print(dates.get("c", "not found"))
```

**Output:**
```text
not found
```

## 3. Adding Elements to a Dictionary

We can add new key-value pairs using the assignment operator (`=`).

### Example
```python
dates = {
    "a": "28-05-2006",
    "b": "09-10-2006"
}

dates["d"] = "28-06-2006"

print(dates)
```

**Output:**
```text
{'a': '28-05-2006', 'b': '09-10-2006', 'd': '28-06-2006'}
```

## 4. Updating Dictionary Elements

We can update an existing value by using its key.

### Example
```python
dates = {
    "a": "28-05-2006",
    "b": "09-10-2006"
}

dates["a"] = "28-05-2005"

print(dates)
```

**Output:**
```text
{'a': '28-05-2005', 'b': '09-10-2006'}
```

## 5. Dictionary Methods

Python provides different methods to work with dictionaries.

### keys()

Returns all the keys in a dictionary.

```python
print(dates.keys())
```

### values()

Returns all the values in a dictionary.

```python
print(dates.values())
```

### get()

Returns the value associated with the specified key.

```python
print(dates.get("a"))
```

### del

Deletes a particular key-value pair.

```python
del dates["a"]
print(dates)
```

## 6. List of Dictionaries

We can store multiple dictionaries inside a list.

This is useful when we want to store information about multiple items or people.

### Example
```python
item1 = {
    "name": "milk",
    "weight": 1,
    "price": 49
}

item2 = {
    "name": "sugar",
    "weight": 3,
    "price": 90.8
}

item = [item1, item2]

print(item)
```

**Output:**
```text
[{'name': 'milk', 'weight': 1, 'price': 49},
 {'name': 'sugar', 'weight': 3, 'price': 90.8}]
```

### Accessing Values from a List of Dictionaries

```python
print(item1["name"])
print(item2["price"])
```

**Output:**
```text
milk
90.8
```

### Performing Calculations

We can perform mathematical operations using dictionary values.

```python
print(f"Total weight: {item1['weight'] + item2['weight']} kg")
```

**Output:**
```text
Total weight: 4 kg
```

## 7. Updating and Deleting Dictionary Elements

### Example
```python
cities = {
    "mysuru": "mysuru pak",
    "bengaluru": "coffee",
    "tumkuru": "chicken",
    "davanagere": "benne dose",
    "mangalore": "fish kabab"
}

# Adding an element
cities["dharwad"] = "peda"

# Updating an element
cities["bengaluru"] = "tea"

# Deleting an element
del cities["mangalore"]

print(cities)
```

### Displaying Keys and Values

```python
print(cities.keys())
print(cities.values())
```

## 8. Storing Friends' Information Using Dictionaries

We can store different information about people using dictionaries.

### Example
```python
friend1 = {
    "name": "hithes",
    "subject": "maths",
    "food": "uppitu"
}

friend2 = {
    "name": "chiru",
    "subject": "kannada",
    "food": "chicken"
}

friends = [friend1, friend2]

print(friends)
```

### Accessing Favourite Food

```python
print("Favourite food: " + friend1["food"])
```

**Output:**
```text
Favourite food: uppitu
```

### Using f-string

We can also use an f-string to display dictionary values.

```python
print(f"Favourite food: {friend1['food']}")
```

**Output:**
```text
Favourite food: uppitu
```

## 9. Important Dictionary Concepts

| Method / Operation | Description |
|---|---|
| `dict[key]` | Access a value |
| `get()` | Access a value safely |
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `del` | Deletes an element |
| `dict[key] = value` | Adds or updates an element |
| `len()` | Returns the number of elements |
| `clear()` | Removes all elements |

## 10. Important Points to Remember

1. Dictionaries store data in key-value pairs.
2. Dictionary keys must be unique.
3. Values can be of different data types.
4. Dictionaries are mutable, meaning we can modify them.
5. We can add, update and delete elements.
6. Dictionaries are written using curly brackets `{}`.
7. We can store dictionaries inside lists.
8. Dictionary values can be accessed using their keys.

## Conclusion

Python dictionaries are useful for storing and managing structured data.

They are commonly used in student records, employee details, product information, JSON data and many real-world applications.

**Topic Completed: Python Dictionary**
