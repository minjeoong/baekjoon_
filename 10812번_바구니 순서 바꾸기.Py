from collections import deque
n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
for x in range(m):
    i, j, k = map(int,input().split())
    deq = deque(lst[i-1:j])
    del lst[i-1:j]
    deq.rotate(-(k-i))
    list_deq = list(deq)
    c = 0

    for y in range(i-1,j):
        
        lst.insert(y,list_deq[c])
        c+= 1
print(*lst)