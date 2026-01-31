n = int(input())
arr = list(map(int, input().split()))
dp = [-1] * n
dp[0] = 0

for i in range(n):
    if dp[i] == -1:
        break
    
    cnt = dp[i] + 1
    for j in range(arr[i]):
        if i+j+1 >= n:
            break
        
        if dp[i+j+1] == -1:
            dp[i+j+1] = cnt
        else:
            dp[i+j+1] = min(cnt, dp[i+j+1])

print(dp[-1])
        