lst = []
while True:
    a = input()
    if a == '0':
        break
    else:
        lst.append(a)
for i in lst:
  check = [char for char in i]
  check = list(map(int,check))
  if check == list(reversed(check)):
    print("yes")
  else:
    print("no")
