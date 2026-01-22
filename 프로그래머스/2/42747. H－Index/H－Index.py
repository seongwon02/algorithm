def solution(citations):
    
    cd = {}
    for c in citations:
        if c in cd:
            cd[c] += 1
        else:
            cd[c] = 1
    
    cList = list(cd.keys())
    cList.sort()
    total = len(citations)
    pastNum = 0
    l = min(total, max(citations))
    answer = 0

    for i in range(l+1):
        if total - pastNum >= i and pastNum <= i:
            answer = i
            
            if i in cd:
                pastNum += cd[i]
        else:
            break
            
    return answer