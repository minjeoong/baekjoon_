#2441번_별찍기 - 4
n = int(input())
for i in range(n,0,-1):
  print((n-i)*" "+i*"*")

#2442번_ 별찍기 - 5
n = int(input())

for i in range(1,n+1):
  print((n-i)*" " + i*"*"+ (i-1)*"*" )

#2443번_ 별 찍기 - 6
n = int(input())

for i in range(n,0, -1):
  print((n-i)*" "+i*"*"+ (i-1)*"*")

#2444번_ 별 찍기 - 7 
n = int(input())
for i in range(1,n+1):
  print((n-i)*" " + i*"*"+ (i-1)*"*" )
for i in range(n-1,0, -1):
  print((n-i)*" "+i*"*"+ (i-1)*"*")

# 2445번_ 별 찍기 - 8
n = int(input())
for i in range(1,n+1):
  print(i*"*" + 2*(n-i)*" " + i*"*")

for i in range(n-1,0, -1):
  print(i*"*"+2*(n-i)*" "+ i*"*")

#2446번_별 찍기 - 9

n = int(input())
for i in range(n,0, -1):
  print((n-i)*" "+i*"*"+ (i-1)*"*")
for i in range(2,n+1):
  print((n-i)*" " + i*"*"+ (i-1)*"*" )

#2522번_ 별 찍기 - 12

n = int(input())

for i in range(1, n+1):
  print(" "*(n-i) + "*"*i)
for i in range(n-1, 0, -1):
  print(" "*(n-i) + "*"*i)

#2523번_ 별 찍기 - 13

n = int(input())

for i in range(1, n+1):
  print("*"*i)

for i in range(n-1, 0, -1):
  print("*"*i)