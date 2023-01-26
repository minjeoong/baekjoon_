#마이너스 뒤로 괄호를 쳐야함. -> 마이너스 기준으로 나눠서 입력받기
#+기준으로 나눈 값은 더해서 cnt에 넣었다가 , 이를 num 리스트에 전부 넣어서 저장.
#num 리스트 [0]에는 가장 처음 숫자가 들어있을 거고, 그 숫자에서 뒷 연산을 모두 뺄셈해주면 돼.
#그 전에 + 연산은 미리 다 진행했기 때문

a = input().split('-')
num = []

for i in a:
  cnt= 0
  s = i.split("+")
  for j in s:
    cnt += int(j)
  num.append(cnt)

out = num[0]
for i in range(1, len(num)):
  out -= num[i]
print(out)
