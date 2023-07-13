#피보나치 수 2
# 다이나믹 프로그래밍

# import sys
# import math

# def Fibo(n):

#     if n <= 1:
#         return n
#     return int((1/math.sqrt(5)) * ( ((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n))


# n = int(sys.stdin.readline())
# print(Fibo(n))


n = int(input())

dp = [0] *(n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])