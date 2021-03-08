N,M = map(int,input().split())
dap = min(N,M) - 1
dap = dap + (max(N,M) - 1) * min(N,M)
print(dap)
