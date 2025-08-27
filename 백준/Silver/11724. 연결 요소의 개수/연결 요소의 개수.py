import sys

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(n)]
visited = [False for _ in range(n)]
answer = 0

def find_root(idx):
    if arr[idx] == idx:
        return idx
    else:
        return find_root(arr[idx])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    left = find_root(a-1)
    right = find_root(b-1)
    
    if left <= right:
        arr[right] = left
    else:
        arr[left] = right

for i in range(n):
        
    if arr[i] == i:
        answer += 1

print(answer)            
