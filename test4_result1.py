def isSubset(dict1, dict2):
    valid = True
    for c in dict1:
        if c not in dict2:
            valid = False
        elif dict2[c] < dict1[c]:
            valid = False
    return valid
def programmerStrings(s):
    t = 'programmer'
    req_freq = {}
    for i in range(len(t)):
        req_freq[t[i]] = req_freq.get(t[i], 0) + 1
        first_end = 0
        last_begin = len(s) - 1
        cur = {}
    for i in range(0,len(s)):
        cur[s[i]] = cur.get(s[i], 0) + 1
        if isSubset(req_freq, cur) == True:
            first_end = i
            break
        cur = {}
    for i in range(len(s)-1,-1,-1):
        cur[s[i]] = cur.get(s[i], 0) + 1
        if isSubset(req_freq, cur) == True:
            last_begin = i
            break
    return last_begin - first_end - 1