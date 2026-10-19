
from collections import deque

def solution(cost, hint):
    answer = float('inf')
    q = deque()
    stages = len(cost)

    q.append((0, 0, [0] * stages))

    while q:
        cur, total, h = q.popleft()

        discount = min(h[cur], stages - 1)
        total += cost[cur][discount]

        if cur == stages - 1:
            answer = min(answer, total)
        else:
            q.append((cur + 1, total, h))

            new_h = h.copy()
            new_total = total + hint[cur][0]

            for i in range(1, len(hint[cur])):
                new_h[hint[cur][i] - 1] += 1

            q.append((cur + 1, new_total, new_h))

    return answer
