'''
n : 행 / m : 열
'''

# 테스트케이스 수만큼만 프로그램 돌아가기
for T in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # array 배열을 m개 단위로 2차원 테이블 만들기
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    # j를 1부터 m-1까지 (열)
    for j in range(1, m):
        # i를 0부터 n-1까지 (행)
        for i in range(n):
            # 왼쪽 위에서 올 때
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽에서 올 때
            left = dp[i][j-1]
            # 왼쪽 아래에서 올 때
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 이제 모든 경우의 left 종류가 모아졌으므로
            # dp 값 업데이트
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    dap = 0
    for i in range(n):
        result = max(dap, dp[i][m-1])

    print(result)
