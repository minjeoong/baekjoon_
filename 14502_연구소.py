# 벽은 3개까지만 세운다.
# 위치의 값이 0일 때 벽을 세울 수 있다.

import copy
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
# 바이러스 감염 함수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  queue = deque()

  tem_graph = copy.deepcopy(graph)

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2:
        queue.append((i, j))
  
  # 바이러스 체크 후 확산
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if tem_graph[nx][ny] == 0:
          tem_graph[nx][ny] = 2
          queue.append((nx, ny))

  # 안전영역 계산
  global answer
  safe =0
  for i in range(n):
    safe += tem_graph[i].count(0)
  
  answer = max(answer, safe)

# 벽을 세울 때는 백트래킹
def makeWall (cnt):
  # 벽을 3개 세우면 바이러스를 퍼뜨림
  if cnt == 3:
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1 # 벽을 세운다
        makeWall(cnt + 1) #두 번째 벽 세우러 가기
        graph[i][j] = 0 # 다시 벽을 허무는 

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0

makeWall(0) # 벽을 세우는 함수 호출
print(answer)