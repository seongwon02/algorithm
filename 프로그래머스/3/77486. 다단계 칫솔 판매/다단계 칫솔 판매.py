def solution(enroll, refreal, seller, amount):
    info = {}
    answer = []
    
    for i in range(len(enroll)):
        info[enroll[i]] = [0, refreal[i]]
    
    for i in range(len(amount)):
        s = seller[i]
        money = amount[i] * 100
        
        while True:
            if s == '-' or money == 0:
                break
            
            temp = money // 10
            info[s][0] += money - temp
            money = temp
            s = info[s][1]
    
    for e in enroll:
        answer.append(info[e][0])
    
    return answer

       
