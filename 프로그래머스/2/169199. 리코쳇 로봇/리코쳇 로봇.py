from collections import deque

def solution(board):
    answer = -1
    q = deque()
    movement = [[0,0,1,-1], [1,-1,0,0]]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                q.append([i, j, 0])
    
    while q:
        x, y, cnt = q.popleft()
        
        if board[x][y] == 'G':
            answer = cnt
            break
        
        for i in range(4):
            nx = x + movement[0][i]
            ny = y + movement[1][i]
            
            
            while True:
                if not (0<=nx<len(board) and 0<=ny<len(board[0])) or board[nx][ny] == 'D':
                    nx -= movement[0][i]
                    ny -= movement[1][i]
                    break
                else:
                    nx += movement[0][i]
                    ny += movement[1][i]
            
            if not visited[nx][ny]:
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = True
                
    return answer