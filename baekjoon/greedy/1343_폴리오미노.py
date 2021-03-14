'''
1 <=length <=3 일 때 코드가 조금 걸리지만 어쨌든 잘 돌아간다

'''
data = input()
data = list(data)
length = len(data)

if length >= 4:
    for i in range(length-3):
        if data[i] == 'X':
            if data[i:i+4] == ['X', 'X', 'X', 'X']:
                for j in range(i, i+4):
                    data[j] = 'A'
            elif data[i:i+2] == ['X', 'X']:
                for j in range(i, i+2):
                    data[j] = 'B'

    for i in range(length-3, length-1):
        if data[i] == 'X' and data[i+1] == 'X':
            for j in range(i, i+2):
                data[j] = 'B'
else:
    if length == 2:
        if data[0] == 'X' and data[1] == 'X':
            data[0] = 'B'
            data[1] = 'B'
    elif length == 3:
        if data[0] == 'X' and data[1] == 'X' and data[2] == '.':
            data[0] = 'B'
            data[1] = 'B'
            
        elif data[0] == '.' and data[1] == 'X' and data[2] == 'X':
            data[1] = 'B'
            data[2] = 'B'
            
if 'X' in data:
    print(-1)
else:
    print(''.join(data))
