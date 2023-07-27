def paint_houses(n):
    mod = 10**9 + 7

    if n == 0:
        return 0
    elif n == 1: # 집이 한개면 3가지 색 칠할 수 있으므로 
        return 3

    prev_prev = 3 #집이 1개일때 3가지
    prev = 6 #집이 2개일때 6가지 m => 계속 업데이트 다이나믹 프로그래밍

    for i in range(3, n, 2):
        curr = (prev * prev_prev ) % mod
        print(curr , prev)
        prev = curr

    return prev

n = 4
result = paint_houses(n)
print(result)  # Output: 18

# n = 6
# result = paint_houses(n)
# print(result)  # Output: 54

# 집이 한 채면 3
# 두 채면 6
# 세 채면 18 = 6 * 3
# 네 채면 54 = 18 * 6
