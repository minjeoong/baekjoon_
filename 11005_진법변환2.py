N, B = map(int, input().split())
lst = ''

# 36 진수로 변환 시 그냥 나머지만 넣으면 35로 나오기 때문에 변환을 위한 Number 선언
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N:
  lst += number[N % B]
  N //= B

print(lst[::-1])