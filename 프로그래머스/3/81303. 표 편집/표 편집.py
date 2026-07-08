def solution(n, k, cmd):
    answer = ["O"] * n
    updown = [[i-1, i+1] for i in range(n)]
    stack = []
    
    for p in cmd:
        if p[0] == 'U':
            _, x = p.split(' ')
            for _ in range(int(x)):
                k = updown[k][0]
        elif p[0] == 'D':
            _, x = p.split(' ')
            
            for _ in range(int(x)):
                k = updown[k][1]
        elif p[0] == 'C':
            stack.append(k)
            answer[k] = 'X'
            
            prev = updown[k][0]
            nxt = updown[k][1]
            
            if prev != -1:
                updown[prev][1] = nxt
            if nxt != n:
                updown[nxt][0] = prev
                
            if nxt == n:
                k = prev
            else:
                k = nxt
                
        elif p[0] == 'Z':
            r = stack.pop()
            answer[r] = 'O'
            
            prev = updown[r][0]
            nxt = updown[r][1]
            
            if prev != -1:
                updown[prev][1] = r
            
            if nxt != n:
                updown[nxt][0] = r
            
    return "".join(answer)
        
