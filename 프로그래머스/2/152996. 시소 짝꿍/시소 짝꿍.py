def solution(weights): #1, 3/2, 4/3, 2
    answer = 0
    wd = {}
    for w in weights:
        if w in wd:
            wd[w] += 1
        else:
            wd[w] = 1
    
    weights = list(set(weights))
    
    for w in weights:
        answer += (wd[w] * (wd[w]-1))//2
        
        if w*2 in weights:
            answer += wd[w] * wd[w*2]
        
        if w%3==0 and w*4//3 in wd:
            answer += wd[w] * wd[w*4//3]
        
        if w%2==0 and w*3//2 in wd:
            answer += wd[w] * wd[w*3//2]
            
    
    return answer