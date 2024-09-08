# 내가 짠 코드

# def research (array, target, start, end):
#   if start > end:
#     return None
#   mid = (start + end) // 2

#   if array[mid] == target:
#     return mid
#   elif array[mid] > target:
#     return research(array, target, start, mid-1)
#   elif array[mid] < target:
#     return research(array, target, mid+1, end)
#   else:
#     return None
  

# N = int(input())
# lst = list(map(int, input().split()))

# M = int(input())
# lst2 = list(map(int, input().split()))

# lst.sort()
# result = []

# for i in lst2:
#   cnt = 0
#   while True:
#     idx = research(lst,i,0,len(lst)-1)
#     if idx is None:
#       break
#     else:
#       cnt += 1
#       lst.pop(idx)
#   result.append(cnt)

# print(*result)


# ----------------------------------------------------------------

import bisect

def count_occurrences(lst, target):
    left = bisect.bisect_left(lst, target)  # target 이 처음 등장하는 위치
    right = bisect.bisect_right(lst, target)  # target 이 마지막으로 등장하는 위치
    return right - left # sorting 을 하니까. 마지막 위치에서 처음 등장하는 위치를 빼면 target 의 개수가 나옴

N = int(input())
lst = list(map(int, input().split()))

M = int(input())
lst2 = list(map(int, input().split()))

lst.sort()  
result = []

for i in lst2:
    result.append(count_occurrences(lst, i))

print(*result)