n, m = map(int, input().split(" "))
lst = []
def fuc(start):

  if len(lst) == m:
    print(" ".join(map(str,lst)))    # fuc(i)
    return
    

  for i in range(start, n+1):
    lst.append(i)
    fuc(i)
    lst.pop()


fuc(1)