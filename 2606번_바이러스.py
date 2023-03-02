# 이거 다시 풀어야함 ,,,ㅡ춭퓿참ㄴ어ㅚ러ㅏㅁ농리ㅓㅏ모라오

n = int(input())
k = int(input())
lst = []
for i in range(k):
    lst.append(list(map(int,input().split())))

lst_2 =[lst[0][0],lst[0][1]]

for i in range(1,k):
    if lst_2.count(lst[i][0]) > 0:
        lst_2.append(lst[i][1])
    elif lst_2.count(lst[i][1]) > 0:
        lst_2.append(lst[i][0])
lstt = list(set(lst_2))

print(len(lstt)-1)