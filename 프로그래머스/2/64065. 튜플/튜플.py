def solution(s):
    s = s[2:-2].split('},{')
    nd = {}
    
    for x in s:
        nums = x.split(',')
        
        for n in nums:
            n = int(n)
            
            if n in nd:
                nd[n] += 1
            else:
                nd[n] = 1
    
    answer = sorted(nd.keys(), key= lambda x: nd[x], reverse = True)
    return answer