'''
dp[n][0] : A 개수
dp[n][1] : B 개수

'''

k = int(input())
dp = [[0 for _ in range(2)] for _ in range(46)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, 46):
    dp[i][0] = dp[i-1][1] - dp[i-1][0] + dp[i-1][0]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]
print(dp[k][0], dp[k][1])
