# Notes on the Slides

## Lesson 7

- CPython compiles source to bytecode internally; running a script does not require the separate compile-and-link step common in C. A `.pyc` file is not guaranteed beside every executed script.
- Triple-quoted strings are string literals, not block comments. A string is a docstring only in a documented position. Use `#` for comments.
- `id()` returns an identity value for an object's lifetime; do not treat it as a portable memory address or fixed output.
- Use straight quotes in code. Curly typographic quotes may cause syntax errors.

## Lesson 8

- For `word = "Programming"`, `word[::2]` is `"Pormig"`; the slide's example result is incorrect.
- Assigning to a name inside a function normally makes it local. `global` refers to a module-level name.
- A function docstring is the first string expression in its body.

## Lesson 9

- A list slice makes a shallow copy; nested mutable objects can still be shared.
- Dictionaries preserve insertion order in modern Python; sets do not guarantee positional order.
- Dictionary keys must be hashable. A tuple containing a list is not a valid key.
- Comprehensions and functional tools are not always more readable. `map` and `filter` return iterators; `zip` stops at the shortest iterable by default.

When checking sets, compare membership rather than printed order. `{}` is an empty dictionary; `set()` is an empty set.
