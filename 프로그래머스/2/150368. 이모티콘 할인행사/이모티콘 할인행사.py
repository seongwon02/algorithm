from collections import deque

def solution(users, emoticons):
    answer = []
    cnt = 0
    total = 0
    discount = [0.9, 0.8, 0.7, 0.6]
    q = deque()
    q.append("4"*len(emoticons))
    visited = set()
    visited.add("4"*len(emoticons))
    
    while q:
        d = q.popleft()
        d = list(map(int, list(d)))
        c, t = 0, 0
        
        for p, m in users:
            temp = 0
            
            for i in range(len(emoticons)):
                if d[i]*10 >= p:
                    temp += emoticons[i]*(10-d[i]) // 10
                    
            if m <= temp:
                c += 1
            else:
                t += temp
        
        if c > cnt:
            cnt = c
            total = t
        elif c == cnt and t > total:
            total = t
            
        for i in range(len(d)):
            dc = list(d)

            if dc[i] > 1:
                dc[i]-=1
                dc = "".join(map(str, dc))

                if dc not in visited:
                    q.append(dc)
                    visited.add(dc)
    
    return [cnt, total]