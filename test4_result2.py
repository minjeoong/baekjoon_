def permute(a, l, r):
    if l == r:
        return ''.join(a)
    else:
        permutations = []
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            p = permute(a, l+1, r)
            for j in p:
                permutations.append(j)
                a[l], a[i] = a[i], a[l]
        return permutations
16/21
def programmerStrings(s):
    t = 'programmer'
    first_end = 0
    last_begin = len(s) - 1
    for i in range(0,len(s)):
        prefix = s[0:i+1]
        permutations = permute(list(prefix), 0, i)
        for p in permutations:
            if t in p:
                first_end = i
                break
        if first_end != 0:
            break
    for i in range(len(s)-1,-1,-1):
        suffix = s[i : len(s)]
        permutations = permute(list(suffix), 0, i)
        for p in permutations:
            if t in p:
                last_begin = i
                break
        if last_begin != 0:
            break
    return last_begin - first_end - 1