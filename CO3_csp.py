# CO3 - Constraint Satisfaction

GRID = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

sensor_observation = (1,1)

candidates = []

for i in range(3):
    for j in range(3):

        if GRID[i][j] == 0:
            candidates.append((i,j))

def satisfies_constraint(cell):

    x,y = cell

    return (x+y)%2 == 0

def backtracking(candidates):

    solutions = []

    for cell in candidates:

        if satisfies_constraint(cell):
            solutions.append(cell)

    return solutions

print("\nPossible Positions:")
print(candidates)

print("\nValid Positions After CSP:")
print(backtracking(candidates))
