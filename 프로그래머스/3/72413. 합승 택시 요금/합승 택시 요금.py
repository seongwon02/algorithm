import heapq

def solution(n, s, a, b, fares):
    answer = float("inf")
    graph = [[-1 for _ in range(n+1)]for _ in range(n+1)]
    
    for x, y, w in fares:
        graph[x][y] = w
        graph[y][x] = w
        graph[x][x] = 0
        graph[y][y] = 0
        
    def find(start):
        hq = [(0, start)]
        li = [float("inf")]*(n+1)
        
        while hq:
            w, cur = heapq.heappop(hq)
            
            if w < li[cur]:
                li[cur] = w
            else:
                continue
            
            for nxt in range(n+1):
                nw = graph[cur][nxt]
                
                if nw > 0:
                    heapq.heappush(hq, (w+nw, nxt))
        
        return li
    
    li_s, li_a, li_b = find(s), find(a), find(b)
    
    for i in range(1, n+1):
        answer = min(answer, li_s[i] + li_a[i] + li_b[i])
            
    return answer