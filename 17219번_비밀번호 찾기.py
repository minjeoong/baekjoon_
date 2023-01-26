#딕셔너리를 활용. 
# 싸이트와 비밀번호를 받고 딕셔너리에 넣은 후 찾고자 하는 개수만큼 딕셔너리에서 가져오는 형식.

n, m = map(int,input().split())
dic ={}
for i in range(n):
  a,b = map(str,input().split())
  dic[a] = b
for i in range(m):
  link = input()
  print(dic[link])
