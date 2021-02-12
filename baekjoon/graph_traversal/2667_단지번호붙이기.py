'''
1 : 집
0 : 아무것도 없음

단지 : park
각 단지에서 집 개수 : houses

'''
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
'''
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range(n)]

# 이거 하면 문자로 받아야 한다 => '0', '1', '1'
'''
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 이 부분이 숫자 버전
    
houses = 0
park = []


def dfs(x,y):
    global houses
    graph[x][y] = 0 # 방문한 곳은 0
    houses += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집
            houses = 0
            dfs(i,j)
            park.append(houses)

print(len(park))
park.sort()
for i in park:
    print(i)
