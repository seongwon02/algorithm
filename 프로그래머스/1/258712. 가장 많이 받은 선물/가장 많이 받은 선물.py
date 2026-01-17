def solution(friends, gifts):
    friendsNum = len(friends)
    friends2id = dict()
    gnt = []
    giftScore = []
    
    for i in range(friendsNum):
        friends2id[friends[i]] = i
        gnt.append([0 for _ in range(friendsNum)])
        giftScore.append(0)
    
    for g in gifts:
        a, b = g.split()
        a2id = friends2id[a]
        b2id = friends2id[b]
        
        gnt[a2id][b2id] += 1
        giftScore[a2id] += 1
        giftScore[b2id] -= 1
    
    answer = [0] * friendsNum
    for i in range(friendsNum):
        for j in range(i+1, friendsNum):
            a = gnt[i][j]
            b = gnt[j][i]
            
            if a > b:
                answer[i] += 1
            elif a < b:
                answer[j] += 1
            else:
                if giftScore[i] > giftScore[j]:
                    answer[i] += 1
                elif giftScore[i] < giftScore[j]:
                    answer[j] += 1
    
    return max(answer)