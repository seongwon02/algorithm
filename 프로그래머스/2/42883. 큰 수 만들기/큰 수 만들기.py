def solution(number, k):
    number = list(number)
    answer = ''
    i = 0
    
    while i < len(number)-1 and k > 0:
        ni = i+1
        
        if number[i] < number[ni]:
            k -= 1
            number[i] = '-'
            bi = i - 1
            
            while bi >= 0 and k > 0:
                if number[bi] == '-':
                    bi -= 1
                    continue
                
                if number[bi] < number[ni]:
                    number[bi] = "-"
                    k -= 1
                    bi -= 1
                else:
                    break
        
        i += 1
    
    for j in range(len(number)-k):
        if number[j] != '-':
            answer += number[j]
            
    return answer

