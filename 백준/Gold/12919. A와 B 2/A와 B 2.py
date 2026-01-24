from collections import deque

s = input()
t = input()

q = deque([t])
answer = 0

while q:
    cur = q.popleft()
    
    if len(cur) == len(s):
        if cur == s:
            answer = 1
            break
        continue
    
    if cur[-1] == 'A':
        q.append(cur[:-1])
    
    if cur[0] == 'B':
        q.append(cur[1:][::-1])

print(answer)
