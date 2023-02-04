L, P = map(int, input().split())
lst = list(map(int, input().split()))
num = L * P
for i in range(5):
  print(lst[i] - num,end= " ")
  