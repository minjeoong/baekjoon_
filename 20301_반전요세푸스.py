# N, K= map(int, input().split())

# lst = [_ for _ in range(1,N+1)] 
# idx = K - 1
# result = []
# while len(lst) !=0 :

#   if idx < len(lst):
#     result.append(lst.pop(idx))
#     idx += K -1
#   else:
#     idx -= len(lst)

#   # print('idx = %d, lst is %s' % (idx,lst))
  
#   if idx >= (len(lst)+1):
#     idx -= len(lst)

# print("<" + ",".join(map(str, result)) + ">")

# ----------------------------------------------------------------
# 이게 그냥 요세푸스
# from collections import deque

# N, K = map(int, input().split())

# people = deque()
# for i in range(1,N+1): people.append(i)
# result = []

# while people:
#   for _ in range(K-1):
#     people.append(people.popleft())
  
#   result.append(people.popleft())

# print("<" + ", ".join(map(str, result)) + ">")

# ----------------------------------------------------------------
# pypy3 으로 제출하면 정답. Python3 으로 제출하면 시간초과임 

from collections import deque

N, K, M = map(int, input().split())
people = deque(range(1,N+1))

idx = 0

while people:

  if idx // M % 2 == 0:
    for i in range(K-1):
      people.append(people.popleft())
  else:
    for i in range(K):
      people.appendleft(people.pop())
  print(people.popleft())
  idx += 1

