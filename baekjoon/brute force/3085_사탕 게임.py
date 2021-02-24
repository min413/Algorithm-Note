'''
max()보다 그냥 if로 크기 비교 후 변수에 직접 넣는게 시간이 더 빠름

'''

import sys
N = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for i in range(N)]
bigger = 0

def row():
    global bigger
    for i in range(N):
        imsi = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                imsi += 1
            else:
                if bigger < imsi:
                    bigger = imsi
                imsi = 1
        if bigger < imsi:
            bigger = imsi

def column():
    global bigger
    for i in range(N):
        imsi = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                imsi += 1
            else:
                if bigger < imsi:
                    bigger = imsi
                imsi = 1
        if bigger < imsi:
            bigger = imsi

for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
            row()
            column()
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]

for i in range(N):
    for j in range(N-1):
        if board[j][i] != board[j+1][i]:
            board[j][i],board[j+1][i] = board[j+1][i],board[j][i]
            row()
            column()
            board[j][i],board[j+1][i] = board[j+1][i],board[j][i]

print(bigger)
