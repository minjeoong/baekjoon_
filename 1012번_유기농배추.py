

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x, y):
    queue = [(x,y)]  # 큐에 x  y 값을 저장해둠

    lst[x][y] = 0  # 1 이었기 때문에 이 함수에 왔으니깐 0 으로 교체 즉 확인했다는 뜻

    while queue:
        x,y= queue.pop() # 큐에 저장된 x y 를 불러온다.

        for i in range(4):
            nx = x + dx[i] # x 의 상하좌우를 확인한다. 
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if lst[nx][ny] == 1: #상하좌우를 확인했는데 1이 있었다면, 
                queue.append((nx,ny)) # 그 해당 값을 큐에 넣고 
                lst[nx][ny] = 0 # 그 값에 해당되는 1 을 0으로 교체 즉 확인했다는 뜻

        # 큐에 넣어진 값을 다시 while 문 앞으로 가서 꺼내서  앞서 확인했던 x y 값이 아니라, 큐에 다시 저장했던 그 저장된 값의 상하좌우를 또 확인한다.


T = int(input())

for j in range(T):
    m,n,k = map(int, input().split())
    cnt = 0
    lst = [[0]*n for _ in range(m)]

    for i in range (k):
        a, b = map(int, input().split())
        lst[a][b] = 1


    for a in range(m):
        for b in range(n):
            if lst[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)

