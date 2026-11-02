# One List, Two Names

**Level:** Progressive practice · **Reference:** lesson slides.

## Challenge

Set a=[1,2], b=a; predict what happens after b.append(3), then print both and compare their ids. Next set x="Hi", y=x; run y += "!" and print both. Explain the difference in notes.md.

## Expected Results

After append, both lists are [1,2,3] and their ids match. Then x is "Hi" and y is "Hi!".

## Your Work

Implement your answer in [main.py](main.py). Record predictions and results in [notes.md](notes.md). Check the examples and add one of your own. From this folder, run `python main.py` (or `py main.py` on Windows).

<details>
<summary>Hint — open after trying</summary>

append mutates a list; string concatenation creates a new string.

</details>
