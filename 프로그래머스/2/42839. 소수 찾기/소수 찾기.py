from itertools import permutations

def solution(numbers):
    nList = list(numbers)
    np = list(permutations(nList, len(numbers)))
    answer = set()
    
    for i in range(len(numbers)):
        np = list(permutations(nList, i+1))
        
        for num in np:
            temp = 0
            for n in num:
                temp = temp * 10 + int(n)
            if temp < 2:
                continue
                
            x = 2
            check = True

            while x*2 <= temp:
                if temp % x == 0:
                    check = False
                    break
                x += 1

            if check:
                answer.add(temp)

    return len(answer)