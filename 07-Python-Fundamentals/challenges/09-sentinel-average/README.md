# Average Until Sentinel

**Level:** Progressive practice · **Reference:** lesson slides.

## Challenge

Read integer grades until -1. Accept grades from 0 to 10; for any other value print an error and continue. Stop on -1. Print count and average to two decimals, or “No grades” if none are valid. Do not use lists.

## Expected Results

8,6,-1 → count 2, average 7.00. -1 → No grades. 12,0,10,-1 → one error, count 2, average 5.00.

## Your Work

Implement your answer in [main.py](main.py). Record predictions and results in [notes.md](notes.md). Check the examples and add one of your own. From this folder, run `python main.py` (or `py main.py` on Windows).

<details>
<summary>Hint — open after trying</summary>

Check the sentinel before validating a grade; avoid division by zero.

</details>
