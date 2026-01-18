def solution(edges):
    degree = {}
    answer = [0, 0, 0, 0]
    
    for a, b, in edges:
        if a not in degree:
            degree[a] = [0, 0]
        if b not in degree:
            degree[b] = [0, 0]
        
        degree[a][1] += 1
        degree[b][0] += 1
    
    cnt = 0
    for n, d in degree.items():
        if d[0] == 0 and d[1] >= 2:
            answer[0] = n
            cnt = d[1]
        elif d[0] >= 0 and d[1] == 0:
            answer[2] += 1
        elif d[0] >= 2 and d[1] >= 2:
            answer[3] += 1
        
    answer[1] = cnt - answer[2] - answer[3]
    return answer
    