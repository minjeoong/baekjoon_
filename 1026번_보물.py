N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
C = [0]*N
for i in range(N):
  C[i] = A[i]*B[i]
print(sum(C))