from collections import deque

def solution(priorities, location):
    answer = 0
    prior_dict = {}
    for n in priorities:
        if n in prior_dict:
            prior_dict[n] += 1
        else:
            prior_dict[n] = 1
    last = len(priorities)-1
    q = deque(priorities)
    
    while q:
        n = q.popleft()
        
        if n < max(prior_dict):
            q.append(n)
            
            if location == 0:
                location = last
            else:
                location -= 1
            continue
        
        prior_dict[n] -= 1
        if prior_dict[n] == 0:
            prior_dict.pop(n)
        answer += 1
        last -= 1
        
        if location == 0:
            break
        else:
            location -= 1
        
    return answer