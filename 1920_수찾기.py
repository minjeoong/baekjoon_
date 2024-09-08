
def binary_search(array, target, start, end):

  if start > end:
    return None
  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  elif array[mid] < target:
    return binary_search(array, target, mid+1, end)
  else:
    return None


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for i in B:
  result_idx = binary_search(A, i, 0, N-1)
  if result_idx == None:
    print(0)
  else:
    print(1)
