def solution(arr1, arr2):
    answer =[]
    
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            
            arr.append(temp)
        answer.append(arr)
                
    
    return answer