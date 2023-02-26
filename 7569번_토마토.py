# BFS 문제
# 1. 익은 토마토를 (1 값) 모두 큐에 넣는다. 
# 2. BFS 함수를 돌려서 큐에 값이 들어있으면 상하좌우앞뒤 모두 확인. 
# 3. 토마토가 존재한다면 (0 값) 확인 할 때마다 +1 되도록 저장한다. 
#    만약 1이 있어서 오른쪽으로 퍼졌다면 그 자리에는 2를 저장. 그 오른쪽 위에 토마토가 또 있어서 위로 퍼졌다면 그 자리에는 3을 저장. 
#    값을 저장할 뿐 아니라 그 자리 값을 또 확인해야하니까 q 에 append 함
# 4. z = 1 result = -1 저장해두고,
#    4-1 함수가 돌고 난 후, 저장된 값들 중 0이 존재한다면 z = 0으로 바꾼다. (즉 익지 않은 토마토가 존재한다면 z=0 으로 바꿈)
#    4-2 저장된 값과 -1 중에 max 값을 result 에 저장한다. 
# 5. z = 0 이면 (익지 않은 토마토가 존재한다는 것) -1 을 출력
#    result = 1 이면 (모든 토마토가 익음) 0 을 출력
#    아니라면 그냥 며칠 걸렸는치 줄력해야하니깐 앞서 +1 해서 저장해준 값들 중 (가장 큰 값 -1)을 출력 (1에서 출발했기 때문.)

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x,y,z = q.popleft()
        dxdydz = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
        for dx,dy,dz in dxdydz:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if -1 < nx < H and -1 < ny < N and -1 < nz < M:
                if grid[nx][ny][nz] == 0:
                    grid[nx][ny][nz] = grid[x][y][z] + 1
                    q.append((nx,ny,nz))


M,N,H = map(int,input().split())
grid = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 1:
                q.append((i,j,k))
bfs()

z = 1
result = -1
for i in grid:
    for j in i:
        for k in j:
            if k == 0:
                z = 0
            result = max(result, k)
if z == 0 :
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)

