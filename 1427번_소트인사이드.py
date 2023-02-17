a= input()
lst = list(a)
lst.sort(reverse=True)

for i in range(len(lst)):
    print(lst[i],end="")