from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1,n+1)])

cnt = 0

for i in lst:
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i) < len(deq)/2:
                while deq[0] != i:
                    deq.append(deq.popleft())
                    cnt += 1
            else:
                while deq[0] != i:
                    deq.appendleft(deq.pop())
                    cnt += 1

print(cnt)



