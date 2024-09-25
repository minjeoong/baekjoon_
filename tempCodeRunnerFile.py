from collections import deque
n = int(input())
lst = deque()


for i in range(n):
  x = int(input())

  if x == 0:
    if len(lst) == 0:
      print(0)
    else:
      print(max(lst))
      lst.remove(max(lst))
  else: 
    lst.append(x)
