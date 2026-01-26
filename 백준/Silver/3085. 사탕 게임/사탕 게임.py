n = int(input())
matrix = []

for _ in range(n):
    temp = list(input())
    matrix.append(temp)

answer = 0

def checking(n):
    result = 0
    
    for x in range(n):
        cnt = 1
        for y in range(n-1):
            if matrix[x][y] == matrix[x][y+1]:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
        
        result = max(result, cnt)
        
    
    for x in range(n):
        cnt = 1
        for y in range(n-1):
            if matrix[y][x] == matrix[y+1][x]:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
        result = max(result, cnt)
    return result

answer = max(answer, checking(n))

for i in range(n):
    for j in range(n-1):
        matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
        answer = max(answer, checking(n))
        matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
        
        matrix[j][i], matrix[j+1][i] = matrix[j+1][i], matrix[j][i]
        answer = max(answer, checking(n))
        matrix[j][i], matrix[j+1][i] = matrix[j+1][i], matrix[j][i]
        
print(answer)  
