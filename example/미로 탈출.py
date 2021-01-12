'''
bfs 이용
0 : 괴물존재
1 : 갈 수 있는 길

'''

from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        # 네 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간 범위 넘어가면 무시(continue)
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽일 때도 무시
            if graph[nx][ny] == 0:
                continue

            # 길을 처음 방문했다면 최단 거리 기록하기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    
    return graph[n-1][m-1]

print(bfs(0,0))
