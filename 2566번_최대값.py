arr =[]
for i in range(9):
  arr.append(list(map(int, input().split())))
a = max(map(max, arr))
print(a)
cnt=0
for k in range(9):
    for j in range(9):
        if arr[k][j] == a and cnt == 0:
            print(k+1, j+1)
            cnt += 1