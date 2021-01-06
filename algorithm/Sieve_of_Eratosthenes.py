# 에라토스테네스 : 1부터 N 범위의 모든 소수를 출력

import math

N = 1000
array = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1

for i in range(2, N+1):
    if array[i]:
        print(i, end=' ')
