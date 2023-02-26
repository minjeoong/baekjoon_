# sys 로 인풋 받아야 시간초과 안 뜸.
# Counter 로 최빈값구해줘야 시간초과 안 ㄸ<ㅁ
# 최빈 값만 구하고 최빈 값이 1보다 크고 여러개인 경우 (2개이상이면)
# 두번째로 작은 값을 출력 

import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
lst = [0]*n
for i in range(n):
    a = int(input())
    lst[i] = a


print(round(sum(lst)/n))
lst.sort()
print(lst[n//2])

a = Counter(lst).most_common()

if len(a) > 1 and a[0][1] == a[1][1]:
    print(a[1][0])
else:
    print(a[0][0])

print(max(lst)-min(lst))