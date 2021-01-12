'''
n개 행 / m개 열
각 행에서 가장 작은 수를 각각 뽑아
그 수들중 가장 큰 수를 출력하는 프로그램

'''
n, m = map(int, input().split())

dap = 0

for i in range(n):
    array = list(map(int, input().split()))
    min_value = min(array)
    dap = max(dap, min_value)

print(dap)
