# ===============================
# CO3 - Constraint Satisfaction
# ===============================

GRID = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

candidates = []

for i in range(3):
    for j in range(3):
        if GRID[i][j] == 0:
            candidates.append((i,j))

def satisfies(cell):
    x, y = cell
    return (x + y) % 2 == 0

def backtracking(candidates):
    return [c for c in candidates if satisfies(c)]

print("\n--- CO3: CSP ---")
print("Candidates:", candidates)
print("Valid:", backtracking(candidates))
print(candidates)
