# Cryptarithmetic Problem Solver - SEND + MORE = MONEY

## Overview

This project solves a cryptarithmetic problem using the Z3 solver. A cryptarithmetic puzzle is a mathematical puzzle where each letter represents a unique digit, and the goal is to find the correct digits for each letter that satisfy a given arithmetic equation.

### Problem:

Given the cryptarithmetic equation:


Each letter (S, E, N, D, M, O, R, Y) represents a different digit. The task is to determine which digit each letter corresponds to such that the equation holds true.

## Approach

To solve the puzzle, we use the **Z3 solver**, which is a Python library for solving constraint satisfaction problems. The solver will assign digits (0-9) to each letter in a way that satisfies the equation `SEND + MORE = MONEY`. 

### Steps:

1. Define a variable for each letter.
2. Translate the words "SEND", "MORE", and "MONEY" into arithmetic equations using their corresponding letter variables.
3. Add constraints to ensure that:
   - The sum of `SEND` and `MORE` equals `MONEY`.
   - All letters represent distinct digits (i.e., no repeated digits).
   - Each letter corresponds to a digit between 0 and 9.
4. Use the Z3 solver to find a solution that satisfies all the constraints.

## Code Explanation

The code below uses the Z3 solver to find a solution to the cryptarithmetic puzzle.

```python
from z3 import *
from z3 import Solver

# Define variables for each letter
s = Int('S')
e = Int('E')
n = Int('N')
d = Int('D')
m = Int('M')
o = Int('O')
r = Int('R')
y = Int('Y')

# Initialize the solver
solver = Solver()

# Define the numbers formed by the letters
SEND = s * pow(10, 3) + e * pow(10, 2) + n * pow(10, 1) + d * pow(10, 0)
MORE = m * pow(10, 3) + o * pow(10, 2) + r * pow(10, 1) + e * pow(10, 0)
MONEY = m * pow(10, 4) + o * pow(10, 3) + n * pow(10, 2) + e * pow(10, 1) + y * pow(10, 0)

# Add the constraint SEND + MORE = MONEY
solver.add(SEND + MORE == MONEY)

# Add the constraint that all letters must be distinct
solver.add(Distinct(s, e, n, d, m, o, r, y))

# Add the constraint that all letters must be between 0 and 9
for var in [s, e, n, d, m, o, r, y]:
    solver.add(var >= 0, var <= 9)

# Check if a solution exists
if solver.check() == sat:
    model = solver.model()
    print("Solution:\n")
    # Output the values for each letter
    for var in [s, e, n, d]:
        print(f"{var}: {model[var]}")
    for var in [m, o, r, e]:
        print(f"{var}: {model[var]}")
    for var in [m, o, n, e, y]:
        print(f"{var}: {model[var]}")
else:
    print("No solution found")
```
I made this project to learn z3 solver.Modifying this code we can solve any cryptoarithmatic problems.
I gotta know about cryptoarithmatic problem by "problem solving technique book"
this is also studied in AI subject of engineering 
