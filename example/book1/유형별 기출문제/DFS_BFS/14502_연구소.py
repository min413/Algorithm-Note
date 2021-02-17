n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

dap = 0

# 바이러스 퍼지게 하는 함수
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 맵에서 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global dap

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        dap = max(dap, get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1

dfs(0)
print(dap)

