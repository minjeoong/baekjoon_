import math 
from fractions import Fraction 

a, b = map(int, input().split())
c, d = map(int, input().split())

if b == d:
  x = Fraction (a+c,b)
  print(x.numerator, x.denominator)
else:
  xlcm = int(math.lcm(b,d))
  k = xlcm//b
  t = xlcm//d
  a = a*k
  c = c*t
  x = Fraction(a+c, xlcm)
  print(x.numerator, x.denominator)

