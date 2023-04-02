
[Contents](../Contents.md) \| [Previous (6.4 Generator Expressions)](../06_Generators/04_More_generators.md) \| [Next (7.2 Anonymous Functions)](02_Anonymous_function.md)

# 7.1 Variable Arguments

This section covers variadic function arguments, sometimes described as
`*args` and `**kwargs`.

### Positional variable arguments (*args)

A function that accepts *any number* of arguments is said to use variable arguments.
For example:

```python
def f(x, *args):
    ...
```

Function call.

```python
f(1,2,3,4,5)
```

The extra arguments get passed as a tuple.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```

### Keyword variable arguments (**kwargs)

A function can also accept any number of keyword arguments.
For example:

```python
def f(x, y, **kwargs):
    ...
```

Function call.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

The extra keywords are passed in a dictionary.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
```

### Combining both

A function can also accept any number of variable keyword and non-keyword arguments.

```python
def f(*args, **kwargs):
    ...
```

Function call.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

The arguments are separated into positional and keyword components

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    ...
```

This function takes any combination of positional or keyword
arguments.  It is sometimes used when writing wrappers or when you
want to pass arguments through to another function.

### Passing Tuples and Dicts

Tuples can be expanded into variable arguments.

```python
numbers = (2,3,4)
f(1, *numbers)      # Same as f(1,2,3,4)
```

Dictionaries can also be expanded into keyword arguments.

```python
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# Same as f(data, color='red', delimiter=',', width=400)
```
