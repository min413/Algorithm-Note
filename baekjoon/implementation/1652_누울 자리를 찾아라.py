'''


'''

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str,input())))
    
garo_dap = 0
# 가로
for i in range(N):
    check = 0
    for j in range(N):
        if graph[i][j] == '.':
            check += 1
        else:
            if check >= 2:
                garo_dap += 1
                check = 0
            else:
                check = 0
    if check >= 2:
        garo_dap += 1
    

sero_dap = 0
# 세로
for i in range(N):
    check = 0
    for j in range(N):
        if graph[j][i] == '.':
            check += 1
        else:
            if check >= 2:
                sero_dap += 1
                check = 0
            else:
                check = 0
    if check >= 2:
        sero_dap += 1

print(garo_dap, sero_dap)

