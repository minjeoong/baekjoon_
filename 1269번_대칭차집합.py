# set : 집합자료형
# 특징 - 중복을 허용하지 않는다.
#      - 순서가 없다
# 중복을 제거하기 위한 도구로 많이 사용됨.
# set 자료형에 저장된 값을 인덱싱으로 접근하려면,  리스트나 튜플로 변환해야함.


a, b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B)+ len(B-A)
