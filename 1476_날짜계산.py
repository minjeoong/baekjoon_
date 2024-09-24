E, S, M = map(int, input().split(" "))

e, s, m = 0, 0, 0
result = 0

while True:
  if E == S == M:
    print(E)
    break

  e += 1
  s += 1
  m += 1
  result += 1

  if e > 15:
    e = 1
  if s > 28:
    s = 1
  if m > 19:
    m = 1
  
  if e == E and s == S and m == M:
    print(result)
    break