import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
dp = [float("inf")] * (f+1)
q = deque()
q.append((s, 0))
check = False

while q:
    cur, cnt = q.popleft()
    
    if cur == g:
        print(cnt)
        check = True
        break
    
    if cnt >= dp[cur]:
        continue
    
    dp[cur] = cnt
    
    if cur + u <= f:
        q.append((cur+u, cnt+1))
    
    if cur - d > 0:
        q.append((cur-d, cnt+1))

if not check:
    print("use the stairs")