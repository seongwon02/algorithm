import heapq

def solution(operations):
    answer = []
    data1 = [] # 최소힙
    data2 = [] # 최대힙
    nd = dict()
    
    def find_min(data, nd):
        while len(data) > 0:
            n = heapq.heappop(data)
            nd[n][0] -= 1

            if nd[n][0] < nd[n][1]:
                nd[n][0] += 1
                heapq.heappush(data, n)
                return n
        
        return 0
    
    def find_max(data, nd):
        while len(data) > 0:
            n = -heapq.heappop(data)
            nd[n][1] -= 1

            if nd[n][1] < nd[n][0]:
                nd[n][1] += 1
                heapq.heappush(data, -n)
                return n
        
        return 0
    
    for op in operations:
        p, num = op.split(" ")
        num = int(num)
        
        if p == 'I':
            heapq.heappush(data1, num)
            heapq.heappush(data2, -num)
            
            if num in nd:
                nd[num][0] += 1
                nd[num][1] += 1
            else:
                nd[num] = [1, 1]
        else:
            if num == 1:
                find_max(data2, nd)
                
                if len(data2):
                    n = -heapq.heappop(data2)
                    nd[n][1] -= 1
            else:
                find_min(data1, nd)
                
                if len(data1):
                    n = heapq.heappop(data1)
                    nd[n][0] -= 1
    
    a = find_min(data1, nd)
    if len(data1) == 0:
        return [0, 0]
    
    b = find_max(data2, nd)
    return [b, a]