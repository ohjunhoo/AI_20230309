[Contents](../Contents.md) \| [Previous (4.3 Special methods)](03_Special_methods.md) \| [Next (5 Object Model)](../05_Object_model/00_Overview.md)

# 4.4 Defining Exceptions

User defined exceptions are defined by classes.

```python
class NetworkError(Exception):
    pass
```

**Exceptions always inherit from `Exception`.**

Usually they are empty classes. Use `pass` for the body.

You can also make a hierarchy of your exceptions.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
