def solution(numbers):
    numbers = sorted(numbers, key=lambda x: (str(x)*4)[:4], reverse = True)
    
    numbers = [str(x) for x in numbers]
    if numbers[0] == '0':
        return "0"
    else:
        return "".join(numbers)