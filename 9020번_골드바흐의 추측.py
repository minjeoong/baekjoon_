# 처음에는 반복문을 무조건 돌렸다. 시간 초과가 났지만 제대로 정답은 나오므로 우선 킵.
# 다시 푼 문제는 받은 숫자를 반으로 나눠서 두 숫자가 둘 다 소수면 프린트, 아니면 한 숫자는 +1, 한 숫자는 -1 하면서 두 숫자가 모두 소수일 때까지 반복. 

# from itertools import combinations, permutations
# import sys
# input = sys.stdin.readline
# n = int(input())
# for i in range(n):
#     a = int(input())
#     lst = []
#     for i in range(2,a):
#         if a == 1:
#             continue
#         for j in range(2,i):
#             if i % j == 0 :
#                 break
#         else:
#             lst.append(i)

#     combi = list(combinations(lst, 2))
#     for j in lst:
#         if j == a//2:
#             combi.append((j,j))
    
#     summ = []
#     for k in range(len(combi)):
#         if sum(combi[k]) == a:
#             summ.append(combi[k])

#     max = summ[0][1] - summ[0][0]
#     pf = summ[0]
#     for p in range(len(summ)):
#         if summ[p][1] - summ[p][0] < max:
#             max = summ[p][1] - summ[p][0]
#             pf = summ[p]
#     print(*pf)


def isprime(n):
    if n == 1:
        return False
    for j in range(2,int((n**0.5))+1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if isprime(a) and isprime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1

