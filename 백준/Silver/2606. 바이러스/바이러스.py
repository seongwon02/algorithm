import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [i for i in range(n+1)]

def find_root(x):
    if arr[x] == x:
        return x
    else:
        return find_root(arr[x])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    r1 = find_root(a)
    r2 = find_root(b)
    
    if r1 < r2:
        arr[r2] = r1
    else:
        arr[r1] = r2

answer = 0
for i in range(2, n+1):
    if find_root(i) == 1:
        answer += 1
        
print(answer)