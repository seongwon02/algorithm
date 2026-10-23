def solution(n):
    answer = 0
    
    def find(x):
        result = ""
        n = 0
        
        while x > 1:
            if x % 2 == 0:
                result = "0" + result
            else:
                result = "1" + result
                n += 1

            x //= 2
        
        if x == 1:
            result = "1" + result
            n += 1
        
        return result, n
    
    _, cnt = find(n)
    
    while True:
        n += 1
        
        r, k = find(n)

        if cnt == k:
            answer = r
            break

    return int(answer, 2)

