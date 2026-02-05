import sys
import heapq

input = sys.stdin.readline

m, n = map(int, input().split())
matrix = []
mm = [[0,0,1,-1], [1,-1,0,0]]
pq = []
heapq.heappush(pq, (0,0,0))
dp = [[float("inf") for _ in range(m)] for _ in range(n)]

for _ in range(n):
    temp = list(map(int, input().strip()))
    matrix.append(temp)
    
while pq:
    cnt, x, y = heapq.heappop(pq)
    
    if dp[x][y] <= cnt:
        continue
    
    dp[x][y] = cnt
    
    for i in range(4):
        dx = x + mm[0][i]
        dy = y + mm[1][i]
        
        if 0<=dx<n and 0<=dy<m:
            if matrix[dx][dy] == 1:
                heapq.heappush(pq, (cnt+1, dx, dy))
            else:
                heapq.heappush(pq, (cnt, dx, dy))

print(dp[-1][-1])