# CCW 알고리즘
#신발끈 공식을 이용해서 구한다.
#from 백준 블로그  https://www.acmicpc.net/blog/view/27 
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

S = (a*d + c*f + e*b) - (c*b + e*d + a*f)
if S > 0: # 반시계
    print(1)
elif S < 0:
    print(-1)
else:
    print(0)
