import sys
input = sys.stdin.readline
while True:

    a = int(input())

 
    sumn = []
    for i in range(1,a):
        if a % i == 0:
            sumn.append(i)
    if a == -1:
        break;
    elif sum(sumn) == a:
        print(a,"= ",end = "")
        print(*sumn,sep=" + ")
    else:
        print(a, "is NOT perfect.")
