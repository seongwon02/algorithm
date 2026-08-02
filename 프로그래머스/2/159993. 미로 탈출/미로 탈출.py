from collections import deque

def solution(maps):
    answer = 0
    movement = [[0, 0, 1, -1], [1, -1, 0, 0]]
    visited = []
    queue = deque()
    x, y = 0, 0
    for i in range(len(maps)):
        temp = []
        for j in range(len(maps[0])):
            temp.append([False, False])
            
            if maps[i][j] == 'S':
                queue.append([i, j, 0, 0])
                x, y = i, j
        visited.append(temp)
    
    step = 0
    visited[x][y][0] = True
    
    while queue:
        x, y, c, cnt = queue.popleft()
        
        if maps[x][y] == 'E' and c == 1:
            answer = cnt
            break
        elif step == 1 and c == 0:
            continue
        
        for i in range(4):
            nx = x + movement[0][i]
            ny = y + movement[1][i]
            
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] != 'X':
                if not visited[nx][ny][c]:
                    visited[nx][ny][c] = True
                
                    if maps[nx][ny] == 'L' and c == 0:
                        step = 1
                        visited[nx][ny][step] = True
                        queue.append([nx, ny, step, cnt+1])
                    else:
                        queue.append([nx, ny, c, cnt+1])
                        
    if answer == 0:
        return -1
    return answer

