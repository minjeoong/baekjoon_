i = int(input())
s = map(int,input().split())
cnt = 0
for n in s:  
  if n > 1:
    error = 0 
    for i in range(2,n): # 2 부터터 n-1 까지
      if n % i == 0:  # 1과과 자신을을 제외한한 수로로 나눠지면면 소수가가 아님님 
        error += 1
    if error == 0:
      cnt += 1
print(cnt)
