

while True:
  a, b, c = map(int,input().split())
  lst = [a,b,c]
  lst.sort()
  if a == 0 and b == 0 and c == 0:
    break
  
  if lst[0] + lst[1] <= lst[2]: # 삼각형이 아닌 경우
    print("Invalid")
  elif a == b or b == c or c == a: # 두 변이 같은
    if a==b==c : # 근데 세 변이 같은
      print("Equilateral")
    else:
      print("Isosceles")
  elif a != b and b != c and c != a: # 세 변이 다른
    print("Scalene")  

