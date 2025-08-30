import sys
from collections import deque

n = int(sys.stdin.readline())
parents = [i for i in range(n+1)]
linked_nodes = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]
queue = deque()

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    linked_nodes[a].append(b)
    linked_nodes[b].append(a)

queue.append(1)
visited[1] = True

while queue:
    x = queue.popleft()
    
    for node in linked_nodes[x]:
        if not visited[node]:
            visited[node] = True
            parents[node] = x
            queue.append(node)
            
for i in range(2, n+1):
    print(parents[i])    