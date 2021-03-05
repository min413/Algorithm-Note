n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.reverse()
dap = 0
for i in range(1, len(data)):
    while data[i-1] <= data[i]:
        dap += 1
        data[i] = data[i] - 1
print(dap)
