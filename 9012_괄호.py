n = int(input())
for _ in range(n):
  lst = list(input())
  stack = []
  for i in lst:
    if i == '(':
      stack.append(i)
    elif i ==')':
      if len(stack) !=0 and stack[-1] =='(':
        stack.pop()
      else:
        stack.append(i)
        break
  if len(stack) == 0:
    print("YES")
  else:
    print("NO") 

