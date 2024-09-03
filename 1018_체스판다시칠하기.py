n, m = map(int, input().split())
lst = []
result= []

for i in range(n):
  lst.append(input())

for a in range(n-7):
  for b in range(m-7):
    cnt1 = 0
    cnt2 = 0
    for i in range(a, a+8):
      for j in range(b, b+8):
        if (i + j) % 2 == 0:
          if lst[i][j] != 'W': 
            cnt1 += 1
          if lst[i][j] != 'B': cnt2 += 1
        else: 
          if lst[i][j] != 'B': cnt1 += 1
          if lst[i][j] != 'W': cnt2 += 1
    result.append(cnt1)
    result.append(cnt2)

print(min(result))
             