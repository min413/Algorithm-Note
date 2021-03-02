'''
두번의 삽질을 거쳤다
첫번째 : (i,j) 부터 (x,y) 위치에 있는 값을 모두 더하는 것으로 잘못 이해함
두번째 : 문제의 의도에 따라 제대로 구현을 시도했으나 시간초과
즉, 이 문제는 dp를 이용하면 된다

<배워야한 스킬>
1. 각 누적값을 계산하는 방법
2. 답을 구하기 위해 필요한 과정
data 배열은 그대로 값을 입력받고
dp는 가로세로줄이 각각 1개씩 커져서 맨윗줄, 맨왼쪽줄은 0으로 되어야 한다(계산 편해짐)

'''

N, M = map(int,input().split())
data = []
dp = [[0] * (M+1) for _ in range(N+1)]
    
for _ in range(N):
    data.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1,M+1):
        dp[i][j] = data[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    dap = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(dap)
