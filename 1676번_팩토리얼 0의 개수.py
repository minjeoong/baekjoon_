n = int(input())
mn = 1
for i in range(1,n+1):
  mn = mn*i

lst = reversed(list(str(mn)))
count = 0
for i in lst:
  if int(i) == 0:
    count += 1
  else:
    break
print(count)
