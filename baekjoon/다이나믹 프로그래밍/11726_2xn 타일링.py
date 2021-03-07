n = int(input())
a = [0] * (n+1)

if n <= 3:
    print(n)
else:
    a[1] = 1
    a[2] = 2
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2]
    dap = a[n] % 10007
    print(dap)

