# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    answer = ''
    X_num = [0 for _ in range(10)]
    Y_num = [0 for _ in range(10)]
    cross = [0 for _ in range(10)]
    
    for i in X:
        X_num[int(i)] += 1
    for i in Y:
        Y_num[int(i)] += 1
    
    
    for i in range(10):
        cross[i] = min(X_num[i], Y_num[i])
    
    if sum(cross) == 0:
        answer += str(-1)
    else:
        only_0 = False
        if cross[0] != 0:
            only_0 = True
        for i in range(1, 10):
            if cross[i] != 0:
                only_0 = False
                break
        if only_0 == True:
            answer += '0'
            return answer
        
        for i in reversed(range(10)):
            if cross[i] != 0:
                for j in range(int(cross[i])):
                    answer += str(i)
        
    return answer
