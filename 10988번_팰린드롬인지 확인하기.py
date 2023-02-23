str = input()
lst = [char for char in str]
lst_re = list(reversed(lst))

if lst == lst_re:
    print(1)
else:
    print(0)
