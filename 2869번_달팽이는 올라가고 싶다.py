#시간 초과가 떴기 때문에 직관적으로 답이 나오는 것이 중요함.
#식 변환이 필요하다. 

import math

a, b, v = map(int, input().split())
day = (v-b)/(a-b)
print(math.ceil(day))
