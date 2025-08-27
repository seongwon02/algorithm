import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

if n > k:
    print(n-k)
elif n == k:
    print(0)
else:
    queue = deque()
    queue.append(n)
    arr = [0 for _ in range(100001)]

    while queue:
        cur = queue.popleft()
        
        if cur == k:
            print(arr[cur])
            break
        
        for i in (cur-1, cur+1, cur*2):
            if 0<=i<=100000 and not arr[i]:
                arr[i] = arr[cur] + 1
                queue.append(i)