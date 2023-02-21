n, m = map(int,input().split())
lst =[0]*n
for x in range(m):
  i,j,k = map(int,input().split())
  for y in range(i,j+1):
    lst[y-1]= k
print(*lst)