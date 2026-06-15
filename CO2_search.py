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
