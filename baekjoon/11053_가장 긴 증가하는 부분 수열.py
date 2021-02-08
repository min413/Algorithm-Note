n = int(input())
data = list(map(int, input().split()))
dp = [1] * n
for i in range(1, len(data)):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        elif data[j] == data[i]:
            dp[i] = max(dp[i], dp[j])
print(max(dp))



