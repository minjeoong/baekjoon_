

n, m = map(int, input().split())
lisst = list(map(int, input().split()))
result = 0 

for i in range(1, n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if (lisst[i] + lisst[j] + lisst[k]) > m:
        continue
      else:
        result = max(result, lisst[i] + lisst[j] + lisst[k])

print(result)
