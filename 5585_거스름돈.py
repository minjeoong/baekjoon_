

num = 1000-int(input())

money = [500, 100, 50, 10, 5, 1]
cnt = 0

while True:

  if num == 0:
    break
    
  for i in money:
    if num >= i:
      num -= i
      cnt += 1
      break
    
print(cnt)