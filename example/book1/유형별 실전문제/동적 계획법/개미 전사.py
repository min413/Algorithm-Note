'''

'''

n = int(input())
array = list(map(int, input().split()))

# array가 0부터 첫번째 글짜를 가리키므로 dp도 그냥 100만큼 공간을 할당함
dp = [0] * 100

# dp[0]과 dp[1]까지는 직접 array로 비교하고,
# 2부터는 dp[i-1]와 dp[i-2]+array[i] 중 더 큰거를 넣는다
dp[0] = array[0]
dp[1] = max(array[0],array[1])
for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])
print(dp[n-1])
