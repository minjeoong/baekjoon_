N = int(input())
#리스트를 받고 문제에서는 B를 제배열하면 안 된다고 했지만 난 그냥.. 재배열함
#문제 보고 딱 떠오른 건 A 는 오름차순 B는 내림차순
# 후 리스트 곱셈. -> append 로 C 에 넣을까 했으나 또 런타임 에러 뜰까봐 C를 생성해놓고 변경시키는 시나리오

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
C = [0]*N
for i in range(N):
  C[i] = A[i]*B[i]
print(sum(C))