lst1 = []
lst2 = []
for i in range(3):
    a = int(input())
    lst1.append(a)
for j in range(2):
    b = int(input())
    lst2.append(b)

print(min(lst1) + min(lst2) - 50)