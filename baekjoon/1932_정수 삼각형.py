n = int(input())
data = []
dp = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    dp.append([0]*(i+1))

if n == 1:
    print(max(max(data)))
elif n == 2:
    print(max(data[0][0] + data[1][0], data[0][0] + data[1][1]))
else:
    for i in range(2, n):
        dp[0][0] = data[0][0]
        dp[1][0] = dp[0][0] + data[1][0] 
        dp[1][1] = dp[0][0] + data[1][1]
        for j in range(i+1):
            if j == 0:
                dp[i][0] = dp[i-1][0] + data[i][0]
                
            elif 1 <= j and j <= (i-1):
                dp[i][j] = max(dp[i-1][j-1] + data[i][j], dp[i-1][j] + data[i][j])
                
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + data[i][j]
                
    print(max(max(dp)))

                
        

'''
n=1 이면
그냥 출력하고

n=2 이면
각각 더해서 그 중에 큰 값을 출력하면 된다

n>=3 이면
dp 배열에 각 누적값을 더해간다
맨 왼쪽과 오른쪽은 바로 윗줄의 맨 왼쪽값, 맨 오른쪽값 위치에 있는 dp(누적)값을 해당 원소에 더하여 dp에 다시 저장한다
그외 중간부분들의 원소들은 왼쪽 대각선, 오른쪽 대각선의 누적값과 해당 원소값을 더한 것 중 큰값을 누적값에 더한다
맨 마지막에는 dp 원소 중 가장 큰값을 출력한다

'''
