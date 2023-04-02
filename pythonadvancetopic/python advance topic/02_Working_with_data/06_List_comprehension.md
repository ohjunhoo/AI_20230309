[Contents](../Contents.md) \| [Previous (2.5 Collections)](05_Collections.md) \| [Next (2.7 Object Model)](07_Objects.md)

# 2.6 List Comprehensions

A common task is processing items in a list.  This section introduces list comprehensions,
a powerful tool for doing just that.

### Creating new lists

A list comprehension creates a new list by applying an operation to
each element of a sequence.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Another example:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

The general syntax is: `[ <expression> for <variable_name> in <sequence> ]`.

### Filtering

You can also filter during the list comprehension.

```python
>>> a = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0 ]
>>> b
[2, 8, 4, 20]
>>>
```

### Use cases

List comprehensions are hugely useful.  For example, you can collect values of a specific
dictionary fields:

```python
stocknames = [s['name'] for s in stocks]
```

You can perform database-like queries on sequences.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

You can also combine a list comprehension with a sequence reduction:

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```

### General Syntax

```code
[ <expression> for <variable_name> in <sequence> if <condition>]
```

What it means:

```python
result = []
for variable_name in sequence:
    if condition:
        result.append(expression)
```

### Historical Digression

List comprehensions come from math (set-builder notation).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

It is also implemented in several other languages. Most
coders probably aren't thinking about their math class though. So,
it's fine to view it as a cool list shortcut.
