n = int(input())
lst=[]

def push(lst, num):
  lst.append(num)

def pop(lst):
  if not lst:
    print(-1)
  else:
    print(lst.pop(0))

def empty(lst):
  if not lst:
    print(1)
  else:
    print(0)

def size(lst):
  print(len(lst))

def front(lst):
  if not lst:
    print(-1)
  else:
    print(lst[0])

def back(lst):
  if not lst:
    print(-1)
  else:
    print(lst[-1])

for _ in range(n):
  a = input().split()
  if a[0] == 'push':
    push(lst, a[1])
  elif a[0] == 'pop':
    pop(lst)
  elif a[0] == 'size':
    size(lst)
  elif a[0] == 'empty':
    empty(lst)
  elif a[0] == 'front':
    front(lst)
  elif a[0] == 'back':
    back(lst)
  else:
    print("error")
