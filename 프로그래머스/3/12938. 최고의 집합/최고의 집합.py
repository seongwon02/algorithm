def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    x = s // n
    y = s % n
    
    for _ in range(n - y):
        answer.append(x)
    
    for _ in range(y):
        answer.append(x+1)
        
    return answer