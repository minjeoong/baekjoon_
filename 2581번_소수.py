m = int(input())
n = int(input())
lst = []
for i in range(m,n+1):
  if m == 1:
    continue
  for j in range(2,i):
    if i % j == 0 :
      break
  else:
      lst.append(i)

if len(lst) < 1:
  print(-1)
else:
  print(sum(lst))
  print(min(lst))