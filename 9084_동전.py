# https://d-cron.tistory.com/23 참고
# 2차원으로 해결하는 법 선택했고, 1차원으로 해결도 가능한 문제
# dp 를 활용 


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
      dp[a][b] = dp[a-1][b] # 그 전에 있던 행을 복제 (2원으로 만들수 있는 가지수 + 다음 돈으로 만들 수 있는 갓지수 ... 다 합해야하기 때문)
      if b-cost_lst[a] >= 0: # X-2 에 있는 값을 가져와서 더해주는 로직인데. X-2 index 가 0보다 작으면 안되기 때문
        dp[a][b] += dp[a][b-cost_lst[a]] # 같은 행에 X-2 에 있는 값을 가져와서 현재 값과 더해줌 
  print(dp[n][m])