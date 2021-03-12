data = input()
dap = 10
for i in range(1, len(data)):
    if data[i-1] == data[i]:
        dap += 5
    else:
        dap += 10
print(dap)
