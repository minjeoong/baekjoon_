# all 은 리스트/튜플 안에 모든 값이 True 로 나왔을 때 
# True 로 반환해준다. 
# 즉, 튜플 안에 모든 값이 오름차순인지 확인하고(내 자신보다 다음 숫자가 크면 true) 모두 true 로 나오면 True 를 반환하는 것을 사용하여 
#오름차순이라면 출력하도록.

from itertools import permutations

N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]

for i in permutations(lst, M):
    if all(i[j] <i[j+1] for j in range(M-1)) == True:
        print(*i)