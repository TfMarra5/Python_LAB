# Optional Bonus — Pandas apply

Reference: lesson 9, slide 32. This activity requires the external Pandas library; the other challenges do not.

## Setup

If Pandas is not installed, run these commands from the repository root:

```powershell
python -m venv .venv
.venv\\Scripts\\python.exe -m pip install pandas
.venv\\Scripts\\python.exe 09-Data-Structures-and-Functional-Tools/bonus/pandas-apply/main.py
```

## Challenge

Create a DataFrame with Name=["Ana","Rui","Bia"] and Score=[90,80,98]. Use apply and lambda on Score to create Bonus by adding 10, capped at 100. Preserve Score and print all three columns. Repeat with Score=[0,100]. Do not use loops.

## Expected Results

First set: Bonus=[100,90,100]; Score remains [90,80,98]. Second set, with Name=["X","Y"]: Bonus=[10,100]; Score remains [0,100].

Hint: apply passes one score at a time; min can cap the result.
