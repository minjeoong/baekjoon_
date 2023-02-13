li = [0,1,3]
n = int(input())

for i in range(3,n+1):
    li.append(li[i-1]+li[i-2]*2)
print(li[n]%10007)