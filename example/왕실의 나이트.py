'''
행 : 1~8 / 열 : a~h
L자 형태로만 이동하는 나이트의 위치를 입력받고 (ex. a1)
그 위치에서 나이트가 이동할 수 있는 경우의 수를 출력하여라  

'''

data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1
# ord()는 문자의 아스키 코드 값을 돌려주는 함수
# a는 1, b는 2, c는 3....

moves = [(-2,-1), (-1,-2), (1,-2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

dap = 0
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]

    if 1 <= next_row and next_row <= 8 and 1 <= next_column and next_column <= 8:
        dap += 1

print(dap)
