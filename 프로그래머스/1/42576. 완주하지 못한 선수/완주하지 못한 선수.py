def solution(participant, completion):
    answer = {}
    
    for name in completion:
        if name in answer:
            answer[name] += 1
        else:
            answer[name] = 1
    
    for name in participant:
        if name not in answer:
            return name
        else:
            answer[name] -= 1
    
    for name in completion:
        if answer[name] != 0:
            return name
    
    return None

