from collections import deque
n = int(input())
deq = deque()
for i in range(n):
  a, b, c = map(int,input().split())
  floor = c % a
  room = c // a +1
  if floor == 0:
    floor = a
    room = c//a

  print(floor*100+room,sep="")