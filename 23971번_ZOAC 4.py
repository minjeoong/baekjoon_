
# H, W, N, M = map(int, input().split())
# arr = [[0]*W for _ in range(H)]

# a ,b = 0,0 
# for i in range(0,H,M+1):
#   for j in range(0,W,N+1):
#     arr[a+i][b+j] = 1

# cnt = 0
# for i in range(len(arr)):
#   cnt += arr[i].count(1)
# print(cnt)

# for i in range(len(arr)-1,-1,-1):
#   print(arr[i])

import math
H, W, N, M = map(int, input().split())
a = math.ceil(W/(M+1))
b = math.ceil(H/(N+1))
print(a*b)