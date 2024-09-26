n, m = map(int, input().split())

lst = list(map(int, input().split()))

sorted_lst = sorted(lst)

def backtracing(depth):
  if depth == m:
    print(' '.join(map(str, box)))
    return

  for i in range(n):
    if sorted_lst[i] in box:
      continue
    box.append(sorted_lst[i])
    backtracing(depth+1)
    box.pop()
  print('box : ', box)

box = []
backtracing(0)