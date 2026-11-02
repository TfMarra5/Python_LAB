# My Notes

## Prediction Before Running

- The program prints the values and types, then the two `isinstance()` results. It displays identity values before and after reassignment, followed by checks for two string methods.

## Checked Cases and Results

- `42` is an `int`; `3.5` is a `float`; `True` is a `bool`; `"42"` is a `str`; `None` is `NoneType`.
- `isinstance(42, int)` is `True`; `isinstance("42", int)` is `False`.
- The numeric values returned by `id()` can vary. `upper` and `lower` are names included by `dir("Python")`.

## My Additional Case

- Input: None. Change `a` to `42.0` before the first type check.
- Expected result: `a` is a `float`; `isinstance(a, int)` is `False`.
- Actual result: Check after making the change and running the program.

## What I Learned and Questions

- `type()` reports an object's type, while `isinstance()` checks whether it belongs to a type.
- Reassignment can make the same variable refer to a value of a different type. `id()` reports object identity; its numeric value is not a fixed expected result.
- `dir()` lists available attributes and methods.
