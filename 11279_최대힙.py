# from collections import deque
# # import sys
# # input = sys.stdin.readlines
# n = int(input())
# lst = deque()


# for i in range(n):
#   x = int(input())

#   if x == 0:
#     if len(lst) == 0:
#       print(0)
#     else:
#       print(max(lst))
#       lst.remove(max(lst))
#   else: 
#     lst.append(x)

# ----------------------------------------------------------------

# Python의 heapq는 최소 힙만 지원하기 때문에, 최대 힙을 구현하려면 음수로 변환하여 값을 저장하고 삭제할 때 다시 양수로 변환해야 합니다.

import sys
import heapq
n = int(input())
lst = []


for i in range(n):
  x = int(sys.stdin.readline())

  if x == 0:
    if len(lst) == 0:
      print(0)
    else:
      print(-heapq.heappop(lst))

  else: 
    heapq.heappush(lst, -x)
