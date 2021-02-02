'''
n : 문서 개수
m : 몇 번째꺼?

'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    array = list(map(int, input().split()))
    check = [0 for _ in range(n)]
    check[m] = 1 # 찾을 문서 위치

    cnt = 0
    while 1:
        if array[0] == max(array): # 맨 왼쪽 원소가 가장 큰 원소면?
            cnt += 1 # 순위 숫자 갱신
            
            if check[0] != 1 : # 찾으려는 숫자가 아니면?
                del array[0]
                del check[0]
            else: # 찾으려는 숫자가 맞다면?
                print(cnt)
                break # while문 끝내기 (종료)

        else:
            array.append(array[0])
            check.append(check[0])
            del array[0]
            del check[0]
            
