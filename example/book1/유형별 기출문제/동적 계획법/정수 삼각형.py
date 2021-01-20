'''
https://www.acmicpc.net/problem/1932

'''
n = int(input())
dp = []
for _ in range(n):
    # dp에 하나씩 추가
    dp.append(list(map(int, input().split())))

    for i in range(1,n):
        for j in range(i+1):
            # from 왼쪽 위
            if j == 0:
                up_left = 0
            else:
                up_left = dp[i-1][j-1]

