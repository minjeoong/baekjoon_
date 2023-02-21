n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
for x in range(m):
    i, j = map(int,input().split())
    new=lst[i-1:j]
    del lst[i-1:j]

    new.reverse()
    c = 0

    for y in range(i-1,j):
        
        lst.insert(y,new[c])
        c+= 1

print(*lst)
