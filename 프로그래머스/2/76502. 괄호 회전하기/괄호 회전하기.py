def solution(s):
    answer = 0
    length = len(s)
    
    for i in range(length):
        stack = []
        check = True
        
        for j in range(length):
            idx = (i + j) % length
            
            if s[idx] in ['[', '{', '(']:
                stack.append(s[idx])
            else:
                if stack:
                    if (s[idx] == ')' and stack[-1] == '(') \
                        or (s[idx] == '}' and stack[-1] == '{') \
                        or (s[idx] == ']' and stack[-1] == '['):
                        stack.pop()
                    else:
                        check = False
                else:
                    check = False
                    
        if check and len(stack) == 0:
            answer += 1
                
    return answer

