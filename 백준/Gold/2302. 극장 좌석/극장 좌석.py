import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
fixed = []
dp = [0] * (n+1)
dp[0], dp[1] = 1, 1
answer = 1

for _ in range(m):
    t = int(input())
    fixed.append(t)
fixed.append(n+1)
start = 0

def facto(n):
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = facto(n-1) * n
    return dp[n]

for num in fixed:
    end = num - 1
    length = end - start
    
    cnt = 0
    c = 0
    while c * 2 <= length:
        a = length - (c * 2)
        cnt += facto(c + a) // (facto(a) * facto(c))
        c += 1       
    start = end+1
    answer *= cnt
    
print(answer)

