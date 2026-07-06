def solution(dirs):
    answer = 0
    minN, maxN = -5, 5
    x, y = 0, 0
    visited = set()
    
    for d in dirs:
        cx, cy = x, y
        
        if d == 'U' and cy < 5:
            cy += 1
        elif d == 'D' and cy > -5:
            cy -= 1
        elif d == 'R' and cx < 5:
            cx += 1
        elif d == 'L' and cx > -5:
            cx -= 1
        else:
            continue
        
        if ((x, y), (cx, cy)) not in visited and \
            ((cx, cy), (x, y)) not in visited:
            answer += 1
            visited.add(((x, y), (cx, cy)))
            visited.add(((cx, cy), (x, y)))
        
        x, y = cx, cy
    
    return answer