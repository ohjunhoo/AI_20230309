[Contents](../Contents.md) \| [Previous (7.1 Variable Arguments)](01_Variable_arguments.md) \| [Next (7.3 Returning Functions)](03_Returning_functions.md)

# 7.2 Anonymous Functions and Lambda

### List Sorting Revisited

Lists can be sorted *in-place*. Using the `sort` method.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

You can sort in reverse order.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

It seems simple enough. However, how do we sort a list of dicts?

```python
[{'name': 'AA', 'price': 32.2, 'shares': 100},
{'name': 'IBM', 'price': 91.1, 'shares': 50},
{'name': 'CAT', 'price': 83.44, 'shares': 150},
{'name': 'MSFT', 'price': 51.23, 'shares': 200},
{'name': 'GE', 'price': 40.37, 'shares': 95},
{'name': 'MSFT', 'price': 65.1, 'shares': 50},
{'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

By what criteria?

You can guide the sorting by using a *key function*. The *key
function* is a function that receives the dictionary and returns the
value of interest for sorting.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

Here's the result.

```python
# Check how the dictionaries are sorted by the `name` key
[
  {'name': 'AA', 'price': 32.2, 'shares': 100},
  {'name': 'CAT', 'price': 83.44, 'shares': 150},
  {'name': 'GE', 'price': 40.37, 'shares': 95},
  {'name': 'IBM', 'price': 91.1, 'shares': 50},
  {'name': 'IBM', 'price': 70.44, 'shares': 100},
  {'name': 'MSFT', 'price': 51.23, 'shares': 200},
  {'name': 'MSFT', 'price': 65.1, 'shares': 50}
]
```

### Callback Functions

In the above example, the key function is an example of a callback
function. The `sort()` method "calls back" to a function you supply.
Callback functions are often short one-line functions that are only
used for that one operation.  Programmers often ask for a short-cut
for specifying this extra processing.

### Lambda: Anonymous Functions

Use a lambda instead of creating the function.  In our previous
sorting example.

```python
portfolio.sort(key=lambda s: s['name'])
```

This creates an *unnamed* function that evaluates a *single* expression.
The above code is much shorter than the initial code.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```

### Using lambda

* lambda is highly restricted.
* Only a single expression is allowed.
* No statements like `if`, `while`, etc.
* Most common use is with functions like `sort()`.
