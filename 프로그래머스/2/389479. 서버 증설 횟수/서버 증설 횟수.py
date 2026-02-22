from collections import deque
def solution(players, m, k):
    answer = 0
    q = deque()
    server = 0
    
    for p in players:
        if p // m > server:
            for _ in range(p//m - server):
                q.append(k)
                server += 1
                answer += 1
        
        temp = 0
        for _ in range(server):
            s = q.popleft()
            s -= 1
            
            if s > 0:
                q.append(s)
            else:
                temp += 1
        
        server -= temp
                
    return answer