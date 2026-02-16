from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    q = deque()
    matrix = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[False for _ in range(102)] for _ in range(102)]
    movement = [[0,0,1,-1], [1,-1,0,0]]
    characterX, characterY = characterX*2, characterY*2
    itemX, itemY = itemX*2, itemY*2
    
    for r in rectangle:
        a, b, c, d = r[0]*2, r[1]*2, r[2]*2, r[3]*2
        for x in range(a, c+1):
            matrix[x][b] += 1
            matrix[x][d] += 1
        
        for y in range(b, d+1):
            matrix[a][y] += 1
            matrix[c][y] += 1
    
    q.append((characterX, characterY, 0))
    
    
    while q:
        x, y, cnt = q.popleft()

        if x == itemX and y == itemY:
            answer = cnt
            break
        
        visited[x][y] = True
        
        for i in range(4):
            dx = x + movement[0][i]
            dy = y + movement[1][i]

            if matrix[dx][dy] == 0 or visited[dx][dy]:
                continue
            
            if matrix[x][y] > 1:
                inner = False
                
                for r in rectangle:
                    if r[0]*2<dx<r[2]*2 and r[1]*2<dy<r[3]*2:
                        inner = True
                
                if not inner:
                        q.append((dx, dy, cnt+1))
            else:
                q.append((dx, dy, cnt+1))
                
    return answer // 2