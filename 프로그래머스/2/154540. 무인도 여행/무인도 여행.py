from collections import deque

def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    movement = [[0,0,1,-1], [1,-1,0,0]]
    answer = []

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        total_num = 0
        visited[x][y] = True

        while q:
            a, b = q.popleft()
            total_num += int(maps[a][b])

            for i in range(4):
                dx = a + movement[0][i]
                dy = b + movement[1][i]

                if 0<=dx<len(maps) and 0<=dy<len(maps[0]) \
                    and maps[dx][dy] != 'X' and not visited[dx][dy]:
                    visited[dx][dy] = True
                    q.append((dx, dy))

        return total_num

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X' or visited[i][j]:
                continue

            answer.append(bfs(i, j))

    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer