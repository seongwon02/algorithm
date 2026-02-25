def solution(n, q, ans):
    answer = 0
    t = set()
    
    def is_clear(idx):
        if idx == len(ans):
            return True
        
        test = q[idx]
        total = 0
        
        for num in test:
            if num in t:
                total += 1
        
        if total == ans[idx]:
            return is_clear(idx+1)
        else:
            return False
        
    for a in range(1, n-3):
        for b in range(a+1, n-2):
            for c in range(b+1, n-1):
                for d in range(c+1, n):
                    for e in range(d+1, n+1):
                        t.clear()
                        t.add(a)
                        t.add(b)
                        t.add(c)
                        t.add(d)
                        t.add(e)
                        
                        if is_clear(0):
                            answer += 1
                        
    return answer