
def count_indices_between_programmers(s):
    target = "programmer"
    foundtarget_f = ""
    foundtarget_e = ''
    i = 0
    
    while i < len(s):

        if s[i] in target:
            foundtarget_f += s[i]
            # print(foundtarget_f, i)
            if foundtarget_f.count('p')>=1 and foundtarget_f.count('r')>=3 and foundtarget_f.count('o')>=1 and foundtarget_f.count('g')>=1 and foundtarget_f.count('a')>=1 and foundtarget_f.count('m')>=2 and foundtarget_f.count('e')>=1:
                s = s[i+1:]
                foundtarget_f = ""
                i = 0
                break
        i += 1

   
    j = len(s)-1
    while j >= 0:
        if s[j] in target:
            foundtarget_e += s[j]
            # print(foundtarget_e, j)
            if foundtarget_e.count('p')>=1 and foundtarget_e.count('r')>=3 and foundtarget_e.count('o')>=1 and foundtarget_e.count('g')>=1 and foundtarget_e.count('a')>=1 and foundtarget_e.count('m')>=2 and foundtarget_e.count('e')>=1:
                s = s[:j]
                
                foundtarget_e = ""
                break
        j -= 1

    return len(s)


# 테스트 케이스
s = "programmerprogrammer"
result = count_indices_between_programmers(s)
print(result)  



