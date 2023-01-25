n, k = map(int,input().split()) 
lst = []
for i in range(n):
  lst.append(int(input()))
count = 0

for i in reversed(range(n)): 
  count += k // lst[i] #1000으로 2400원을 나눈 몫 ->  2  (2000원을 2개 쓴 것이므로 count 에 추가)
  k = k % lst[i] #1000원으로 2400원을 나눈 나머지 -> 400 (결국엔 다음 순서로 100원이 400을 나눌 수 있도록 k에 덮어 씌우기.)
print(count)
