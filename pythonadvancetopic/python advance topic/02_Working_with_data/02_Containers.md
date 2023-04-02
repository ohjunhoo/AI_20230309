[Contents](../Contents.md) \| [Previous (2.1 Datatypes)](01_Datatypes.md) \| [Next (2.3 Formatting)](03_Formatting.md)

# 2.2 Containers

This section discusses lists, dictionaries, and sets.

### Overview

Programs often have to work with many objects.

* A portfolio of stocks
* A table of stock prices

There are three main choices to use.

* Lists. Ordered data.
* Dictionaries. Unordered data.
* Sets. Unordered collection of unique items.

### Lists as a Container

Use a list when the order of the data matters. Remember that lists can hold any kind of object.
For example, a list of tuples.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]

portfolio[0]            # ('GOOG', 100, 490.1)
portfolio[2]            # ('CAT', 150, 83.44)
```

### List construction

Building a list from scratch.

```python
records = []  # Initial empty list

# Use .append() to add more items
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

An example when reading records from a file.

```python
records = []  # Initial empty list

with open('Data/portfolio.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```

### Dicts as a Container

Dictionaries are useful if you want fast random lookups (by key name).  For
example, a dictionary of stock prices:

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Here are some simple lookups:

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```

### Dict Construction

Example of building a dict from scratch.

```python
prices = {} # Initial empty dict

# Insert new items
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

An example populating the dict from the contents of a file.

```python
prices = {} # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Note: If you try this on the `Data/prices.csv` file, you'll find that
it almost works--there's a blank line at the end that causes it to
crash.  You'll need to figure out some way to modify the code to
account for that (see Exercise 2.6).

### Dictionary Lookups

You can test the existence of a key.

```python
if key in d:
    # YES
else:
    # NO
```

You can look up a value that might not exist and provide a default value in case it doesn't.

```python
name = d.get(key, default)
```

An example:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```

### Composite keys

Almost any type of value can be used as a dictionary key in Python. A dictionary key must be of a type that is immutable.
For example, tuples:

```python
holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}
```

Then to access:

```python
>>> holidays[3, 14]
'Pi day'
>>>
```

*Neither a list, a set, nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable.*

### Sets

Sets are collection of unordered unique items.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Sets are useful for membership tests.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Sets are also useful for duplicate elimination.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Additional set operations:

```python
unique.add('CAT')        # Add an item
unique.remove('YHOO')    # Remove an item

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Set union { 'a', 'b', 'c', 'd' }
s1 & s2                 # Set intersection { 'c' }
s1 - s2                 # Set difference { 'a', 'b' }
```

## Exercises

In these exercises, you start building one of the major programs used
for the rest of this course.  Do your work in the file `Work/report.py`.

### Exercise 2.4: A list of tuples

The file `Data/portfolio.csv` contains a list of stocks in a
portfolio.  In [Exercise 1.30](../01_Introduction/07_Functions.md), you
wrote a function `portfolio_cost(filename)` that read this file and
performed a simple calculation.

Your code should have looked something like this:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Using this code as a rough guide, create a new file `report.py`.  In
that file, define a function `read_portfolio(filename)` that opens a
given portfolio file and reads it into a list of tuples.  To do this,
you’re going to make a few minor modifications to the above code.

First, instead of defining `total_cost = 0`, you’ll make a variable
that’s initially set to an empty list. For example:

```python
portfolio = []
```

Next, instead of totaling up the cost, you’ll turn each row into a
tuple exactly as you just did in the last exercise and append it to
this list. For example:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Finally, you’ll return the resulting `portfolio` list.

Experiment with your function interactively (just a reminder that in
order to do this, you first have to run the `report.py` program in the
interpreter):

*Hint: Use `-i` when executing the file in the terminal*

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

This list of tuples that you have created is very similar to a 2-D
array.  For example, you can access a specific column and row using a
lookup such as `portfolio[row][column]` where `row` and `column` are
integers.

That said, you can also rewrite the last for-loop using a statement like this:

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
