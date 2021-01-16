import sys

data = sys.stdin.readline().rstrip()

dap = []
num = 0

# 알파벳 확인 : 문자열.isalpha()
for i in data:
    if i.isalpha():
        dap.append(i)
    else:
        num += int(i)

dap.sort()

# 만약 숫자가 존재하면 dap뒤에 삽입한다

if num != 0:
    dap.append(str(num))

# 리스트에서 문자열로
print(''.join(dap))
