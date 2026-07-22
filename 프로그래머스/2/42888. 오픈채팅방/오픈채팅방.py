def solution(record):
    result = []
    user = {}
    n = 0
    
    for r in record:
        command = r.split()
        
        if command[0] == 'Enter':
            uid, nickname = command[1], command[2]
            if uid not in user or user[uid] != nickname:
                user[uid] = nickname
            result.append(uid)
        elif command[0] == 'Leave':
            uid = command[1]
            result.append(uid)
        elif command[0] == 'Change':
            uid, nickname = command[1], command[2]
            user[uid] = nickname
    
    for r in record:
        command = r.split()
        uid = command[1]
        
        if command[0] == 'Enter':
            result[n] = user[uid] + "님이 들어왔습니다."
            n += 1
        elif command[0] == 'Leave':
            result[n] = user[uid] + "님이 나갔습니다."
            n += 1
    
    return result
                