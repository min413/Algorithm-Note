'''
(0,0) (0,2) (0,4) (0,6)
(1,1) (1,3) (1,5) ...
=> i+j가 짝수면 됨
'''

graph = []
dap = 0
for _ in range(8):
    graph.append(list(map(str, input())))

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            if graph[i][j] == 'F':
                dap += 1
print(dap)
