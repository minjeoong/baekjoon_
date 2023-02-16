from collections import deque
n,k  =map(int,input().split())
deq= deque(i for i in range(1,n+1))
lst = []

while len(deq) > 0 :
  deq.rotate(-(k-1))
  lst.append(deq.popleft())
print("<","".join(str(lst))[1:-1],">", sep="")