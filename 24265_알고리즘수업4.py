# 주어진 코드1 을 해석해보면, 
# 첫번째 for 문의 실행 횟수는 n-1 번
# 두번째 for 문의 실행 횟수는 n-i 번
# 따라서, 총 실행 횟수는 (n-1) + (n-2) + ... + 1 
# = n(n-1)/2 이게 맞긴 한데 나는 그냥 팩토리얼로 생각했다. 7이 입력들어오면 6! 인것. 


def menofpassion(n):
  sum = 0
  for i in range(1, n):
    for j in range(i+1, n+1):
      # sum = sum + a[i] * a[j]
      sum += 1
      # print("i is %d, j is %d" % (i, j))
  print(sum)

def my(n):
  sum = 0
  for i in range(n):
    sum += i
  print(sum)


n = int(input())
my(n)
print(2)