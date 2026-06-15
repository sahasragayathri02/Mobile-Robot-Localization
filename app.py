# ===============================
# MOBILE ROBOT LOCALIZATION AI PROJECT
# ===============================

from collections import deque
import heapq

# ===============================
# CO1 - Problem Representation
# ===============================

class State:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def __str__(self):
        return f"({self.x},{self.y},{self.heading})"


ACTIONS = ["FORWARD", "TURN_LEFT", "TURN_RIGHT"]

robot = State(2, 3, "N")
confidence = 0.87

print("\n--- CO1: STATE REPRESENTATION ---")
print("Robot State:", robot)
print("Actions:", ACTIONS)

print("Goal Test:", "Localized" if confidence >= 0.85 else "Continue")

# ===============================
# CO2 - Search Algorithms
# ===============================

graph = {
    'A': {'B':1,'C':4},
    'B': {'D':2,'E':5},
    'C': {'F':1},
    'D': {},
    'E': {'G':2},
    'F': {'G':3},
    'G': {}
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                queue.append(path + [n])

def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                stack.append(path + [n])

def ucs(start, goal):
    pq = [(0, start, [start])]

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        for n, w in graph[node].items():
            heapq.heappush(pq, (cost + w, n, path + [n]))

heuristic = {
    'A':6,'B':4,'C':4,'D':3,'E':2,'F':2,'G':0
}

def astar(start, goal):
    pq = [(0, start, [start], 0)]

    while pq:
        f, node, path, g = heapq.heappop(pq)

        if node == goal:
            return path, g

        for n, w in graph[node].items():
            new_g = g + w
            new_f = new_g + heuristic[n]
            heapq.heappush(pq, (new_f, n, path + [n], new_g))

print("\n--- CO2: SEARCH ---")
print("BFS:", bfs('A','G'))
print("DFS:", dfs('A','G'))
print("UCS:", ucs('A','G'))
print("A* :", astar('A','G'))

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

# ===============================
# CO4 - Decision Agent
# ===============================

actions = {
    "FORWARD": {"info_gain":5, "cost":1},
    "TURN_LEFT":{"info_gain":3, "cost":0.5},
    "TURN_RIGHT":{"info_gain":2, "cost":0.5}
}

def utility(info_gain, cost):
    return info_gain - 0.2 * cost

best_action = None
best_score = -999

print("\n--- CO4: DECISION AGENT ---")

for a, data in actions.items():
    score = utility(data["info_gain"], data["cost"])
    print(a, "=>", score)

    if score > best_score:
        best_score = score
        best_action = a

print("Best Action:", best_action)

# ===============================
# CO5 - Bayes Filter
# ===============================

belief = {"A":0.25,"B":0.25,"C":0.25,"D":0.25}
likelihood = {"A":0.1,"B":0.9,"C":0.6,"D":0.2}

print("\n--- CO5: BAYES FILTER ---")
print("Initial Belief:", belief)

new_belief = {}
total = 0

for s in belief:
    new_belief[s] = belief[s] * likelihood[s]
    total += new_belief[s]

for s in new_belief:
    new_belief[s] /= total

print("Updated Belief:", new_belief)
print("Most Likely:", max(new_belief, key=new_belief.get))

# ===============================
# CO6 - Integrated Pipeline
# ===============================

states = [(0,0),(0,1),(1,0),(1,1)]

print("\n--- CO6: INTEGRATED PIPELINE ---")
print("Initial States:", states)

valid_states = [s for s in states if s != (1,1)]
print("CSP Filtered:", valid_states)

belief = {s:1/len(valid_states) for s in valid_states}
print("Belief:", belief)

best_action = "FORWARD"
confidence = 0.90

print("Action:", best_action)
print("Confidence:", confidence)

if confidence >= 0.85:
    print("Robot Localized ✔")

    path = [(0,0),(0,1),(1,1),(2,1)]
    print("Planned Path:", path)
else:
    print("Continue Localization")
