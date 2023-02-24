import math
from collections import Counter

n = int(input())
lst = [0]*n
for i in range(n):
    a = int(input())
    lst[i] = a


print(round(sum(lst)/n))
lst.sort()
print(lst[n//2])

a = Counter(lst).most_common()
print(a)
if len(a) > 1 and a[0][1] == a[1][1]:
    print(a[1][0])
else:
    print(a[0][0])

print(max(lst)-min(lst))