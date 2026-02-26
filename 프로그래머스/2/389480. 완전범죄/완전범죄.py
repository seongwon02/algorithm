def solution(info, n, m):
    visited = set()
    def dfs(a, b, n, m, idx, answer):
        if idx == len(info):
            return min(answer, a)
        elif answer <= a:
            return answer
        elif (a, b, idx) in visited:
            return answer
        
        visited.add((a,b,idx))
        
        if b+info[idx][1] < m:
            answer = min(dfs(a, b+info[idx][1], n, m, idx+1, answer), answer)
        
        if a+info[idx][0] < n:
            answer = min(dfs(a+info[idx][0], b, n, m, idx+1, answer), answer)
        
        return answer
    
    answer = dfs(0, 0, n, m, 0, n)
    
    if answer == n:
        return -1
            
    return answer