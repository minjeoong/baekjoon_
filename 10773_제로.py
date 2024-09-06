k = int(input())
lst = []

for i in range(k):
  a = int(input())
  if a == 0:
    lst.pop()
  else:
    lst.append(a)

print(sum(lst))