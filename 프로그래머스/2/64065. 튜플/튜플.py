def solution(s):
    answer = []
    s = s[2:-2]
    li = s.split('},{')
    tup = set()
    li = sorted(li, key = lambda x: len(x))
    
    for data in li:
        nums = data.split(',')
        
        for n in nums:
            n = int(n)
            if n not in tup:
                answer.append(n)
                tup.add(n)
            
    return answer