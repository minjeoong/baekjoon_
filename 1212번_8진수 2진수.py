#처음 작성한 코드 -> 단어를 하나씩 쪼개서 8진수 - 10진수 -2진수로 만드는 과정. 
# 8진수 -> 10 진수
# 8**n .. 8**2, 8**1, 8**0 각 숫자와 곱해질 것이므로, 단어 길이만큼 범위를 잡고 for문

# 10 진수 -> 2진수
# 구한 10진수를 2로 나눈 나머지를 덱 으로 구현하여 가장 왼쪽에 append 하도록 만들었다.
# 그다음 2로 나눈 몫을 다시 업데이트하여 반복하는 방법.


from collections import deque
word = list(input())
sip = [0]*len(word)
for i in range(len(word)):
  sip[i] = (8**(len(word)-(i+1)))*int(word[i]) 

hap = sum(sip)
deq = deque()

while True:
  deq.appendleft(int(hap)%2)
  hap = int(hap)//2
  if hap <= 0:
    break

for i in deq:
  print(i, end="")
  
  
  
  
  
#하지만 답은 
# bin() 함수를 이용하면 x 진수를 2진수로 변환할 수 있다. (8진수 변환함수 = oct())
# 8진수로 입력 받기 -> int(input(), 8)
# [2:] 인 이유 : 그냥 출력하면 0b1101 로 출력하기 때문에, 0b를 잘라주기 위해서

print(bin(int(input(), 8))[2:])

