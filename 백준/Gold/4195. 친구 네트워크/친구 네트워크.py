import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    f = int(input())
    
    ids = [i for i in range(200000)]
    weight = [1] * 200000
    name2id = {}
    idx = 0
    
    def root(x):
        while x != ids[x]:
            x = ids[x]
        
        return x
    
    for _ in range(f):
        n1, n2 = input().rstrip().split()
        
        if n1 not in name2id:
            name2id[n1] = idx
            idx += 1
        
        if n2 not in name2id:
            name2id[n2] = idx
            idx += 1
        
        id1, id2 =  name2id[n1], name2id[n2]
        r1, r2 = root(id1), root(id2)
        
        if r1 == r2:
            print(weight[r1])
        elif weight[r1] >= weight[r2]:
            weight[r1] += weight[r2]
            ids[r2] = r1
            print(weight[r1])
        else:
            weight[r2] += weight[r1]
            ids[r1] = r2
            print(weight[r2])