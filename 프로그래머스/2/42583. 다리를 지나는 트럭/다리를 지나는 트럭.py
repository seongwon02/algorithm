from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waitting_q = deque(truck_weights)
    crossing_q1 = deque()
    crossing_q2 = deque()
    cur_weight = 0
    cnt = len(truck_weights)
    
    
    while cnt != 0:
        answer += 1
        
        if crossing_q1:
            while crossing_q1:
                w, d = crossing_q1.popleft()
                
                if d == bridge_length:
                    cnt -= 1
                    cur_weight -= w
                else:
                    crossing_q2.append((w, d+1))
        else:
            while crossing_q2:
                w, d = crossing_q2.popleft()
                
                if d == bridge_length:
                    cnt -= 1
                    cur_weight -= w
                else:
                    crossing_q1.append((w, d+1))
                    
        if waitting_q:
            w = waitting_q.popleft()
            if cur_weight + w <= weight:
                if crossing_q1:
                    crossing_q1.append((w, 1))
                else:
                    crossing_q2.append((w, 1))
                
                cur_weight += w
            else:
                waitting_q.appendleft(w)
    
    return answer