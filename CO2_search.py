from collections import deque

graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}

def bfs(start,goal):

    queue = deque([[start]])

    while queue:

        path = queue.popleft()

        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            queue.append(path+[neighbor])

print("BFS:", bfs('A','E'))
