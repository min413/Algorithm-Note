T = int(input())
for _ in range(T):
    N,M = map(int,input().split())  # MCN
    dap = 1 
    imsi = M-N  # M과 N의 차이
    while M > imsi:  # M 부터 1 중에서 imsi,imsi-1, ... 1을 제외
        dap *= M
        M -= 1
    while N > 1:  # N!로 나누기
        dap = dap // N
        N -= 1
    print(dap)
        
        
