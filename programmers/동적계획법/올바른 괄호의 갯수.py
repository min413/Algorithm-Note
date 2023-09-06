# 올바른 괄호의 갯수
# https://school.programmers.co.kr/learn/courses/30/lessons/12929
# 괄호의 개수가 0인 상태부터 만들어질 개수를 배열에 추가해가면서
# (0쌍, n쌍), (1쌍, n-1쌍), (2쌍, n-2쌍), ... , (n쌍, 0쌍)
# 이렇게 곱해가면서 더하면 된다
def solution(n):
    answer = 0
    dp = [1,1]
    for k in range(2, n+1):
        hap = 0
        for i in range(k):
            hap += dp[i] * dp[k-i-1]
        dp.append(hap)
    answer = dp[n]
    return answer
