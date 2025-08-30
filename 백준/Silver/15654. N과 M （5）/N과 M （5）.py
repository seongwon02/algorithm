import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
combi = list(permutations(nums, m))

for answer in combi:
    tmp = list(answer)
    print(*tmp)
        