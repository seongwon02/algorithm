def solution(str1, str2):
    answer = 0
    
    s1, s2 = set(), set()
    d1, d2 = {}, {}
    for i in range(len(str1)-1):
        a, b = str1[i], str1[i+1]
        
        if a.isalpha() and b.isalpha():
            t = a.upper()+b.upper()
            s1.add(t)
            
            if t in d1:
                d1[t] += 1
            else:
                d1[t] = 1
    
    for i in range(len(str2)-1):
        a, b = str2[i], str2[i+1]
        
        if a.isalpha() and b.isalpha():
            t = a.upper()+b.upper()
            s2.add(t)
            
            if t in d2:
                d2[t] += 1
            else:
                d2[t] = 1
                
    x = list(s1 & s2)
    y = list(s1 | s2)
    
    if len(x) == 0 and len(y) == 0:
        return 65536
    else:
        u, v = 0, 0
        for w in x:
            u += min(d1[w], d2[w])
        
        for w in y:
            if w in d1 and w in d2:
                v += max(d1[w], d2[w])
            elif w in d1:
                v += d1[w]
            elif w in d2:
                v += d2[w]
        return int(u / v * 65536)
