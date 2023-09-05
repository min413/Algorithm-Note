
# 무인도여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solution(maps):
    visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))]
    hap = 0
    answer = []
    
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                hap = int(maps[i][j])
                visited[i][j] = 1
                
                queue = deque()
                queue.append((i,j))
                
                while queue:
                    x,y = queue.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        
                        
                        if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                            continue
                        
                        if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                            hap += int(maps[nx][ny])
                            visited[nx][ny] = 1
                            queue.append((nx,ny))
                answer.append(hap)
    
    answer.sort()
    if not answer:
        answer.append(-1)
        
    return answer
