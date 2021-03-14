'''
while "반복문이 돌아갈 조건":
    코드들...
    
(처음엔 끝나는 조건을 넣다가 코드가 아예 실행조차 안되어서 당황했음
기본을 까먹지 말자)

'''
data = list(map(int, input().split()))
goal = [1, 2, 3, 4, 5]
check = 1
while data != goal:
    if check == 1:
        if data[0] > data[1]:
            imsi = data[0]
            data[0] = data[1]
            data[1] = imsi
            for i in range(5):
                print(data[i],end=' ')
            print()
            check += 1
        else:
            check += 1
            
    elif check == 2:
        if data[1] > data[2]:
            imsi = data[1]
            data[1] = data[2]
            data[2] = imsi
            for i in range(5):
                print(data[i],end=' ')
            print()
            check += 1
        else:
            check += 1
            
    elif check == 3:
        if data[2] > data[3]:
            imsi = data[2]
            data[2] = data[3]
            data[3] = imsi
            for i in range(5):
                print(data[i],end=' ')
            print()
            check += 1
        else:
            check += 1
            
    elif check == 4:
        if data[3] > data[4]:
            imsi = data[3]
            data[3] = data[4]
            data[4] = imsi
            for i in range(5):
                print(data[i],end=' ')
            print()
            check += 1
        else:
            check += 1
            
    elif check == 5:
        check = 1
        

    
