def solution(board, moves):
    answer = 0
    stack = []
    
    def findN(board, x):
        x -= 1
        n = 0
        
        for i in range(len(board)):
            if board[i][x] != 0:
                n = board[i][x]
                board[i][x] = 0
                
                break
        
        return n
    
    for m in moves:
        n = findN(board, m)
        
        if n == 0:
            continue
            
        if stack:
            if stack[-1] == n:
                stack.pop()
                answer += 2
            else:
                stack.append(n)
        else:
            stack.append(n)
    return answer
