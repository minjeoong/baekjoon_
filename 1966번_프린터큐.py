# b : 내위치 
# cnt : 이동 횟수 
from collections import deque
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    deq = deque(list(map(int, input().split())))
    cnt = 0
    while deq:
        Wang = max(deq)
        front = deq.popleft()
        b -= 1

        if front == Wang:
            cnt += 1
            if b < 0:
                print(cnt)
                break
        else:
            deq.append(front)
            if b < 0:
                b = len(deq) - 1
        

    

