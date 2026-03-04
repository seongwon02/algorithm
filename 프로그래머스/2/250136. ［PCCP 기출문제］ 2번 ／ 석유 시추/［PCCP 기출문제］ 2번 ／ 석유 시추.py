import sys
sys.setrecursionlimit(1000000)

def solution(land):
    n = len(land)
    m = len(land[0])
    answer = [0 for _ in range(m)]
    movement = [[0,0,1,-1], [1,-1,0,0]]
    oil_land = set()
    
    def find_oil(x, y):
        if land[x][y] == 0:
            return 0
        
        land[x][y] = 0
        total = 1
        oil_land.add(y)
        
        for i in range(4):
            nx = x + movement[0][i]
            ny = y + movement[1][i]
            
            if 0<=nx<len(land) and 0<=ny<len(land[0]):
                total += find_oil(nx, ny)
        
        return total
            
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                continue
            
            total = find_oil(i, j)
            
            for k in oil_land:
                answer[k] += total
            
            oil_land.clear()
    
    return max(answer)