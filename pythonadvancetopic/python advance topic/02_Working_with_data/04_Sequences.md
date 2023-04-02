[Contents](../Contents.md) \| [Previous (2.3 Formatting)](03_Formatting.md) \| [Next (2.5 Collections)](05_Collections.md)

# 2.4 Sequences

### Sequence Datatypes

Python has three *sequence* datatypes.

* String: `'Hello'`. A string is a sequence of characters.
* List: `[1, 4, 5]`.
* Tuple: `('GOOG', 100, 490.1)`.

All sequences are ordered, indexed by integers, and have a length.

```python
a = 'Hello'               # String
b = [1, 4, 5]             # List
c = ('GOOG', 100, 490.1)  # Tuple

# Indexed order
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Length of sequence
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Sequences can be replicated: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequences of the same type can be concatenated: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```

### Slicing

Slicing means to take a subsequence from a sequence.
The syntax is `s[start:end]`. Where `start` and `end` are the indexes of the subsequence you want.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

* Indices `start` and `end` must be integers.
* Slices do *not* include the end value. It is like a half-open interval from math.
* If indices are omitted, they default to the beginning or end of the list.

### Slice re-assignment

On lists, slices can be reassigned and deleted.

```python
# Reassignment
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]
```

*Note: The reassigned slice doesn't need to have the same length.*

```python
# Deletion
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

### Sequence Reductions

There are some common functions to reduce a sequence to a single value.

```python
>>> s = [1, 2, 3, 4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['Hello', 'World']
>>> max(t)
'World'
>>>
```

### Iteration over a sequence

The for-loop iterates over the elements in a sequence.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

On each iteration of the loop, you get a new item to work with.
This new value is placed into the iteration variable. In this example, the
iteration variable is `x`:

```python
for x in s:         # `x` is an iteration variable
    ...statements
```

On each iteration, the previous value of the iteration variable is overwritten (if any).
After the loop finishes, the variable retains the last value.

### break statement

You can use the `break` statement to break out of a loop early.

```python
for name in namelist:
    if name == 'Jake':
        break
    ...
    ...
statements
```

When the `break` statement executes, it exits the loop and moves
on the next `statements`.  The `break` statement only applies to the
inner-most loop. If this loop is within another loop, it will not
break the outer loop.

### continue statement

To skip one element and move to the next one, use the `continue` statement.

```python
for line in lines:
    if line == '\n':    # Skip blank lines
        continue
    # More statements
    ...
```

This is useful when the current item is not of interest or needs to be ignored in the processing.

### Looping over integers

If you need to count, use `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

The syntax is `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Notice how it counts in steps of 2, not 1.
```

* The ending value is never included. It mirrors the behavior of slices.
* `start` is optional. Default `0`.
* `step` is optional. Default `1`.
* `range()` computes values as needed. It does not actually store a large range of numbers.

### enumerate() function

The `enumerate` function adds an extra counter value to iteration.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

The general form is `enumerate(sequence [, start = 0])`. `start` is optional.
A good example of using `enumerate()` is tracking line numbers while reading a file:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...
```

In the end, `enumerate` is just a nice shortcut for:

```python
i = 0
for x in s:
    statements
    i += 1
```

Using `enumerate` is less typing and runs slightly faster.

### For and tuples

You can iterate with multiple iteration variables.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Loops with x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #            ...
```

When using multiple variables, each tuple is *unpacked* into a set of iteration variables.
The number of variables must match the number of items in each tuple.

### zip() function

The `zip` function takes multiple sequences and makes an iterator that combines them.

```python
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

To get the result you must iterate. You can use multiple variables to unpack the tuples as shown earlier.

```python
for column, value in pairs:
    ...
```

A common use of `zip` is to create key/value pairs for constructing dictionaries.

```python
d = dict(zip(columns, values))
```
