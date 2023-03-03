lst = [0]*5
sum = 0
for i in range(5):
    lst[i] = int(input())
    if lst[i] < 40 :
        lst[i] = 40
    sum += lst[i]
print(sum // 5)