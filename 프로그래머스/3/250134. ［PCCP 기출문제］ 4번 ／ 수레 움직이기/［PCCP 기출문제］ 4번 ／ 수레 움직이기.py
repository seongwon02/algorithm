def solution(maze):
    answer = float("inf")
    visited = []
    a, b, c, d = 0 , 0, 0, 0
    movement = [[0,0,1,-1], [1,-1,0,0]]

    for i in range(len(maze)):
        temp = []
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                a, b = i, j
                temp.append([False, False])
            elif maze[i][j] == 2:
                c, d = i, j
                temp.append([False, False])
            elif maze[i][j] == 5:
                temp.append([True, True])
            else:
                temp.append([False, False])
        
        visited.append(temp)

    visited[a][b][0] = True
    visited[c][d][1] = True   
    
    def dfs(rx, ry, bx, by, cnt, answer):
        if cnt >= answer:
            return answer

        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            return cnt
        elif maze[rx][ry] == 3:
            for i in range(4):
                nbx = bx + movement[0][i]
                nby = by + movement[1][i]

                if 0<=nbx<len(maze) and 0<=nby<len(maze[0]) and (nbx != rx or nby != ry) and not visited[nbx][nby][1]:
                    visited[nbx][nby][1] = True
                    answer = min(answer, dfs(rx, ry, nbx, nby, cnt+1, answer))
                    visited[nbx][nby][1] = False
        elif maze[bx][by] == 4:
            for i in range(4):
                nrx = rx + movement[0][i]
                nry = ry + movement[1][i]

                if 0<=nrx<len(maze) and 0<=nry<len(maze[0]) and (nrx != bx or nry != by) and not visited[nrx][nry][0]:
                    visited[nrx][nry][0] = True
                    answer = min(answer, dfs(nrx, nry, bx, by, cnt+1, answer))
                    visited[nrx][nry][0] = False
        else:
            for i in range(4):
                nrx = rx + movement[0][i]
                nry = ry + movement[1][i]

                if 0<=nrx<len(maze) and 0<=nry<len(maze[0]) and not visited[nrx][nry][0]:
                    for j in range(4):
                        nbx = bx + movement[0][j]
                        nby = by + movement[1][j]

                        if 0<=nbx<len(maze) and 0<=nby<len(maze[0]) and not visited[nbx][nby][1] and (nbx != nrx or nby != nry) and (nrx != bx or nry != by or nbx != rx or nby != ry):
                            visited[nrx][nry][0] = True
                            visited[nbx][nby][1] = True
                            answer = min(answer, dfs(nrx, nry, nbx, nby, cnt+1, answer))
                            visited[nrx][nry][0] = False
                            visited[nbx][nby][1] = False
        return answer

    answer = dfs(a,b,c,d,0, answer)

    if answer == float("inf"):
        return 0
    return answer