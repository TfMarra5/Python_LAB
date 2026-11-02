# Menu Calculator

**Level:** Progressive practice · **Reference:** lesson slides.

## Challenge

Repeat a menu: 1 add, 2 divide, 0 quit. For choices 1 and 2, read two floats. Handle division by zero and invalid choices without asking for operands. Do not define functions; assume numeric inputs are valid.

## Expected Results

1,2,3,0 → 5.0 then quits. 2,7,2,0 → 3.5. 2,7,0,0 → division error then quits. 9,0 → invalid choice and exits.

## Your Work

Implement your answer in [main.py](main.py). Record predictions and results in [notes.md](notes.md). Check the examples and add one of your own. From this folder, run `python main.py` (or `py main.py` on Windows).

<details>
<summary>Hint — open after trying</summary>

Use while for the session and separate branches for each choice.

</details>
