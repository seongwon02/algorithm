def solution(stones, k):

    left = 1
    right = max(stones)
    
    def isCross(n, k):
        cnt = 0
        
        for i in range(len(stones)):
            if stones[i] <= n:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                return False
        return True
    
    while left <= right:
        mid = (left + right) // 2
        
        if isCross(mid, k):
            left = mid + 1
        else:
            right = mid - 1
        
    return max(left, right)