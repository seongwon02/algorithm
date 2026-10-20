from collections import deque

def solution(board):
    n = len(board)

    costs = [[[float("inf")] * 4 for _ in range(n)] for _ in range(n)]

    q = deque()
    movement = [[-1, 1, 0, 0], [0, 0, -1, 1]]

    costs[0][0][1] = 0
    costs[0][0][3] = 0

    q.append((0, 0, 0, 1))
    q.append((0, 0, 0, 3))

    while q:
        x, y, total, m = q.popleft()

        if total != costs[x][y][m]:
            continue

        for i in range(4):
            nx = x + movement[0][i]
            ny = y + movement[1][i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:

                if (m == 0 and i == 1) or \
                   (m == 1 and i == 0) or \
                   (m == 2 and i == 3) or \
                   (m == 3 and i == 2):
                    continue

                if m == i:
                    new_cost = total + 100
                else:
                    new_cost = total + 600

                if new_cost < costs[nx][ny][i]:
                    costs[nx][ny][i] = new_cost
                    q.append((nx, ny, new_cost, i))

    return min(costs[-1][-1])