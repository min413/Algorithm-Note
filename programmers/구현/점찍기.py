# 점찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107?language=python3
def solution(k, d):
    dots = int(d / k) + 1
    dot_hap = dots
    dist = int(d / k) * k
    
    for i in range(k, d+1, k):
        while(i*i + dist*dist > d*d):
            dots -= 1
            dist -= k
        dot_hap += dots

    answer = dot_hap
    return answer
