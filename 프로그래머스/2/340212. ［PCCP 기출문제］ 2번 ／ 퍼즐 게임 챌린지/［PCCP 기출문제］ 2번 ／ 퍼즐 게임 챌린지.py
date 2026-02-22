def solution(diffs, times, limit):
    answer = float("inf")
    lo, hi = min(diffs), max(diffs)
    
    while lo <= hi:
        mid = (lo+hi) // 2
        
        t = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                t += times[i]
            else:
                t += (times[i-1]+times[i]) * (diffs[i] - mid) + times[i]
        
        if t <= limit:
            answer = min(answer, mid)
            hi = mid - 1
        else:
            lo = mid + 1
            
    return answer