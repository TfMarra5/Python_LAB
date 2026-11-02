"""Type Detective.

Read README.md and implement your answer below.
This file is a starting point, not a solution.
"""

# Print each value and its type.
a = 42
b = 3.5
c = True
d = "42"
e = None

for value in (a, b, c, d, e):
    print(value, type(value))

# Check the integer and string values.
print(isinstance(a, int))
print(isinstance(d, int))

# Observe identity before and after reassignment.
print(id(a))
a = "Hello"
print(type(a))
print(id(a))

# Check for two methods returned by dir().
methods = dir("Python")
print("upper" in methods)
print("lower" in methods)
