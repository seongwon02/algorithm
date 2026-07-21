def solution(n, k, cmd):
    answer = ["O"] * n
    stack = []
    up = [i-1 for i in range(n)]
    down = [i+1 for i in range(n)]
    
    for i in range(len(cmd)):
        if cmd[i][0] == 'D':
            _, x = cmd[i].split()
            x = int(x)
            
            for _ in range(x):
                k = down[k]
        elif cmd[i][0] == 'U':
            _, x = cmd[i].split()
            x = int(x)
            
            for _ in range(x):
                k = up[k]
        elif cmd[i][0] == 'C':
            u = up[k]
            d = down[k]
            
            stack.append((k, u, d))
            answer[k] = 'X'
                         
            if d == n:
                k = u
                down[u] = d
            elif u == -1:
                k = d
                up[d] = u
            else:
                k = d
                down[u] = d
                up[d] = u
        elif cmd[i][0] == 'Z':
            idx, u, d = stack.pop()
            answer[idx] = 'O'
            
            if u == -1:
                up[d] = idx
            elif d == n:
                down[u] = idx
            else:
                up[d] = idx
                down[u] = idx
                         
            
    return "".join(answer)
        
