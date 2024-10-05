n = int(input())

temp = list(input())

for i in range(n-1):
  lst = list(input())
  for j in range(len(temp)):
    if temp[j] != lst[j]:
      temp[j]= '?'

print(''.join(map(str,temp)))
