def solution(s):
    stack = []
    
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
    
    if stack:
        return 0
    else:
        return 1
    