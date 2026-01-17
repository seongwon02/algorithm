def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y, num, t = -1, 0, 1, 0
    
    for i in range(n):
        for j in range(i, n):            
            if t % 3 == 0:
                x += 1
            elif t % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            arr[x][y] = num
            num += 1
        t += 1
    
    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])
                
    return answer