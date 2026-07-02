def solution(N, stages):
    answer = []    
    counts = [0]*(N+1)
    fails = {}
    total = len(stages)
    
    for s in stages:
        counts[s-1] += 1
    
    for i in range(N):
        if counts[i] == 0:
            fails[i+1] = 0
        else:
            fails[i+1] = counts[i] / total
            total -= counts[i]
    
    answer = sorted(fails, key= lambda x: fails[x], reverse= True)
    
    return answer
    