#분해합
# BFS

inp = int(input())
# 1 ~ 받은 숫자까지 돌면서 생성자 찾기
for i in range(1, inp+1):
    sumn = sum(map(int, str(i)))     #각 자리 숫자 합
    sum_num = sumn + i   # 받은 수 + 각자리 숫자 합
    if sum_num == inp:
        print(i)
        break
    if i == inp:
        print(0)

