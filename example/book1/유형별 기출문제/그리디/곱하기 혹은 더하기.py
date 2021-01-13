# 스스로 작성한 코드

array = input()

a = int(array[0])
index = 1

for i in range(len(array) - 1):
    b = int(array[index])
    if a == 0 or b == 0:
        a += b
    else:
        a *= b
    index += 1

print(a)


