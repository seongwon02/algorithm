def solution(fees, records):
    answer = []
    info = {}
    
    for r in records:
        t, car, x = r.split()
        h, m = map(int, t.split(':'))
        
        if x == 'IN':
            if car not in info:
                info[car] = [0, 60 * h + m, 1] # sum, record, IN(1)
            else:
                info[car] = [info[car][0], 60 * h + m, 1]
        else:
            info[car][0] += (60 * h + m) - info[car][1]
            info[car][2] = 0
    
    cars = []
    for i in info:
        cars.append(i)
        
        if info[i][2] == 1:
            info[i][0] += (60 * 23 + 59) - info[i][1]

    cars.sort()
    for c in cars:
        if info[c][0] <= fees[0]:
            answer.append(fees[1])
        else:
            temp = 0
            
            if (info[c][0] - fees[0]) % fees[2]:
                temp = (info[c][0] - fees[0])//fees[2] + 1
                answer.append(fees[1] + temp * fees[3])
            else:
                temp = (info[c][0] - fees[0])//fees[2]
                answer.append(fees[1] + temp * fees[3])
        
    return answer