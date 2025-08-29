import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
answer = 0

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

def t1(x, y):
    global n
    global m
    
    a = 0
    if (0<=x<n and 0<=y<m) and \
        (0<=x+1<n and 0<=y+1<m):
        a = arr[x][y] + arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1]
    
    return a

def t2(x, y):
    global n
    global m
    
    a = 0
    b = 0
    
    if (0<=x<n and 0<=y<m) and \
        (0<=x+3<n and 0<=y<m):
        a = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y]
    
    if (0<=x<n and 0<=y<m) and \
        (0<=x<n and 0<=y+3<m):
        b = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x][y+3]
    
    return max(a, b)
    
def t3(x, y):
    global n
    global m
    
    a = b =  c = d = e = f = g = h = 0
    
    if (0<=x<n and 0<=y<m) and \
        (0<=x+2<n and 0<=y+1<m):
        a = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+2][y+1]
        b = arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1]
        c = arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+2][y+1]
        d = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1]
        e = arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1]
        f = arr[x+2][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+2][y+1]
        g = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x][y+1]
        h = arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1] + arr[x][y+1]
        
    
    return max(a, b, c, d, e, f, g, h)

def t4(x, y):
    global n
    global m
    
    a = b  = c = d = e = f = g = h = 0
    
    if (0<=x<n and 0<=y<m) and \
        (0<=x+1<n and 0<=y+2<m):
        a = arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2] + arr[x][y+2]
        b = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y]
        c = arr[x+1][y] + arr[x+1][y+1] + arr[x][y+1] + arr[x][y+2]
        d = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1]
        e = arr[x+1][y] + arr[x+1][y+1] + arr[x][y+1] + arr[x+1][y+2]
        f = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+2]
        g = arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+1][y+2]
        h = arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y+2]
    
    return max(a, b, c, d, e, f, g, h)
 
for i in range(n):
    for j in range(m):
        answer = max(answer, t1(i, j), t2(i, j), t3(i, j), t4(i, j))

print(answer)