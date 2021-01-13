array = input()
cnt_0 = 0
cnt_1 = 0

# 첫번째 문자 처리가 중요

if int(array[0]) == 0:
    cnt_1 += 1
else:
    cnt_0 += 1
    

for i in range(len(array)-1):
    if array[i] != array[i+1]:
        if array[i+1] == '1':
            cnt_0 += 1
        else:
            cnt_1 += 1

print(min(cnt_0, cnt_1))
        
# 백준 1439
