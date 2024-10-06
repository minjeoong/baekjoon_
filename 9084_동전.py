import sys
t = int(sys.stdin.readline())



for i in range(t):
  n = int(sys.stdin.readline()) # 동전의 가지 수

  cost_lst = list(map(int, sys.stdin.readline().split())) # n가지 동전의 각 금액 오름차순
  cost_lst.insert(0, 0)

  m = int(sys.stdin.readline()) # 만들어야 할 금액 

  dp = [[0]* (m+1) for _ in range(n+1)]

  for i in range(n+1):
    dp[i][0] = 1

  for a in range(1, n+1):
    for b in range(1, m+1):
      dp[a][b] = dp[a-1][b]
      if b-cost_lst[a] >= 0:
        dp[a][b] += dp[a][b-cost_lst[a]]
  print(dp[n][m])