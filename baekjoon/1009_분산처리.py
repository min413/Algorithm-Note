
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    array = []
    a %= 10
    imsi = a
    array.append(a)
    for i in range(b):
        a *= imsi
        one = a%10
        if one == imsi:
            break # 끝내버리기
        array.append(one)

    
    index = b % len(array)
    if index == 0:
        index = len(array)
    if array[index-1] == 0:
        print(10)
    else:
        print(array[index-1])
    
        
