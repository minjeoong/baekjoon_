
import sys

def Fibo(n):
    if n <= 1:
        return n
    return Fibo(n-1) + Fibo(n-2)


n = int(sys.stdin.readline())
print(Fibo(n))
