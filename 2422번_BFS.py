#한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# BFS 문제

from itertools import combinations

n, m = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(n)]
result = [[False for _ in range(n)] for _ in range(n)] # 모두 false 로 맞춰놓고

for i in range(m):
    a, b = map(int, input().split()) # 받아오는 숫자에 인덱스에 맞게 true 처리.
    result[a-1][b-1] = True # 그러면 섞어먹으면 안되는 조합에 맞게 테이블이 작성됨
    result[b-1][a-1] = True


count = 0
for i in combinations(range(n), 3): # 콤비네이션으로 모두 생성해준 후 
    # 세개의 숫자를 확인해주면 되니까. (0,1,2) 라면 (0,1) 을 확인해주고,(0,2) 확인해주고, (1,2) 확인해주면 됨. 셋중 하나라도 true 면 패스해줌
    if result[i[0]][i[1]] or result[i[0]][i[2]] or result[i[1]][i[2]] : 
        continue
    count += 1

print(count)
    