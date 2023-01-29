# 투 포인터, 구간합 문제
# 투 포인터(Two Pointers) : 두 지점을 통해 구간의 부분합 도출
# 설명하기 어렵다 
# 리스트 받은 값 [0]을 sum의 첫 수로 정하고, sum 이 m과 같아질 때 cnt 가 증가.
######################
# 우선 end 와 start 는 인덱스 값.
# lst[start] ~ lst[end] 사이 수의 합을 구하는 것이다. 
# 
# 1. sum 이 m 보다 작으면 더 더해줘야 하므로, 두 포인터 중 end 를 +1 한다. -> 인덱스가 더해진다? lst[end] 값을 sum 에도 더해야함.
# 2. sum 이 m 과 같으면 (문제에서 구하고자 하는 답) 도출. 즉 cnt +1 하고 start 수를 왼쪽으로 미뤄준다. 즉 +1 해준다
# (당연히 인덱스가 번했으니 sum 에도 lst[start] 값을 빼줘야겠지 ? **중요 먼저 sum 에서 빼주고 start 를 +1 해줘야함. 순서 매우 중요)
# 3. sum 이 m 보다 크면  빼줘야지 뭐.
# 두 포인터 중 start 값을 오른쪽으로 민다. 즉 +1 해줌.
#(당연히 인덱스가 변했으니 .. 뭐 똑같다 위랑. 근데 마찬가지로 sum에서 lst[start]를 먼저 빼주고 start 를 +1 해줘야 하는 순서가 중요)



n, m = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
sum = lst[0]
start, end = 0, 0

while True:
  print(sum)
  print("start:", start, "end:", end)
  if sum < m :
    end += 1
    if end >= n:
      break
    sum += lst[end]
  elif sum == m :
    cnt += 1
    sum -= lst[start]
    start+= 1
  else:
    sum -= lst[start]
    start += 1
print(cnt)