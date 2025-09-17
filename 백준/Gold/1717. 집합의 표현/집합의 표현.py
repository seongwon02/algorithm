import sys

def find_root(a):
    while a != parents[a]:
        a = parents[a]
    return a

def connect(a, b):
    return find_root(a) == find_root(b) 

def union(a, b):
    ra = find_root(a)
    rb = find_root(b)
    
    if ra == rb:
        return
    elif weights[ra] >= weights[rb]:
        parents[rb] = ra
        weights[ra] += weights[rb]
    else:
        parents[ra] = rb
        weights[rb] += weights[ra]
    
    return

n, m = map(int, sys.stdin.readline().split())

parents = [i for i in range(n+1)]
weights = [1 for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 0:
        union(b, c)
    else:
        if connect(b, c):
            print("YES")
        else:
            print("NO")