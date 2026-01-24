ab = input()
a_cnt = 0
l = len(ab)
answer = []
for c in ab:
    if c == 'a':
        a_cnt+=1

ab += ab

for i in range(l):
    temp = 0
    for j in range(a_cnt):
        if ab[i+j] == 'b':
            temp += 1
        
    answer.append(temp)

print(min(answer))