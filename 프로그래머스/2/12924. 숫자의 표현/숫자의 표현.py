def solution(n):
    answer = 0
    head, tail, cur = 0, 0, 0
    
    while True:
        if head == n and head == n:
            break
        
        if cur == n:
            answer += 1
            head += 1
            cur -= head
        if cur < n:
            tail += 1
            cur += tail
        elif cur > n:
            head += 1
            cur -= head
    
    return answer