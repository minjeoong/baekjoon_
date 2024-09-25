from collections import deque


def bfs():

  while lst:
    x, y = lst.popleft()
    dxdy = [(0,1),(0,-1), (1,0), (-1,0)]

    for dx, dy in dxdy:
      nx = x + dx
      ny = y + dy

      if -1 < nx < N and -1 < ny < M:
        if grid[nx][ny] == 0: # 0 이면 익지 않은 토마토 => 주변 토마토가 익지 않았다면 ~ 
          grid[nx][ny] = grid[x][y] + 1  # 1이 있었던 자리에 2를 넣어주고, 2가 있었던 자리에 3을 넣어주는 방식
          lst.append((nx,ny)) # 그리고 그 확인한 주변 토마토 좌표를 다시 lst 에 넣어줌 (그 주변 토마토 기준으로 또 주변 순찰)
      # for i in grid:
      #   print(i) 
      # print("------------------------------") 




M,N = map(int, input().split())
grid = [list(map(int,input().split(" "))) for _ in range(N)]
lst = deque()
day = 0


for i in range(N):
  for j in range(M):
    if grid[i][j] == 1:
      lst.append((i,j))

bfs()



z = 1
result = -1

for i in grid:
  for j in i:
    if j == 0: # 값을 다 돌렸는데 0 이 남았으면 익지 않은 토마토가 있다는 것
      z = 0 # 모두 익지는 못하는 상태
    result = max(result, j) # 모든 토마토가 익었을 때, 가장 큰 값이 최종 걸린 날짜가 됨

if z == 0: # 모두 익지는 못하는 상태
  print("-1")
elif result == 0: # 저장될 때부터 모든 토마토가 익어있는 상태
  print("0")
else:
  print(result-1) # 1부터 시작했기 때문에 -1 해줌