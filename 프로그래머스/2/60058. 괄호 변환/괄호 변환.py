def solution(p):
    answer = ""
    
    def getString(s):
        temp = ""
        if s == "":
            return s
        
        r = 0
        u, v = "", ""
        for i in range(len(s)):
            if s[i] == '(':
                r += 1
            else: 
                r -= 1
            
            if r == 0:
                u = "".join(s[:i+1])
                v = "".join(s[i+1:])
                break
        
        if u[0] == '(':
            temp += u
            temp += getString(v)
        else:
            temp += "("
            temp += getString(v)
            temp += ")"
            
            for j in range(1, len(u)-1):
                if u[j] == '(':
                    temp += ')'
                else:
                    temp += '('
        
        return temp
    
    answer = getString(p)
    return answer
        
            
        
