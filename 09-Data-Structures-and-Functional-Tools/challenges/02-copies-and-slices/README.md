# Copy or Alias?

**Level:** Progressive practice · **Reference:** lesson slides.

## Challenge

Create original, alias=original, and copy=original[:]. Mutate the alias and replace a slice in the copy. Show all lists and identity comparisons. Then delete a slice from [1,2,3,4,5].

## Expected Results

Original and alias share changes; copy does not. Slice deletion leaves [1,5].

## Your Work

Implement your answer in [main.py](main.py). Record predictions and results in [notes.md](notes.md). Check the examples and add one of your own. From this folder, run `python main.py` (or `py main.py` on Windows).

<details>
<summary>Hint — open after trying</summary>

A slice makes a shallow copy of the outer list.

</details>
