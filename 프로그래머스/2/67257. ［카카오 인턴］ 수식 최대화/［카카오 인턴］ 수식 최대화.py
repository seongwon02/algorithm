from itertools import permutations

def solution(expression):
    answer = []
    weightedOp = list(permutations(['+', '-', '*'], 3))
    
    def findOpWeight(op, idx):
        for i in range(3):
            if weightedOp[idx][i] == op:
                return i
    
    for i in range(len(weightedOp)):
        nop = []
        op = []
        temp = ''
        
        for x in expression:
            if x.isdigit():
                temp += x
            else:
                nop.append(int(temp))
                temp = ''
                
                while op:
                    if findOpWeight(op[-1], i) >= findOpWeight(x, i):
                        b = nop.pop()
                        a = nop.pop()
                        o = op.pop()
                        nop.append(a+b if o=='+' else a-b if o=='-' else a*b)
                    else:
                        break
                op.append(x)

        nop.append(int(temp))
        while op:
            b = nop.pop()
            a = nop.pop()
            o = op.pop()
            nop.append(a+b if o=='+' else a-b if o=='-' else a*b)

        answer.append(abs(nop[0]))
    
    return max(answer)