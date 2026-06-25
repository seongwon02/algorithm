from math import gcd

def solution(arrayA, arrayB):
    answer = 1
    
    def find_min_number(arr):
        g = arr[0]
        
        for n in arr[1:]:
            g = gcd(g, n)
        
        return g
    
    def check(arr, a):
        for n in arr:
            if n % a == 0:
                return False
        return True
    
    x = find_min_number(arrayA)
    y = find_min_number(arrayB)
    
    if check(arrayA, y):
        answer = max(answer, y)
    if check(arrayB, x):
        answer = max(answer, x)
    
    if answer == 1:
        return 0
    return answer
