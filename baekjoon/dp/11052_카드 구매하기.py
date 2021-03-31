'''

dp[2] = dp[1] + data[1] , d[0] + data[2]
dp[3] = dp[2] + data[1] , dp[1] + data[2] , dp[0] + data[3]
.
.
.

'''
 
n = int(input())
dp = [0 for _ in range(n+1)]
data = list(map(int, input().split()))
data = [0] + data
dp[1] = data[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + data[j]:
            dp[i] = dp[i - j] + data[j]
print(dp[n])
