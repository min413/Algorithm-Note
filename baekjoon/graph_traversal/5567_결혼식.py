from collections import deque

def bfs(x): # bfs의 정석 풀이
    visited[x] = 1 # 방문처리
    queue.append(x)
    while queue:
        x = queue.popleft()
        for i in data[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
    return visited

n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
# 여기까지 표현 익혀두기

queue = deque()
cnt = 0
visited = [0]*(n+1)

dap = bfs(1)
for i in dap:
    if 2 <= i <= 3: # 친구, 친구의 친구
        cnt += 1
print(cnt)
