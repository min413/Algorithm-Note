'''
https://www.youtube.com/watch?v=2IkdAk1Loek
여기가 설명 잘 되어 있다


'''

n, k = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in data:
    for j in range(i, k+1):
        dp[j] += dp[j - i]

print(dp[k])
