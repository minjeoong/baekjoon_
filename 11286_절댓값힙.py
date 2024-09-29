import sys
import heapq

N = int(input())
max_lst = []
min_lst = []

for i in range(N):
  x = int(sys.stdin.readline())

  if x != 0:
    if x < 0:
      heapq.heappush(max_lst, -x)
    else:
      heapq.heappush(min_lst, x)
  else:
    if min_lst: # 최소힙이 존재
      if max_lst: # 최소힙과 최대힙 존재
        if min_lst[0] < max_lst[0]: # 최소 힙이 더 작으면
          print(heapq.heappop(min_lst))
        else: 
          print(-heapq.heappop(max_lst))
      else: # 최소힙만 존재
        print(heapq.heappop(min_lst))
    elif max_lst: # 최대힙만 존재
      print(-heapq.heappop(max_lst))
    else: # 둘다 없으면
      print(0)
    


