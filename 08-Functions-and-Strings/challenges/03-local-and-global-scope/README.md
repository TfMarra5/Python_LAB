# Counter and Scope

**Level:** Progressive practice · **Reference:** lesson slides.

## Challenge

Show a module-level counter=10 and a local counter=3 inside a function. Then increment the global counter twice using global. Finally implement increment(value) that returns value+1 without global. Explain the difference.

## Expected Results

Inside 3, outside 10; global becomes 12; increment(12) returns 13 without changing it.

## Your Work

Implement your answer in [main.py](main.py). Record predictions and results in [notes.md](notes.md). Check the examples and add one of your own. From this folder, run `python main.py` (or `py main.py` on Windows).

<details>
<summary>Hint — open after trying</summary>

The same identifier can refer to different variables in different scopes.

</details>
