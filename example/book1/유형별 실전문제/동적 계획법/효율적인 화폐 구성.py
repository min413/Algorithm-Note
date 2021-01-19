'''
n : 화폐 종류 개수
m : 만들어야 할 금액


'''
n,m = map(int, input().split())
array=[]

# 2차원으로 데이터 받는 방법
for i in range(n):
    array.append(int(input()))

# 10000원보다는 큰 금액 중 아무거나 기입
dp = [10001]*(m+1)

dp[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        dp[j] = min(dp[j], dp[j-array[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
