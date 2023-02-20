#순열 라이브러리를 사용하여 풀었음. 
# *을 붙여서 출력하면 리스트/튜플 안에 내용 값만 출력한다. 

from itertools import permutations

N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]

for i in permutations(lst, M):
    print(*i)

   


