from collections import deque
import heapq

graph = {
    'A': {'B':1,'C':4},
    'B': {'D':2,'E':5},
    'C': {'F':1},
    'D': {},
    'E': {'G':2},
    'F': {'G':3},
    'G': {}
}

# BFS
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

            for neighbor in graph[node]:
                queue.append(path+[neighbor])

# DFS
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

            for neighbor in graph[node]:
                stack.append(path+[neighbor])

# UCS
def ucs(start, goal):

    pq = [(0,start,[start])]

    while pq:

        cost,node,path = heapq.heappop(pq)

        if node == goal:
            return path,cost

        for neighbor,w in graph[node].items():

            heapq.heappush(
                pq,
                (cost+w,
                 neighbor,
                 path+[neighbor])
            )

# A*
heuristic = {
    'A':6,
    'B':4,
    'C':4,
    'D':3,
    'E':2,
    'F':2,
    'G':0
}

def astar(start,goal):

    pq = [(0,start,[start],0)]

    while pq:

        f,node,path,g = heapq.heappop(pq)

        if node == goal:
            return path,g

        for neighbor,w in graph[node].items():

            new_g = g+w
            new_f = new_g+heuristic[neighbor]

            heapq.heappush(
                pq,
                (new_f,
                 neighbor,
                 path+[neighbor],
                 new_g)
            )

print("\nBFS:", bfs('A','G'))
print("DFS:", dfs('A','G'))
print("UCS:", ucs('A','G'))
print("A* :", astar('A','G'))print(candidates)

print("\nValid Positions After CSP:")
print(backtracking(candidates))
