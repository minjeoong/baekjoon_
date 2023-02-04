#a,b 범위가 1000이므로 46까지만 범위를 잡고 arr 를 생성하더라도 len(arr)= 1036 임.
#arr = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ... ]


a, b = map(int, input().split())

arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
print(sum(arr[a:b+1]))