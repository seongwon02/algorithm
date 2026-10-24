def solution(data, col, row_begin, row_end):
    answer = 0
    
    data = sorted(data, key= lambda x: (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        temp = 0
        
        for n in data[i]:
            temp += n % (i+1)
        
        answer = answer ^ temp
        
    return answer