'''
n을 입력받고 
n x n 크기의 정사각형 공간위에 시작점은 (1,1)
L R U D의 명령어를 공백으로 구분받아 엔터까지 입력받아 수행된 후
도착점 좌표를 줄력하여라 
'''

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
# L(0, -1) R(0, 1) U(-1, 0) D(1, 0)
move = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x,y = nx, ny

print(x,y)


