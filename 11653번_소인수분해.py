#n 이 d로 나눠지면 나누고, 안 나눠지면 d 에 +1 을 하면서 나눠질 때까지 돌림

n = int(input())

d = 2
while d <= n:
  if n % d == 0:
     n= n/d
     print(d)
  else:
    d = d+1