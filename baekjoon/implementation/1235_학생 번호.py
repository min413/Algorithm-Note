'''


'''
N = int(input())
data = []
for _ in range(N):
    data.append(input())
    
length = len(data[0])
for i in range(length): # 원소의 길이 
    check = [] # 잘라낸 것 보관
    for j in range(len(data)): # 원소 개수
        imsi = data[j]
        check.append(imsi[length-1-i:])
    my_set = set(check)
    my_list = list(my_set)
    if len(my_list) == len(data):
        break

print(i+1)
