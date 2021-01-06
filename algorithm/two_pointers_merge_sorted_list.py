# 투 포인터 : 정렬되어 있는 두 리스트의 합집합

N, M = 3,4
a = [1,3,5]
b = [2,4,6,8]

dap = [0] * (N+M)
i = 0
j = 0
k = 0

while i < N or j < M:
    # 리스트 B의 모든 원소 처리됨 or 리스트 A의 원소가 더 작을 때
    if j >= M or (i < N and a[i] <= b[j]):
        # 리스트 A의 원소를 dap 리스트에 옮기기
        dap[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소 처리됨 or 리스트 B의 원소가 더 작을 때
    else:
        # 리스트 B의 원소를 dap 리스트에 옮기기
        dap[k] = b[j]
        j += 1
    k += 1

for i in dap:
    print(i, end=' ')
