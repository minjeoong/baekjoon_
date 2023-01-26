import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
  lst = list(input().split())

  if lst[0] =="push_front":
    deq.appendleft(lst[1])

  elif lst[0] == "push_back":
    deq.append(lst[1])

  elif lst[0] == "pop_front":
    if deq:
      print(deq.popleft())
    else:
      print(-1)

  elif lst[0] == "pop_back":
    if deq:
      print(deq.pop())
    else:
      print(-1)

  elif lst[0] == "size":
    print(len(deq))

  elif lst[0] == "empty":
    if deq:
      print(0)
    else:
      print(1)

  elif lst[0] == "front":
    if deq:
      print(deq[0])
    else:
      print(-1)

  elif lst[0] == "back":
    if deq:
      print(deq[-1])
    else:
      print(-1)
