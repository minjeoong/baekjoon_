#시간 초과 때문에 0과 1의 개수만 세는 방법으로 변경.
# n 이 3 이상일 때부터, n-1, n-2 의 수를 더해주는 방법.



def fibona(n):
  zero = [1, 0, 1]
  one = [0, 1, 1]
  if n >= 3:
    for i in range(3, n+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])
  print(zero[n], one[n])

a = int(input())
for i in range(a):
  n = int(input())
  fibona(n)
