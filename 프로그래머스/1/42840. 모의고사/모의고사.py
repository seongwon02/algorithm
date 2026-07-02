def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    a1,a2,a3 = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            a1 += 1
        
        if answers[i] == s2[i%8]:
            a2 += 1
        
        if answers[i] == s3[i%10]:
            a3 += 1

    n = max(a1, a2, a3)
    
    if a1 == n:
        answer.append(1)
    if a2 == n:
        answer.append(2)
    if a3 == n:
        answer.append(3)
    
    return answer