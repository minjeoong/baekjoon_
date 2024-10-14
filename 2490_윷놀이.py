case1 = list(map(int, input().split()))
case2 = list(map(int, input().split()))
case3 = list(map(int, input().split()))

def what_case(case):
  if case.count(0) == 1:
    print('A')
  elif case.count(0) == 2:
    print('B')
  elif case.count(0) == 3:
    print('C')
  elif case.count(0) == 4:
    print('D')
  else:
    print('E')

what_case(case1)
what_case(case2)
what_case(case3)