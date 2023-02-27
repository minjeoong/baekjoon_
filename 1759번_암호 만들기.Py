#모음은 1개 이상, 자음은 2개이상이라는 조건을 유의해야하는 문제.
# 모음을 카운트 하고, 자음을 카운트 해서 그 조건에 맞다면 프린트해주는 형식으로 풀어냈다.
from itertools import combinations, permutations

a = set(["a","e","i","o","u"])
l, c = map(int,input().split())
lst = list(map(str, input().split()))
lst.sort()
combi = list(combinations(lst,l))


for i in combi:
    cnt_a, other_a = 0, 0
    for char in i:
        if char in a:
            cnt_a += 1
        else:
            other_a += 1
    if cnt_a > 0 and other_a > 1:
        print(*i,sep="")





