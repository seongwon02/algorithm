import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
queue = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
movement = [[0, 0, 1, -1], [1, -1, 0, 0]]
for i in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    
    for j in range(len(tmp)):
        if tmp[j] == 'I':
            queue.append((i, j))
            visited[i][j] = True
    
    arr.append(tmp)

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        dx = x + movement[0][i]
        dy = y + movement[1][i]
        
        if (0 <= dx < n and 0 <= dy < m) and \
            not visited[dx][dy] and arr[dx][dy] != 'X':
            
            if arr[dx][dy] == 'P':
                answer += 1
            
            queue.append((dx, dy))
            visited[dx][dy] = True

if answer == 0:
    print("TT")
else:
    print(answer)
    