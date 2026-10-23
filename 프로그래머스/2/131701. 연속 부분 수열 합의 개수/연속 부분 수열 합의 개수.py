def solution(elements):
    answer = 0
    result = set(elements)
    data = list(elements)
    l = len(elements)
    
    for i in range(1, l):
        for j in range(l):
            k = (i + j)%l
            
            data[j] += elements[k]
        result = result | set(data)
    
    answer = len(result)
    return answer