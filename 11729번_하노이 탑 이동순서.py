# N : 원반 개수
# start : 원반 시작 위치
# to : 원반을 이동할 도착치
# sub : 이동하면서 거치는 경유지

# hanoi(N)  = 1. 1                    (if N == 1)
#             2. 2 * hanoi(N-1) + 1   (else) 
# 여기서 일반항 도출해 내면 
# 하노이 탑의 일반항 2*N - 1

message = "{} {}"

def move(start, to):
    print(message.format(start, to))

def hanoi(N, start, to , sub):
    if N == 1:
        move(start, to)
    else:
        hanoi(N-1, start, sub, to)
        move(start, to)
        hanoi(N-1, sub, to, start)

N =int(input())
cnt = 0
print(2**N -1)
hanoi(N, 1, 3, 2)

