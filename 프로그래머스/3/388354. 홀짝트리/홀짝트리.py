from collections import deque

def solution(nodes, edges):
    
    tree = {}
    visited = {}
    answer = [0, 0]
    
    for n in nodes:
        tree[n] = []
        visited[n] = False
    
    for v, w in edges:
        tree[v].append(w)
        tree[w].append(v)
    
    for n in nodes:
        if visited[n]:
            continue
        
        q = deque()
        q.append(n)
        result = [0, 0]
        
        while q:
            v = q.popleft()
            visited[v] = True
            
            if v % 2 == len(tree[v]) % 2:
                result[0] += 1
            else:
                result[1] += 1
            
            for w in tree[v]:
                if not visited[w]:
                    q.append(w)
        
        if result[0] == 1:
            answer[0] += 1
        if result[1] == 1:
            answer[1] += 1
            
    return answer