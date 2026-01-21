def solution(arr):
    num = {}
    
    for n in arr:
        x = 2
        cnt = 0
        while n > 1:
            while n % x == 0:
                cnt += 1
                n //= x
            
            if x in num:
                if cnt > num[x]:
                    num[x] = cnt
            else:
                num[x] = cnt
            
            x += 1
            cnt = 0
    
    answer = 1
    for n in num:
        answer *= n ** num[n]
    
    return answer