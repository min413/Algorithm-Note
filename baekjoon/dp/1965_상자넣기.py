n = int(input())
data = list(map(int,input().split()))
dp = [1] * n

for point in range(n):
    for i in range(point):
        if data[i] < data[point]:
            dp[point] = max(dp[point], dp[i] + 1)
print(max(dp))
