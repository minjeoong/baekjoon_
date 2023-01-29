#a,b 범위가 1000이므로 46까지만 범위를 잡고 arr 를 생성하더라도 len(arr)= 1036 임.
#


a, b = map(int, input().split())

arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
print(arr)
print(sum(arr[a:b+1]))