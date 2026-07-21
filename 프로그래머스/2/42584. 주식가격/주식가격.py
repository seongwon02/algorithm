def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        if not stack:
            stack.append((i, prices[i]))
        else:
            while stack:
                idx, p = stack[-1]
                
                if p <= prices[i]:
                    break
                    
                stack.pop()
                answer[idx] = i - idx
                
            stack.append((i, prices[i]))
    
    while stack:
        idx, _ = stack.pop()
        
        answer[idx] = len(prices) - idx - 1
    
    return answer
                    
                