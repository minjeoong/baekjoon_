# 위에서 더해서 밑으로 내려갔을 때 가장 큰 수를 출력하는 방식 
# 한 가지 방법만 생각하지 말고 모든 방법의 수를 비교해서 max 로 출력 

n = int(input())
grid = []
for k in range(n):
    grid.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(grid[i])):
        if j == 0:
            grid[i][j] = grid[i-1][j] + grid[i][j]
        elif j == len(grid[i])-1:
            grid[i][j] = grid[i-1][j-1] + grid[i][j]
        else:
            grid[i][j] = grid[i][j] + max(grid[i-1][j-1], grid[i-1][j])

print(max(grid[n-1]))