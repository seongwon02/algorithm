import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = []
chicken = []
house = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)
    
    for j in range(n):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chicken.append([i, j])

combChicken = combinations(chicken, m)
answer = float("inf")

for c in combChicken:
    tmp = 0
    
    for h in house:
        dist = float("inf")
        
        for j in range(m):
            dist = min(dist, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))

        tmp += dist
    answer = min(answer, tmp)
        
print(answer)
    