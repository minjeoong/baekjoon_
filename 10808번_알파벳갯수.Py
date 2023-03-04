inp = input()
dic = {}
for str in "abcdefghijklmnopqrstuvwxyz":
    dic[str] = 0

for i in inp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for str in "abcdefghijklmnopqrstuvwxyz":
    print(dic[str], end = " ")
