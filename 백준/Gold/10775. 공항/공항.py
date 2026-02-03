import sys

input = sys.stdin.readline
g = int(input())
p = int(input())

airline = [i for i in range(g+1)]
cnt = 0

def root(x):
    while x != airline[x]:
        x = airline[x]
    return x

for _ in range(p):
    x = int(input())
    
    r = root(x)
    
    if r == 0:
        break
    
    cnt += 1
    airline[r] = r-1
    airline[x] = r-1

print(cnt)