def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        if not stack:
            stack.append((i, prices[i]))
        else:
            while stack:
                if stack[-1][1] > prices[i]:
                    idx, p = stack.pop()
                    answer[idx] = i - idx
                else:
                    break
                    
            stack.append((i, prices[i]))
    
    while stack:
        idx, p = stack.pop()
        answer[idx] = len(prices) - idx - 1
        
    return answer
                    
                