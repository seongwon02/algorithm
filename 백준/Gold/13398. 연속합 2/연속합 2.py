n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp2 = [0] * n

if n == 1:
    print(arr[0])
else:
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], arr[i] + dp[i-1])


    dp2[0], dp2[1] = dp[0], dp[1]
    for j in range(2, n):
        if arr[j-1] < 0:
            dp2[j] = max(arr[j], arr[j] + dp2[j-1], arr[j] + dp[j-2])
        else:
            dp2[j] = max(arr[j], arr[j] + dp2[j-1])
    print(max(dp2))