
# 이항계수 공식 n! / k!(n-k)!


n,k = map(int,input().split())

Nfac = 1
for i in range(1,n+1):
  Nfac = Nfac*i

Kfac = 1
for i in range(1,k+1):
  Kfac = Kfac*i

NKfac = 1
for i in range(1, n-k+1):
  NKfac = NKfac*i

print(int(Nfac/(Kfac*NKfac)))