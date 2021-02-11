for _ in range(int(input())):
    data = input()
    length = len(data.split(' '))
    dap = []
    for i in range(length):
        dap.append(data.split(' ')[i])
    for i in range(length):
        print(dap[i][::-1],end=' ')
    print()
