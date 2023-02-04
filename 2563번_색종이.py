#2차원 배열 받고  -  받은 a, b 값을 기준으로 10만큼 1로 채우기 반복  -  1 로 채워진 배열 카운트.


arr = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())

for i in range(N):
  a, b = map(int, input().split())
  for row in range(a,a+10):
    for col in range(b, b+10):
      arr[row][col] = 1
cnt = 0
for i in arr:
  cnt += i.count(1)

print(cnt)