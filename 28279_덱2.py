import sys
from collections import deque

input = sys.stdin.read
deq = deque()

def one (x):
  deq.appendleft(x)

def two(x):
  deq.append(x)

def three ():
  if len(deq) == 0:
    print("-1")
  else:
    print(deq.popleft())
    
def four ():
  if len(deq) == 0:
    print("-1")
  else:
    print(deq.pop())

def five ():
  print(len(deq))

def six ():
  if len(deq) == 0:
    print("1")
  else:
    print('0')

def seven ():
  if len(deq) == 0:
    print('-1')
  else:
    print(deq[0])

def eight ():
  if len(deq) == 0:
    print('-1')
  else:
    print(deq[-1])

data = input().splitlines()
N = int(data[0])

for i in range(1, N+1):
  a = data[i].split()
  if a[0] == '1':
    one(a[1])
  elif a[0] == '2':
    two(a[1])
  elif a[0] == '3':
    three()
  elif a[0] == '4':
    four()
  elif a[0] == '5':
    five()
  elif a[0] == '6':
    six()
  elif a[0] == '7':
    seven()
  elif a[0] == '8':
    eight()
