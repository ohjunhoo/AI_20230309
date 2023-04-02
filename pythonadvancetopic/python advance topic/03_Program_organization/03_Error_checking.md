[Contents](../Contents.md) \| [Previous (3.2 More on Functions)](02_More_functions.md) \| [Next (3.4 Modules)](04_Modules.md)

# 3.3 Error Checking

Although exceptions were introduced earlier, this section fills in some additional
details about error checking and exception handling.

### How programs fail

Python performs no checking or validation of function argument types
or values.  A function will work on any data that is compatible with
the statements in the function.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

If there are errors in a function, they appear at run time (as an exception).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

To verify code, there is a strong emphasis on testing (covered later).

### Exceptions

Exceptions are used to signal errors.
To raise an exception yourself, use `raise` statement.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

To catch an exception use `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```

### Exception Handling

Exceptions propagate to the first matching `except`.

```python
def grok():
    ...
    raise RuntimeError('Whoa!')   # Exception raised here

def spam():
    grok()                        # Call that will raise exception

def bar():
    try:
       spam()
    except RuntimeError as e:     # Exception caught here
        ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Exception does NOT arrive here
        ...

foo()
```

To handle the exception, put statements in the `except` block. You can add any
statements you want to handle the error.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements              # Use this statements
        statements
        ...

bar()
```

After handling, execution resumes with the first statement after the
`try-except`.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements
        statements
        ...
    statements                  # Resumes execution here
    statements                  # And continues here
    ...

bar()
```

### Built-in Exceptions

There are about two-dozen built-in exceptions.  Usually the name of
the exception is indicative of what's wrong (e.g., a `ValueError` is
raised because you supplied a bad value). This is not an
exhaustive list. Check the [documentation](https://docs.python.org/3/library/exceptions.html) for more.

```python
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
```

### Exception Values

Exceptions have an associated value. It contains more specific
information about what's wrong.

```python
raise RuntimeError('Invalid user name')
```

This value is part of the exception instance that's placed in the variable supplied to `except`.

```python
try:
    ...
except RuntimeError as e:   # `e` holds the exception raised
    ...
```

`e` is an instance of the exception type. However, it often looks like a string when
printed.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```

### Catching Multiple Errors

You can catch different kinds of exceptions using multiple `except` blocks.

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

Alternatively, if the statements to handle them is the same, you can group them:

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```

### Catching All Errors

To catch any exception, use `Exception` like this:

```python
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
```

In general, writing code like that is a bad idea because you'll have
no idea why it failed.

### Wrong Way to Catch Errors

Here is the wrong way to use exceptions.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

This catches all possible errors and it may make it impossible to debug
when the code is failing for some reason you didn't expect at all
(e.g. uninstalled Python module, etc.).

### Somewhat Better Approach

If you're going to catch all errors, this is a more sane approach.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

It reports a specific reason for failure.  It is almost always a good
idea to have some mechanism for viewing/reporting errors when you
write code that catches all possible exceptions.

In general though, it's better to catch the error as narrowly as is
reasonable. Only catch the errors you can actually handle. Let
other errors pass by--maybe some other code can handle them.

### Reraising an Exception

Use `raise` to propagate a caught error.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

This allows you to take action (e.g. logging) and pass the error on to
the caller.

### Exception Best Practices

Don't catch exceptions. Fail fast and loud. If it's important, someone
else will take care of the problem.  Only catch an exception if you
are *that* someone.  That is, only catch errors where you can recover
and sanely keep going.

### `finally` statement

It specifies code that must run regardless of whether or not an
exception occurs.

```python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
```

Commonly used to safely manage resources (especially locks, files, etc.).

### `with` statement

In modern code, `try-finally` is often replaced with the `with` statement.

```python
lock = Lock()
with lock:
    # lock acquired
    ...
# lock released
```

A more familiar example:

```python
with open(filename) as f:
    # Use the file
    ...
# File closed
```

`with` defines a usage *context* for a resource.  When execution
leaves that context, resources are released. `with` only works with
certain objects that have been specifically programmed to support it.
