def solution(targets):
    answer = 0
    sorted_targets = sorted(targets, key = lambda x:x[1])
    start, end = 0, 0
    
    for i, j in sorted_targets:
        if i >= end:
            start = i
            end = j
            answer += 1
        
    return answer