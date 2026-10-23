def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    skill_set = set(skill)
    
    for s in skill_trees:
        j = 0
        clear = True
        
        for c in s:
            if c in skill_set:
                if c == skill[j]:
                    j += 1
                else:
                    clear = False
                    break
        
        if clear:
            answer += 1
            
    return answer