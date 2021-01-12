# n과 m을 입력받는 코드
n,m = map(int, input().split())

# 그래프 n x m 을 받는 과정
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 함수 생성
def dfs(x,y):
    # 만약 범위를 넘어가면? -> 즉시 종료(False)
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    
    # 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

dap = 0
for i in range(n):
    for j in range(m):

        if dfs(i,j) == True:
            dap += 1

print(dap)
