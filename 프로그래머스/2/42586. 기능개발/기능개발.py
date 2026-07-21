def solution(progresses, speeds):
    answer = []
    cnt = []
    
    for i in range(len(speeds)):
        if (100-progresses[i]) % speeds[i]:
            days = (100-progresses[i]) // speeds[i] + 1
        else:
            days = (100-progresses[i]) // speeds[i]
        cnt.append(days)
    
    c = cnt[0]
    deploy = 0
    
    for i in range(len(cnt)):
        if c >= cnt[i]:
            deploy += 1
        else:
            answer.append(deploy)
            deploy = 1
            c = cnt[i]
    
    answer.append(deploy)
    
    return answer
