def solution(word):
    answer = 0
    alphabat = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(w, depth):
        nonlocal answer
        
        if w == word:
            return True
        
        for a in alphabat:
            if depth < 5:
                answer += 1
            
                if dfs(w+a, depth+1):
                    return True
            
    dfs('', 0)
    
    return answer
                