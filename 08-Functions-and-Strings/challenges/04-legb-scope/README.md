# Name Lookup

**Level:** Progressive practice · **Reference:** lesson slides.

## Challenge

Create nested functions with text assigned at local, enclosing, and module scope. Print the nearest value, then remove assignments one at a time and observe lookup. Explain LEGB and why naming a variable len can interfere with len("abc").

## Expected Results

Prints local, then enclosing, then global as inner assignments are removed.

## Your Work

Implement your answer in [main.py](main.py). Record predictions and results in [notes.md](notes.md). Check the examples and add one of your own. From this folder, run `python main.py` (or `py main.py` on Windows).

<details>
<summary>Hint — open after trying</summary>

Python searches Local, Enclosing, Global, then Built-in.

</details>
