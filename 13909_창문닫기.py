# 그냥 푸는 줄 알았더만 규칙이 있었던 문제.
# 4이면 답이 2
# 5이면 답이 2
# ...
# 9이면 답이 3
# 10이면 답이 3
# ...
# 16이면 답이 4
# 등의 규칙이 있다


import sys
import math

n = int(sys.stdin.readline())

print(math.floor(n**0.5))

