# 첫번째 for 문의 반복횟수 n-2번
# 두번째 for 문의 반복횟수 n-i-1번
# 세번째 for 문의 반복회수 n-j

# 5일 때는 3+2+1 + 2+1 + 1
# 6일 때는 4+3+2+1
# 7일 때는 5+4+3+2+1 + 4+3+2+1 + 3+2+1 + 2+1 + 1
# 즉 수열 안에 수열이 있는 형식
# 공식을 사용하여 풀어보면 


# def my(n):
#   sum = 0
#   for i in range(1, n-1):
#     for j in range(i+1, n):
#       for k in range(j+1, n+1):
#         print("i=%d, j=%d, k=%d" % (i, j, k))
#         sum += 1
#   print(sum)

n = int(input())
print(int(n*(n-2)*(n-1)/6))
print(3)
