# 과일장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    answer = 0
    
    types = []
    visited = list(0 for i in range(10))
    for i in range(len(score)):
        visited[score[i]] += 1
    
    for i in range(len(visited)):
        if(visited[i] != 0): 
            types.append(i)
    
    types.sort(reverse=True) # types : 값 종류 내림차순
    score.sort()
    
    # score : 모든 사과의 각각 가격들
    # visited : 각 인덱스 => 값 종류, 각 데이터 => 사과 개수
    
    while sum(visited) >= m: # visited 값들의 합이 m보다 크면 계속 진행
        min_price = types[0]
        while sum(visited[min_price:]) < m:
            min_price -= 1
        visited[min_price] -= 1
            
        imsi = min_price
        for _ in range(m - 1):
            while visited[imsi] == 0:
                imsi += 1
            visited[imsi] -= 1
        answer += min_price * m
    
    return answer
