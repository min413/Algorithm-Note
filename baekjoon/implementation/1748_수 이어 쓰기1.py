import sys
input = sys.stdin.readline

dap = 0
n = input()
length = len(n) - 1
yes = 0
for i in range(1, length):
    if i == 1: # 한자리수?
        dap += 9
    else: # 두자리수 이상?
        imsi = 10**(i-1)
        dap += i * 9 * imsi
    yes = i

k = 10**(length-1)
dap += (yes+1) * (int(n) - k + 1)
print(dap)
