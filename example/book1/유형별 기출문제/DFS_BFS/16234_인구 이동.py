from collections import deque

n,l,r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dap = 0

def dfs(x,y,index):
    # (x,y) 위치와 연결된 연합 정보를 담는 리스트
    united = []
    united.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    cnt = 1 # 현재 연합의 국가 수

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 주변 나라를 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    cnt += 1
                    united.append((nx,ny))
    for i,j in united:
        graph[i][j] = summary//cnt
    return cnt

total_cnt = 0

while 1:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                dfs(i,j,index)
                index += 1
    if index == n*n:
        break
    total_cnt += 1
print(total_cnt)
