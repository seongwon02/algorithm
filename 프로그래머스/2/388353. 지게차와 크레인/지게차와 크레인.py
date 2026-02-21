from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    matrix = [['.'] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            matrix[i+1][j+1] = storage[i][j]
            
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
    for r in requests:
        target = r[0]
        
        if len(r) == 1: 
            visited = [[False] * (m + 2) for _ in range(n + 2)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            to_remove = []
            
            while queue:
                cx, cy = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    
                    if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visited[nx][ny]:
                        if matrix[nx][ny] == '.':
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                        elif matrix[nx][ny] == target:
                            visited[nx][ny] = True 
                            to_remove.append((nx, ny))
                            
            for x, y in to_remove:
                matrix[x][y] = '.'
                
        else: 
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if matrix[i][j] == target:
                        matrix[i][j] = '.'
                        
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] != '.':
                answer += 1
                
    return answer