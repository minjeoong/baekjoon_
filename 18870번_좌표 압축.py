import sys
input = sys.stdin.readline
n = int(input())

lst = list(map(int,input().split()))
lst_set = sorted(list(set(lst)))

dic={}
for i in range(len(lst_set)):
    dic[lst_set[i]] = i

for j in lst:
    print(dic[j],end=" ")