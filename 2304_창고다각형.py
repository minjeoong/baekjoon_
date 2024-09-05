n = int(input())
lst = []
result = 0

for _ in range(n):
  a, b = map(int, input().split())
  lst.append([a,b])

lst.sort()

# 가장 높은 기둥의 높이
for i in range(n):
  if lst[i][1] > result:
    result = lst[i][1]
    idx = i

height = lst[0][1]
# 왼쪽에서 가장 높은 기둥까지의 넓이
for i in range(idx):
    if height < lst[i+1][1]:
      result += height * (lst[i+1][0] - lst[i][0])
      print("i = %d -> %d * (%d - %d)" % (i, height, lst[i+1][0], lst[i][0]))
      height = lst[i+1][1]
    else: 
      result += height * (lst[i+1][0] - lst[i][0])
      print("i = %d -> %d * (%d - %d)" % (i, height, lst[i+1][0], lst[i][0]))

# 오른쪽에서 가장 높은 기둥까지의 높이
height = lst[-1][1]
for i in range(n-1, idx, -1):
  if height < lst[i-1][1]:
      result += height * (lst[i][0]-lst[i-1][0])
      print("i = %d -> %d * (%d - %d)" % (i, height, lst[i][0], lst[i-1][0]))
      height = lst[i-1][1]
  else:
      result += height * (lst[i][0] - lst[i-1][0])
      print("i = %d -> %d * (%d - %d)" % (i, height, lst[i][0], lst[i-1][0]))
print(result)
