import sys
import heapq

n = int(input())
lst = []

for _ in range(n):
  x = int(sys.stdin.readline())

  if x == 0 :
    if len(lst) != 0:
      print(heapq.heappop(lst))
    else:
      print(0)

  else:
    heapq.heappush(lst, x)