N = int(input())
M = int(input())

broken = set()
if M > 0:
    broken = set(input().split())

answer = abs(N - 100)

for channel in range(1000001):
    channel_str = str(channel)
    
    for ch in channel_str:
        if ch in broken:
            break
    else:
        presses = len(channel_str) + abs(channel - N)
        answer = min(answer, presses)

print(answer)
