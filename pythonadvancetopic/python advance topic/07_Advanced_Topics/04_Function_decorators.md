[Contents](../Contents.md) \| [Previous (7.3 Returning Functions)](03_Returning_functions.md) \| [Next (7.5 Decorated Methods)](05_Decorated_methods.md)

# 7.4 Function Decorators

This section introduces the concept of a decorator.  This is an advanced
topic for which we only scratch the surface.

### Logging Example

Consider a function.

```python
def add(x, y):
    return x + y
```

Now, consider the function with some logging added to it.

```python
def add(x, y):
    print('Calling add')
    return x + y
```

Now a second function also with some logging.

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```

### Observation

*Observation: It's kind of repetitive.*

Writing programs where there is a lot of code replication is often
really annoying.  They are tedious to write and hard to maintain.
Especially if you decide that you want to change how it works (i.e., a
different kind of logging perhaps).

### Code that makes logging

Perhaps you can make a function that makes functions with logging
added to them. A wrapper.

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Now use it.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

What happens when you call the function returned by `logged`?

```python
logged_add(3, 4)      # You see the logging message appear
```

This example illustrates the process of creating a so-called *wrapper function*.

A wrapper is a function that wraps around another function with some
extra bits of processing, but otherwise works in the exact same way
as the original function.

```python
>>> logged_add(3, 4)
Calling add   # Extra output. Added by the wrapper
7
>>>
```

*Note: The `logged()` function creates the wrapper and returns it as a result.*

## Decorators

Putting wrappers around functions is extremely common in Python.
So common, there is a special syntax for it.

```python
def add(x, y):
    return x + y
add = logged(add)

# Special syntax
@logged
def add(x, y):
    return x + y
```

The special syntax performs the same exact steps as shown above. A decorator is just new syntax.
It is said to *decorate* the function.

### Commentary

There are many more subtle details to decorators than what has been presented here.
For example, using them in classes. Or using multiple decorators with a function.
However, the previous example is a good illustration of how their use tends to arise.
Usually, it's in response to repetitive code appearing across a wide range of
function definitions.  A decorator can move that code to a central definition.
