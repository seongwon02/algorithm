n, s = map(int, input().split())
number = list(map(int, input().split()))

answer = n+1
cnt = 0
total = 0
i, j = 0, 0

while True:
    while total < s and j < n:
        total += number[j]
        j += 1
        cnt += 1
    
    if total < s:
        break
    
    while total >= s and i < j:
        answer = min(answer, cnt)
        cnt -= 1
        total -= number[i]
        i += 1

if answer > n:
    print(0)
else:
    print(answer)