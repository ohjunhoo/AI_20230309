[Contents](../Contents.md) \| [Previous (4.1 Classes)](01_Class.md) \| [Next (4.3 Special methods)](03_Special_methods.md)

# 4.2 Inheritance

Inheritance is a commonly used tool for writing extensible programs.
This section explores that idea.

### Introduction

Inheritance is used to specialize existing objects:

```python
class Parent:
    ...

class Child(Parent):
    ...
```

The new class `Child` is called a derived class or subclass.  The
`Parent` class is known as base class or superclass.  `Parent` is
specified in `()` after the class name, `class Child(Parent):`.

### Extending

With inheritance, you are taking an existing class and:

* Adding new methods
* Redefining some of the existing methods
* Adding new attributes to instances

In the end you are **extending existing code**.

### Example

Suppose that this is your starting class:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

You can change any part of this via inheritance.

### Add a new method

```python
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
```

Usage example.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.shares
75
>>> s.panic()
>>> s.shares
0
>>>
```

### Redefining an existing method

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Usage example.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

The new method takes the place of the old one. The other methods are unaffected. It's tremendous.

## Overriding

Sometimes a class extends an existing method, but it wants to use the
original implementation inside the redefinition.  For this, use `super()`:

```python
class Stock:
    ...
    def cost(self):
        return self.shares * self.price
    ...

class MyStock(Stock):
    def cost(self):
        # Check the call to `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Use `super()` to call the previous version.

*Caution: In Python 2, the syntax was more verbose.*

```python
actual_cost = super(MyStock, self).cost()
```

### `__init__` and inheritance

If `__init__` is redefined, it is essential to initialize the parent.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

You should call the `__init__()` method on the `super` which is the
way to call the previous version as shown previously.

### Using Inheritance

Inheritance is sometimes used to organize related objects.

```python
class Shape:
    ...

class Circle(Shape):
    ...

class Rectangle(Shape):
    ...
```

Think of a logical hierarchy or taxonomy.  However, a more common (and
practical) usage is related to making reusable or extensible code.
For example, a framework might define a base class and instruct you
to customize it.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
        ...
        # Custom processing
```

The base class contains some general purpose code.
Your class inherits and customized specific parts.

### "is a" relationship

Inheritance establishes a type relationship.

```python
class Shape:
    ...

class Circle(Shape):
    ...
```

Check for object instance.

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

*Important: Ideally, any code that worked with instances of the parent
class will also work with instances of the child class.*

### `object` base class

If a class has no parent, you sometimes see `object` used as the base.

```python
class Shape(object):
    ...
```

`object` is the parent of all objects in Python.

*Note: it's not technically required, but you often see it specified
as a hold-over from it's required use in Python 2. If omitted, the
class still implicitly inherits from `object`.

### Multiple Inheritance

You can inherit from multiple classes by specifying them in the definition of the class.

```python
class Mother:
    ...

class Father:
    ...

class Child(Mother, Father):
    ...
```

The class `Child` inherits features from both parents.  There are some
rather tricky details. Don't do it unless you know what you are doing.
Some further information will be given in the next section, but we're not
going to utilize multiple inheritance further in this course.
