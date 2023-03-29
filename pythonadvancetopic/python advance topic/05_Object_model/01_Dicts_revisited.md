[Contents](../Contents.md) \| [Previous (4.4 Exceptions)](../04_Classes_objects/04_Defining_exceptions.md) \| [Next (5.2 Encapsulation)](02_Classes_encapsulation.md)

# 5.1 Dictionaries Revisited

The Python object system is largely based on an implementation
involving dictionaries.  This section discusses that.

### Dictionaries, Revisited

Remember that a dictionary is a collection of named values.

```python
stock = {
    'name' : 'GOOG',
    'shares' : 100,
    'price' : 490.1
}
```

Dictionaries are commonly used for simple data structures.  However,
they are used for critical parts of the interpreter and may be the
*most important type of data in Python*.

### Dicts and Modules

Within a module, a dictionary holds all of the global variables and
functions.

```python
# foo.py

x = 42
def bar():
    ...

def spam():
    ...
```

If you inspect `foo.__dict__` or `globals()`, you'll see the dictionary.

```python
{
    'x' : 42,
    'bar' : <function bar>,
    'spam' : <function spam>
}
```

### Dicts and Objects

User defined objects also use dictionaries for both instance data and
classes.  In fact, the entire object system is mostly an extra layer
that's put on top of dictionaries.

A dictionary holds the instance data, `__dict__`.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
```

You populate this dict (and instance) when assigning to `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

The instance data, `self.__dict__`, looks like this:

```python
{
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

**Each instance gets its own private dictionary.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

If you created 100 instances of some class, there are 100 dictionaries
sitting around holding data.

### Class Members

A separate dictionary also holds the methods.

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

The dictionary is in `Stock.__dict__`.

```python
{
    'cost': <function>,
    'sell': <function>,
    '__init__': <function>
}
```

### Instances and Classes

Instances and classes are linked together.  The `__class__` attribute
refers back to the class.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

The instance dictionary holds data unique to each instance, whereas
the class dictionary holds data collectively shared by *all*
instances.

### Attribute Access

When you work with objects, you access data and methods using the `.` operator.

```python
x = obj.name          # Getting
obj.name = value      # Setting
del obj.name          # Deleting
```

These operations are directly tied to the dictionaries sitting underneath the covers.

### Modifying Instances

Operations that modify an object update the underlying dictionary.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name':'GOOG', 'shares': 100, 'price': 490.1 }
>>> s.shares = 50       # Setting
>>> s.date = '6/7/2007' # Setting
>>> s.__dict__
{ 'name': 'GOOG', 'shares': 50, 'price': 490.1, 'date': '6/7/2007' }
>>> del s.shares        # Deleting
>>> s.__dict__
{ 'name': 'GOOG', 'price': 490.1, 'date': '6/7/2007' }
>>>
```

### Reading Attributes

Suppose you read an attribute on an instance.

```python
x = obj.name
```

The attribute may exist in two places:

* Local instance dictionary.
* Class dictionary.

Both dictionaries must be checked.  First, check in local `__dict__`.
If not found, look in `__dict__` of class through `__class__`.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

This lookup scheme is how the members of a *class* get shared by all instances.

### How inheritance works

Classes may inherit from other classes.

```python
class A(B, C):
    ...
```

The base classes are stored in a tuple in each class.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

This provides a link to parent classes.

### Reading Attributes with Inheritance

Logically, the process of finding an attribute is as follows. First,
check in local `__dict__`.  If not found, look in `__dict__` of the
class.  If not found in class, look in the base classes through
`__bases__`.   However, there are some subtle aspects of this discussed next.

### Reading Attributes with Single Inheritance

In inheritance hierarchies, attributes are found by walking up the
inheritance tree in order.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```
With single inheritance, there is single path to the top.
You stop with the first match.

### Method Resolution Order or MRO

Python precomputes an inheritance chain and stores it in the *MRO* attribute on the class.
You can view it.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

This chain is called the **Method Resolution Order**.  To find an
attribute, Python walks the MRO in order. The first match wins.

### MRO in Multiple Inheritance

With multiple inheritance, there is no single path to the top.
Let's take a look at an example.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

What happens when you access an attribute?

```python
e = E()
e.attr
```

An attribute search process is carried out, but what is the order? That's a problem.

Python uses *cooperative multiple inheritance* which obeys some rules
about class ordering.

* Children are always checked before parents
* Parents (if multiple) are always checked in the order listed.

The MRO is computed by sorting all of the classes in a hierarchy
according to those rules.

```python
>>> E.__mro__
(
  <class 'E'>,
  <class 'C'>,
  <class 'A'>,
  <class 'D'>,
  <class 'B'>,
  <class 'object'>)
>>>
```

The underlying algorithm is called the "C3 Linearization Algorithm."
The precise details aren't important as long as you remember that a
class hierarchy obeys the same ordering rules you might follow if your
house was on fire and you had to evacuate--children first, followed by
parents.

### An Odd Code Reuse (Involving Multiple Inheritance)

Consider two completely unrelated objects:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commonality with LoudBike (below)
        return super().noise().upper()
```

And

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commonality with LoudDog (above)
        return super().noise().upper()
```

There is a code commonality in the implementation of `LoudDog.noise()` and
`LoudBike.noise()`.  In fact, the code is exactly the same.  Naturally,
code like that is bound to attract software engineers.

### The "Mixin" Pattern

The *Mixin* pattern is a class with a fragment of code.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

This class is not usable in isolation.
It mixes with other classes via inheritance.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Miraculously, loudness was now implemented just once and reused
in two completely unrelated classes.  This sort of trick is one
of the primary uses of multiple inheritance in Python.

### Why `super()`

Always use `super()` when overriding methods.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delegates to the *next class* on the MRO.

The tricky bit is that you don't know what it is.  You especially don't
know what it is if multiple inheritance is being used.

### Some Cautions

Multiple inheritance is a powerful tool. Remember that with power
comes responsibility.  Frameworks / libraries sometimes use it for
advanced features involving composition of components.  Now, forget
that you saw that.
