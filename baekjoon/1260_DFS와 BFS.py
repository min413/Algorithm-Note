'''
n : 정점 개수
m : 간선 개수
v : 탐색 시작 정점

'''
from collections import deque
n,m,v = map(int, input().split())

graph = [[0]*(n+1) for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(v)
print()
bfs(v)
        
        

