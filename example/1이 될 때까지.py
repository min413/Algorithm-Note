'''
n이 1이 될 때까지 두 과정 중 하나를 선택하여 반복 수행된다
1. n에서 1 빼기
2. n을 k로 나누기 (n이 k로 나누어 떨어질때)
이때 연산이 수행되는 최소 횟수를 구하여라

'''

n, k = map(int, input().split())
cnt = 0
while True:
    if n % k == 0:
        n = int(n/k)
        cnt = cnt + 1
    else:
        n = n - 1
        cnt = cnt + 1
    print(n)
    print(cnt)
    if n == 1: break

print(cnt)
