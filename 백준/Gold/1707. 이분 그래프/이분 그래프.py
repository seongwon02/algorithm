import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (v+1)  # 0: 미방문, 1: red, -1: blue
    ok = True

    for i in range(1, v+1):
        if color[i] != 0:
            continue

        q = deque([i])
        color[i] = 1

        while q and ok:
            cur = q.popleft()
            for nxt in graph[cur]:
                if color[nxt] == 0:
                    color[nxt] = -color[cur]
                    q.append(nxt)
                elif color[nxt] == color[cur]:
                    ok = False
                    break

        if not ok:
            break

    print("YES" if ok else "NO")
