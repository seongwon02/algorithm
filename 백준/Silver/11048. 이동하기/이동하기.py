n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(1, n):
    matrix[i][0] += matrix[i-1][0]

for j in range(1, m):
    matrix[0][j] += matrix[0][j-1]
    
for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] += max(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
        
print(matrix[-1][-1])