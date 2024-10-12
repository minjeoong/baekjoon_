n = list(input())
len_n = len(n)
tem = [16 ** (len_n - i - 1) ㅜfor i in range(len_n)]

for i in range(len_n):
    if n[i] in 'ABCDEF':  # A-F의 경우
        n[i] = int(n[i], 16)
    else:
        n[i] = int(n[i])

for i in range(len_n):
    n[i] *= tem[i]

print(sum(n))
