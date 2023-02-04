#찾고자 하는 숫자를 lst 에 담고, 그 수 하나하나를 i 로 반복해서 확인한다.
#덱을 사용하여, 가장 앞에 있는 수 (deq[0])이 i 와 같다면, 찾고자 하는 숫자와 같다면 가장 왼쪽 숫자를 지우고 다음 숫자로 패스ㅡ.
#가장 앞에 있는 수가 i 와 같이 있지 않다면, 가장 왼쪽 혹은 가장 왼쪽으로 보내야한다.
# 1. 만약 찾고자 하는 숫자의 덱에서의 인덱스가 덱의 길이의 2분의 1보다 작으면 
#   덱의 가장 왼 쪽에 i 가 올 때까지 덱의 가장 왼쪽으로 미뤄야 한다. -> count 도 1씩 더해줌
# 2. 만약 찾고자 하는 숫자의 덱에서의 인덱스가 덱의 길이의 2분의 1보다 크다면
#   덱의 가장 오른 쪽에 i 가 올 때까지 덱의 가장 오른쪽으로 미뤄야 한다. -> count 도 1씩 더해줌.
#즉 예를 들어 10 길이의 덱에서 숫자 9가 있는 인덱스가 8일때, 덱의 길이 10/2 인 5보다 8은 크므로, 
#가장 오른 쪽으로 미루는 것이 맞다. 


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



