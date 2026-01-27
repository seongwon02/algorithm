n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+1, dp[j])
            
result = max(dp)
print(result)

stack = []
for i in range(n):
    if dp[n-1-i] == result:
        stack.append(arr[n-1-i])
        result -= 1

while stack:
    print(stack.pop(), end=" ")
