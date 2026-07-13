"""Calculator module providing basic arithmetic operations.

Exported functions:
    add(a, b)      -- Return the sum of two numeric operands.
    subtract(a, b) -- Return the difference of two numeric operands.

Only int and float operands are accepted.  bool is explicitly rejected
(even though it is a subclass of int), and any other unsupported type
raises TypeError.
"""


def _validate_numeric(a, b) -> None:
    """Raise TypeError if either operand is not int or float.

    bool is explicitly rejected because it is semantically a discrete
    truth value rather than a general number, despite being a subclass
    of int in Python.
    """
    for name, val in (("a", a), ("b", b)):
        if isinstance(val, bool):
            raise TypeError(
                f"unsupported operand type(s) for '{name}': bool"
            )
        if not isinstance(val, (int, float)):
            raise TypeError(
                f"unsupported operand type(s) for '{name}': {type(val).__name__}"
            )


def add(a, b):
    """Return a + b for numeric operands.

    Raises TypeError if either operand is not int or float.
    """
    _validate_numeric(a, b)
    return a + b


def subtract(a, b):
    """Return a - b for numeric operands.

    Raises TypeError if either operand is not int or float.
    """
    _validate_numeric(a, b)
    return a - b
