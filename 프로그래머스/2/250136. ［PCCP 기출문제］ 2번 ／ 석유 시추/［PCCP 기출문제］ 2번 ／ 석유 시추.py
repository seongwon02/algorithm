from collections import deque

def solution(land):
    answer = 0
    q = deque()
    info = {}
    movement = [[0,0,1,-1], [1,-1,0,0]]

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 0:
                continue
            
            s = set()
            q.append([i, j])
            land[i][j] = 0
            scale = 0

            while q:
                x, y = q.popleft()
                scale += 1
                s.add(y)

                for k in range(4):
                    nx = x + movement[0][k]
                    ny = y + movement[1][k]

                    if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]:
                        land[nx][ny] = 0
                        q.append([nx,ny])


            s = list(s)

            for a in s:
                if a in info:
                    info[a] += scale
                else:
                    info[a] = scale

    return max(info.values())