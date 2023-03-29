[Contents](../Contents.md) \| [Previous (2.2 Containers)](02_Containers.md) \| [Next (2.4 Sequences)](04_Sequences.md)

# 2.3 Formatting

This section is a slight digression, but when you work with data, you
often want to produce structured output (tables, etc.). For example:

```code
      Name      Shares        Price
----------  ----------  -----------
        AA         100        32.20
       IBM          50        91.10
       CAT         150        83.44
      MSFT         200        51.23
        GE          95        40.37
      MSFT          50        65.10
       IBM         100        70.44
```

### String Formatting

One way to format string in Python 3.6+ is with `f-strings`.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

The part `{expression:format}` is replaced.

It is commonly used with `print`.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```

### Format codes

Format codes (after the `:` inside the `{}`) are similar to C `printf()`.  Common codes
include:

```code
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
```

Common modifiers adjust the field width and decimal precision.  This is a partial list:

```code
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```

### Dictionary Formatting

You can use the `format_map()` method to apply string formatting to a dictionary of values:

```python
>>> s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

It uses the same codes as `f-strings` but takes the values from the
supplied dictionary.

### format() method

There is a method `format()` that can apply formatting to arguments or
keyword arguments.

```python
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
>>> '{:10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

Frankly, `format()` is a bit verbose. I prefer f-strings.

### C-Style Formatting

You can also use the formatting operator `%`.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

This requires a single item or a tuple on the right.  Format codes are
modeled after the C `printf()` as well.

*Note: This is the only formatting available on byte strings.*

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>>
```
