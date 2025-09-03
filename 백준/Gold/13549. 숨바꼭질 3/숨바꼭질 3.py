import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
queue.append((n, 0))
dp = [float("inf") for _ in range(k+1)]

while queue:
    pos, sec = queue.popleft()
    
    if sec >= dp[k]:
        continue
    
    if pos < k:
        if pos == 0:
            if sec + 1 < dp[1]:
                dp[1] = sec + 1
                queue.append((pos+1, sec + 1))       
        else:
            if sec + 1 < dp[pos + 1]:
                dp[pos + 1] = sec + 1
                queue.append((pos + 1, sec + 1))
            
            if sec + 1 < dp[pos - 1]:
                dp[pos - 1] = sec + 1
                queue.append((pos - 1, sec + 1))
            
            if pos * 2 > k:
                dp[k] = min(dp[k], sec + (pos * 2) - k)
            elif pos * 2 <= k and sec < dp[pos * 2]:
                dp[pos * 2] = sec
                queue.append((pos * 2, sec))    
    elif pos > k:
        dp[k] = min(dp[k], sec + pos - k)
    else:
        dp[k] = min(dp[k], sec)

print(dp[k])