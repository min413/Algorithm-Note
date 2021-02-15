n, a, b = map(int, input().split())
dap = 0
while a != b:
    dap += 1
    if a%2 == 0:
        a = a/2
    elif a%2 != 0:
        a = (a+1)/2
    if b%2 == 0:
        b = b/2
    elif b%2 != 0:
        b = (b+1)/2
print(dap)
