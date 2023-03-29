[Contents](../Contents.md) \| [Previous (3.1 Scripting)](01_Script.md) \| [Next (3.3 Error Checking)](03_Error_checking.md)

# 3.2 More on Functions

Although functions were introduced earlier, very few details were provided on how
they actually work at a deeper level.  This section aims to fill in some gaps
and discuss matters such as calling conventions, scoping rules, and more.

### Calling a Function

Consider this function:

```python
def read_prices(filename, debug):
    ...
```

You can call the function with positional arguments:

```
prices = read_prices('prices.csv', True)
```

Or you can call the function with keyword arguments:

```python
prices = read_prices(filename='prices.csv', debug=True)
```

### Default Arguments

Sometimes you want an argument to be optional.  If so, assign a default value
in the function definition.

```python
def read_prices(filename, debug=False):
    ...
```

If a default value is assigned, the argument is optional in function calls.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

*Note: Arguments with defaults must appear at the end of the arguments list (all non-optional arguments go first).*

### Prefer keyword arguments for optional arguments

Compare and contrast these two different calling styles:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

In most cases, keyword arguments improve code clarity--especially for arguments that
serve as flags or which are related to optional features.

### Design Best Practices

Always give short, but meaningful names to functions arguments.

Someone using a function may want to use the keyword calling style.

```python
d = read_prices('prices.csv', debug=True)
```

Python development tools will show the names in help features and documentation.

### Returning Values

The `return` statement returns a value

```python
def square(x):
    return x * x
```

If no return value is given or `return` is missing, `None` is returned.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```

### Multiple Return Values

Functions can only return one value.  However, a function may return
multiple values by returning them in a tuple.

```python
def divide(a,b):
    q = a // b      # Quotient
    r = a % b       # Remainder
    return q, r     # Return a tuple
```

Usage example:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```

### Variable Scope

Programs assign values to variables.

```python
x = value # Global variable

def foo():
    y = value # Local variable
```

Variables assignments occur outside and inside function definitions.
Variables defined outside are "global". Variables inside a function
are "local".

### Local Variables

Variables assigned inside functions are private.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

In this example, `filename`, `portfolio`, `line`, `fields` and `s` are local variables.
Those variables are not retained or accessible after the function call.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

Locals also can't conflict with variables found elsewhere.

### Global Variables

Functions can freely access the values of globals defined in the same
file.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Using `name` global variable
```

However, functions can't modify globals:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # prints 'Dave'
```

**Remember: All assignments in functions are local.**

### Modifying Globals

If you must modify a global variable you must declare it as such.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Changes the global name above
```

The global declaration must appear before its use and the corresponding
variable must exist in the same file as the function.   Having seen this,
know that it is considered poor form.  In fact, try to avoid `global` entirely
if you can.  If you need a function to modify some kind of state outside
of the function, it's better to use a class instead (more on this later).

### Argument Passing

When you call a function, the argument variables are names that refer
to the passed values. These values are NOT copies (see [section
2.7](../02_Working_with_data/07_Objects)). If mutable data types are
passed (e.g. lists, dicts), they can be modified *in-place*.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**

### Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a
value and reassigning a variable name.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Changes local `items` variable to point to a different object

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

*Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.*
