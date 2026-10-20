from collections import deque

def solution(n, computers):
    answer = 0
    q = deque()
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        
        answer += 1
        visited[i] = True
        q.append(i)
    
        while q:
            x = q.popleft()
            
            for j in range(n):
                if computers[x][j] == 1 and x != j and not visited[j]:
                    q.append(j)
                    visited[j] = True
    
    return answer

