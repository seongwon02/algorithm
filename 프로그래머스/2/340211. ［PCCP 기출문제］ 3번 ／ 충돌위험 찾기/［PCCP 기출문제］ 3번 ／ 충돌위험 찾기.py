from collections import deque

def solution(points, routes):
    answer = 0
    robot_count = len(routes)
    q = deque()
    pos = {}
    
    for i in range(robot_count):
        j = routes[i][0] - 1
        q.append((points[j][0], points[j][1], i, 1))
    
    while q:
        temp = len(q)
        
        for _ in range(temp):
            x, y, robot, d = q.popleft()

            if (x, y) in pos:
                pos[(x, y)] += 1
            else:
                pos[(x, y)] = 1

            target = routes[robot][d]-1

            if x == points[target][0] and y == points[target][1]:
                d += 1
                if d >= len(routes[0]):
                    continue

                target = routes[robot][d] - 1

            if x < points[target][0]:
                x += 1
            elif x > points[target][0]:
                x -= 1
            elif y < points[target][1]:
                y += 1
            elif y > points[target][1]:
                y -= 1
            
            q.append((x, y, robot, d))
        
        for k in pos:
            if pos[k] > 1:
                answer += 1
        
        pos.clear()
        
    return answer