
lst = []
for _ in range(6):
  lst.append(int(input()))

front = sorted(lst[:4])
back = sorted(lst[4:])

print(sum(front[1:]) + sum(back[1:]))
