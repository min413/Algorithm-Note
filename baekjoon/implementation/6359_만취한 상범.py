T = int(input())
for _ in range(T):
    n = int(input())
    data = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        imsi = i
        while imsi <= n:
            data[imsi] = data[imsi] * (-1)
            imsi += i
    dap = data.count(1) - 1
    print(dap)
