
# lst  =[]
# MCnt = 0
# LCnt = 0
# while True:
#   a = input()
#   if a == '.':
#     break
#   lst = list(a)
#   for _ in range(len(lst)):
#     if lst[_] == '(':
#       MCnt += 1
#     elif lst[_] == ')':
#       MCnt -= 1
#       if MCnt < 1:
#         break
#     elif lst[_] == '[':
#       LCnt += 1
#     elif lst[_] == ']':
#       LCnt -= 1
#       if LCnt < 1:
#         break
#     print("lst[_] is %s , () is %d [] is %d" % (lst[_], MCnt, LCnt))

#   if MCnt == 0 and LCnt == 0:
#     print("MCnt is %d, LCnt is %d , yes" % (MCnt, LCnt))
#   else:
#     print("MCnt is %d, LCnt is %d , no" % (MCnt, LCnt))
# ----------------------------------------------------------------


while True:
  a = input()
  stack = []
  if a == '.':
    break
  lst = list(a)
  for i in lst:
    if i == '(' or i == '[':
      stack.append(i)
    elif i ==')':
      if len(stack) != 0 and stack[-1] =='(':
        stack.pop()
      else:
        stack.append(i)
        break
    elif i == ']':
      if len(stack) != 0 and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(i)
        break

  if not stack:
    print("yes")
  else:
    print("no")
    


