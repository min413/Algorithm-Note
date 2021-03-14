N = int(input())
data = list(map(int, input().split()))
check = [0 for _ in range(101)]
dap = 0
for i in data:
    if check[i] == 0:
        check[i] = 1
    else:
        dap += 1
print(dap)
