def solution(key, lock):
    m, n = len(key), len(lock)
    key1 = [[]for _ in range(4)]
    lock0 = []
    
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                key1[0].append((i,j))
                key1[1].append((j, abs(m-i-1)))
                key1[2].append((abs(m-i-1), abs(m-j-1)))
                key1[3].append((abs(m-j-1), i))
    
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                lock0.append((i, j))
    
    totalLock = len(lock0)
    sLock = set(lock0)
    
    if totalLock == 0:
        return True
    
    for i in range(4):
        for x, y in key1[i]:
            for a, b in lock0:
                dx, dy = a-x, b-y
                cnt = 0
                inner = False
                for c, d in key1[i]:
                    if (c+dx, d+dy) in sLock:
                        cnt += 1
                    elif 0<=c+dx<n and 0<=d+dy<n:
                        inner = True
                        break

                if cnt == totalLock and not inner:
                    return True
    
    return False