data = []
A, P = map(int,input().split())
data.append(A)
while 1:
    hap = 0
    imsi = str(A)
    for i in imsi:
        hap += int(i) ** P
        
    if hap in data:
        check = hap
        break
    else:
        data.append(hap)
        
    A = hap

for j in range(len(data)):
    if data[j] == check:
        dap = j
        break

print(j)
