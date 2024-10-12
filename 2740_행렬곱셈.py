
n, m = map(int, input().split())
A = list(list(map(int, input().split())) for i in range(n) )
m, k = map(int, input().split())
B = list(list(map(int, input().split())) for i in range(m) )

def matrix_mul(A, B):
    result = [[0]*len(B[0]) for i in range(len(A))]
    for i in range(n):
        for j in range(k):
            for p in range(m):
                result[i][j] += A[i][p] * B[p][j]
    return result

result = matrix_mul(A, B)
for i in range(len(result)):
    print(*result[i])
                