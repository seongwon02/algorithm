import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix =  [[-1 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    
    if matrix[start][end] == -1:
        matrix[start][end] = cost
    else:
        matrix[start][end] = min(cost, matrix[start][end])
    
start, end = map(int, sys.stdin.readline().split())
answer = float("inf")
dist = [float("inf") for _ in range(n+1)]
dist[start] = 0
queue = deque()
queue.append((start, 0))

while queue:
    x, cost = queue.popleft()    
    
    if cost > answer:
        continue
    
    if x == end:
        continue
    
    cities = matrix[x]
    
    for i in range(1, n+1):
        if cities[i] == -1 or  cost + cities[i] >= dist[i]:
            continue
        
        dist[i] = cost + cities[i]
        queue.append((i, cost + cities[i]))

print(dist[end])