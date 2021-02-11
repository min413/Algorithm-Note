n,m = map(int, input().split())
data =[]
for _ in range(n):
    data.append(list(map(int, input())))
dap = 1
for i in range(n-1):
    for j in range(m-1):
        k = 1
        while 1:
            if (i+k) == n or (j+k) == m:
                break
            if data[i][j] == data[i+k][j] and data[i][j] == data[i][j+k] and data[i][j] == data[i+k][j+k]:
                dap = max(dap, (k+1)*(k+1))
            k += 1
print(dap)

'''
어떤 직사각형이 입력되든 가장 작은 정사각형 값은 1이므로
최종 답을 담는 변수 dap을 1로 초기화한다

직사각형에서 마지막 행,열을 제외한 모든 부분에서 범위를 넘어가지 않는 자연수만큼 행,열,행과 열을 더한 직사각형 원소와 같은지 확인한다
만약 같다면 기존 dap과 새로운 정사각형의 넓이 중 큰 수를 dap에 저장한다

'''


