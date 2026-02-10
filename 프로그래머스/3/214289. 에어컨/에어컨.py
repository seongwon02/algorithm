def solution(temperature, t1, t2, a, b, onboard):
    offset = 10
    temperature += offset
    t1 += offset
    t2 += offset
    
    n = len(onboard)
    max_temp = 52
    
    dp = [[float("inf")] * max_temp for _ in range(n)]
    
    dp[0][temperature] = 0
    
    for i in range(n - 1):
        for j in range(max_temp):
            if dp[i][j] == float("inf"):
                continue
            
            if onboard[i] == 1 and not (t1 <= j <= t2):
                continue
            
            if j - 1 >= 0:
                cost = 0
                if j > temperature: cost = 0 
                else: cost = a
                dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j] + cost)

            cost = 0
            if j == temperature: cost = 0 
            else: cost = b
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + cost)
            
            if j + 1 < max_temp:
                cost = 0
                if j < temperature: cost = 0
                else: cost = a
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + cost)

    answer = float("inf")
    for j in range(max_temp):
        if onboard[n-1] == 1 and not (t1 <= j <= t2):
            continue
        answer = min(answer, dp[n-1][j])
        
    return answer