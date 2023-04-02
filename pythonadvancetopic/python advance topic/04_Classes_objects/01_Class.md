[Contents](../Contents.md) \| [Previous (3.6 Design discussion)](../03_Program_organization/06_Design_discussion.md) \| [Next (4.2 Inheritance)](02_Inheritance.md)

# 4.1 Classes

This section introduces the class statement and the idea of creating new objects.

### Object Oriented (OO) programming

A Programming technique where code is organized as a collection of
*objects*.

An *object* consists of:

* Data. Attributes
* Behavior. Methods which are functions applied to the object.

You have already been using some OO during this course.

For example, manipulating a list.

```python
>>> nums = [1, 2, 3]
>>> nums.append(4)      # Method
>>> nums.insert(1,10)   # Method
>>> nums
[1, 10, 2, 3, 4]        # Data
>>>
```

`nums` is an *instance* of a list.

Methods (`append()` and `insert()`) are attached to the instance (`nums`).

### The `class` statement

Use the `class` statement to define a new object.

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts
```

In a nutshell, a class is a set of functions that carry out various operations on so-called *instances*.

### Instances

Instances are the actual *objects* that you manipulate in your program.

They are created by calling the class as a function.

```python
>>> a = Player(2, 3)
>>> b = Player(10, 20)
>>>
```

`a` and `b` are instances of `Player`.

*Emphasize: The class statement is just the definition (it does
 nothing by itself). Similar to a function definition.*

### Instance Data

Each instance has its own local data.

```python
>>> a.x
2
>>> b.x
10
```

This data is initialized by the `__init__()`.

```python
class Player:
    def __init__(self, x, y):
        # Any value stored on `self` is instance data
        self.x = x
        self.y = y
        self.health = 100
```

There are no restrictions on the total number or type of attributes stored.

### Instance Methods

Instance methods are functions applied to instances of an object.

```python
class Player:
    ...
    # `move` is a method
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

The object itself is always passed as first argument.

```python
>>> a.move(1, 2)

# matches `a` to `self`
# matches `1` to `dx`
# matches `2` to `dy`
def move(self, dx, dy):
```

By convention, the instance is called `self`. However, the actual name
used is unimportant. The object is always passed as the first
argument. It is merely Python programming style to call this argument
`self`.

### Class Scoping

Classes do not define a scope of names.

```python
class Player:
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NO. Calls a global `move` function
        self.move(-amt, 0)  # YES. Calls method `move` from above.
```

If you want to operate on an instance, you always refer to it explicitly (e.g., `self`).
