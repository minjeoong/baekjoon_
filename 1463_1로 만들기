
n = int(input())
dp = [0] * (n+1)
for i in range(2,n+1):
  dp[i] = dp[i-1] + 1
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1)  # 대칭으로 이루어져 있기에 i//2 까지만 범위를 잡아줘도 됨.
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])
