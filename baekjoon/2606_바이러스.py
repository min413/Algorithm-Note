'''
n : 컴퓨터 수
m : 네트워크 연결된 컴퓨터 쌍 수
1번 컴퓨터가 무조건 감염시작된다

'''
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
# 이러면 빠르게 입력받을 수 있다

graph = [[0]*(n+1) for i in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dap = 0
def dfs(x):
    global dap
    visited[x] = True
    dap += 1
    for i in range(1, n+1):
        if not visited[i] and graph[x][i] == 1:
            dfs(i)

dfs(1)
print(dap-1)

