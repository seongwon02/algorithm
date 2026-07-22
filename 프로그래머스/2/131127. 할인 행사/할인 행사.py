def solution(want, number, discount):
    answer = 0
    want_dict = {}
    market_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(10):
        if discount[i] not in market_dict:
            market_dict[discount[i]] = 1
        else:
            market_dict[discount[i]] += 1
    
    
    for i in range(len(discount) - 9):
        if i != 0:
            market_dict[discount[i-1]] -= 1
            
            if discount[i+9] not in market_dict:
                market_dict[discount[i+9]] = 1
            else:
                market_dict[discount[i+9]] += 1
        
        check = True
        for w in want:
            if w not in market_dict or want_dict[w] != market_dict[w]:
                check = False
                break
        
        if check:
            answer += 1
    
    return answer
    