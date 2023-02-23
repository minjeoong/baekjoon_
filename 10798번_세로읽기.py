# 0 이 15개 채워진 리스트 5개 를 미리 생성하고
# 그 안에 수를 넣은 다음
# 출력할 때는 0 일경우 그냥 넘어가는 방식으로 출력 -> 그 수가 없으면 다음 수를 출력하는 방식 

c = [[0]*15 for i in range(5)]
for i in range(5):
    d = list(input())
    for j in range(len(d)):
        c[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if c[j][i] == 0:
            continue
        else:
            print(c[j][i], end="")
    
