n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    # 이름은 문자열, 점수는 정수형으로 반환
    array.append((input_data[0], int(input_data[1])))

def setting(data):
    return data[1]
array = sorted(array, key=setting)
# def 부터 setting까지 코드대신 이걸로 써도 됨
# array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
