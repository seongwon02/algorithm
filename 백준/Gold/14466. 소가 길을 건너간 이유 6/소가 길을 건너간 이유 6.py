from collections import deque    

n, k, r = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(n)]
ids = [0 for _ in range(n*n)]
movement = [[0,0,1,-1], [1,-1,0,0]]
blocks = {}

for _ in range(r):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    
    p, q = a*n+b, c*n+d
    
    if p in blocks:
        blocks[p].append(q)
    else:
        blocks[p] = [q]
    
    if q in blocks:
        blocks[q].append(p)
    else:
        blocks[q] = [p]

q = deque()
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
    
        q.append((i,j))
        visited[i][j] = True
        
        while q:
            x, y = q.popleft()
            ids[n*x + y] = cnt
            
            for m in range(4):
                dx = x + movement[0][m]
                dy = y + movement[1][m]
                
                if 0<=dx<n and 0<=dy<n and not visited[dx][dy]:
                    
                    if n*x+y in blocks:
                        if n*dx+dy in blocks[n*x+y]:
                            continue
                        
                    q.append((dx, dy))
                    ids[n*dx + dy] = cnt
                    visited[dx][dy] = True
        cnt += 1

groups = {}
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    if ids[n*a+b] in groups:
        groups[ids[n*a+b]] += 1
    else:
        groups[ids[n*a+b]] = 1
if len(groups.keys()) == 1:
    print(0)
else:
    answer = k * (k-1) // 2
    
    for key in groups:
        answer -= groups[key] * (groups[key] - 1) // 2

    print(answer)
    