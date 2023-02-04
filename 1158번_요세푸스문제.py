#덱 을 입력받은 수 만큼 차례대로 생성 즉 1 2 3 4 5 6 7 ..
#리스트도 그만큼 생성해주고 
#받은 b 만큼 덱을 순환시켜주고 (-로 하면 왼쪽으로 돌아)
#맨 앞 수 , 즉 맨 왼쪽 수를 지운다 
#지운 수를 리스트에 담아두고 프린트.

from collections import deque
a,b = map(int, input().split())
deq = deque(i for i in range(1,a+1))

lst = [0]*a
for i in range(a):
  deq.rotate(-b)
  pop = deq.pop()
  lst[i] = pop

print("<","".join(str(lst))[1:-1],">", sep="")