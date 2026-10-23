from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0, set()))
    
    while q:
        w, cnt, s = q.popleft()
        
        if w == target:
            answer = cnt
            break
            
        for i in range(len(words)):
            if i in s:
                continue
            
            n = 0
            for j in range(len(words[i])):
                if w[j] != words[i][j]:
                    n += 1
                
            if n <= 1:
                s.add(i)
                q.append((words[i], cnt+1, s))
    
    return answer