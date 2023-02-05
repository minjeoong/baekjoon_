#  a.numerator : 분자
#  a.denominator  :  분모
#  Fraction(2,4) -> 2/4 를 알아서 기약분수로 만들어줌 1/2

from fractions import Fraction 

n = int(input())
lst = list(map(int, input().split()))

for i in range(1,n):
    a = Fraction(lst[0],lst[i])
    print(a.numerator,"/",a.denominator,sep="")
