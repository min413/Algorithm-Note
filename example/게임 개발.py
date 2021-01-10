'''
0은 육지, 1은 바다

'''

n,m = map(int,input().split())

d = [[0] * m for _ in range(n)]
# 0(1,1) 0(1,2) 0(1,3) ... 0(1,m)
# ...
# 0(n,1) 0(n,2) 0(n,3) ... 0(n,m)

x,y,direction = map(int, input().split())
d[x][y] = 1
# 1 : 방문함

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    # 왼쪽으로 방향 바꾸기
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 한 후 정면에 육지이자 안 가본 곳이 있다면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        # 방문처리
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        # 만약 4번 돌아도 갈 곳이 없다면?
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            # 뒤가 땅이라면
            x = nx
            y = ny
        else:
            # 뒤가 바다라면
            break
        turn_time = 0

print(cnt)
