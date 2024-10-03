
sumlist = []

for i in range(5):
  lst = map(int, input().split())
  sumlist.append(sum(lst))

print(sumlist.index(max(sumlist))+1 , max(sumlist))