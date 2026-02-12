def solution(numbers):
    answer = []
    for num in numbers:
        
        b_num = ""
        
        while num > 1:
            if num % 2 == 0:
                b_num = '0' + b_num
            else:
                b_num = '1' + b_num
            
            num = num // 2
        
        b_num = '1' + b_num
        b_len = len(b_num)
        standard_len = 1
        mul_n = 2
        
        while standard_len < b_len:
            standard_len += mul_n
            mul_n *= 2
        
        while True:
            if standard_len == b_len:
                break
            
            b_num = '0' + b_num
            b_len += 1
        
        def partition(b_num, start, end):
            if start == end:
                return True
            
            mid = (start + end) // 2
            
            lv = partition(b_num, start, mid-1)
            rv = partition(b_num, mid+1, end)
            
            if b_num[mid] == '0':
                if '1' in b_num[start:mid] or '1' in b_num[mid+1:end+1]:
                    return False
            
            return lv and rv
        
        if partition(b_num, 0, b_len - 1):
            answer.append(1)
        else:
            answer.append(0)
                
            
    return answer