'''
A C G T
'''

N, M = map(int, input().split())
data = []
dap1 = ''
dap2 = 0

for _ in range(N):
    data.append(input())

for j in range(M):
    check = [0,0,0,0]
    for i in range(N):
        if data[i][j] == 'A':
            check[0] += 1
        elif data[i][j] == 'C':
            check[1] += 1
        elif data[i][j] == 'G':
            check[2] += 1
        elif data[i][j] == 'T':
            check[3] += 1
    big = max(check)
    dap2 = dap2 + (N - big)
    
    repeat = []
    for k in range(4):
        if check[k] == big:
            repeat.append(k)
    
    if repeat[0] == 0:
        dap1 = dap1 + 'A'
    elif repeat[0] == 1:
        dap1 = dap1 + 'C'
    elif repeat[0] == 2:
        dap1 = dap1 + 'G'
    elif repeat[0] == 3:
        dap1 = dap1 + 'T'

print(dap1)
print(dap2)
        

    
        
