# 정수삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# dp 중 유명하면서 익숙한 문제
def solution(triangle):
    answer = 0
    tri_len = len(triangle)
    
    for i in range(1, tri_len):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])
    
    answer = max(triangle[tri_len-1])
    return answer
