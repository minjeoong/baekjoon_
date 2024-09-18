
# 이건 이분탐색으로 품.


# 전체 시간 복잡도:

# 	1.	정렬 단계: O(N log N)
# 	2.	이진 탐색 단계: O(M log N)

# 따라서 전체 시간 복잡도는:


# O(N \log N + M \log N)



N = int(input())

Nlst = input().split()

M = int(input())
Mlst = input().split()
Nlst.sort()
result = []

def binary_search(arr, target, start, end):

  while start <= end:
    mid = (start+end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return None


for i in Mlst:
  idx = binary_search(Nlst, i, 0, N-1)
  result.append(0 if idx is None else 1)



print(*result)
