#BFS 문제..
# 받은 리스트 = grid, 방문 했으면 0->1 = visited 
# nsk 색약 x, sk = 색약 o

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        dxdy = [(0,-1),(0,1),(-1,0),(1,0)]
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))


n = int(input())
grid = [list(map(str, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)]for _ in range(n)]
nsk = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            nsk += 1
print(nsk,end =" ")

sk = 0 
visited = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == "G":
            grid[i][j] = "R"

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            sk += 1

print(sk)