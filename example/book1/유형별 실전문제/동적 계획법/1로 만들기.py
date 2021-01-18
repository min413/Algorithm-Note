'''

'''

data = int(input())

d = [0] * 30001

# range(시작숫자, 종료숫자, step)
for i in range(2, data+1):
    # 현재 수에서 1 뺄 때
    d[i] = d[i-1] + 1

    # 현재 수가 2로 나누어 떨어질 때 
    if i%2 == 0:
        d[i] = min(d[i],d[i//2] + 1)


    # 현재 수가 3으로 나누어 떨어질 때
    if i%3 == 0:
        d[i] = min(d[i],d[i//3] + 1)

    # 현재 수가 5로 나누어 떨어질 때 
    if i%5 == 0:
        d[i] = min(d[i],d[i//5] + 1)

print(d[data])
