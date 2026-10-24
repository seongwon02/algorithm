import heapq

def solution(N, road, K):
    answer = 0
    li = [float("inf")] * (N+1)
    hq = [(0, 1)]
    graph = [[] for _ in range(N+1)]
    
    for x, y, w in road:
        graph[x].append((y, w))
        graph[y].append((x, w))
    
    while hq:
        w, cur = heapq.heappop(hq)
        
        if w >= li[cur]:
            continue
        li[cur] = w
        
        for nxt, nw in graph[cur]:
            heapq.heappush(hq, (w+nw, nxt))
    
    for n in li:
        if n <= K:
            answer += 1

    return answer
