n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    x = lst[b]
    lst.sort(reverse=True)
    print(lst.index(x)+1)
    ############# 실패 이건 다시 풀ㄹ어야돼