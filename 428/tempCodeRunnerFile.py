S = input()

s1 = S.replace('()','')
s2 = s1.replace('()','')

def is_good(S):
    while len(S) >= 2:
        if '()' in S:
            S = S.replace('()','')
        else:
            break  
    if len(S) > 0:
        return False
    else:
        return True

flag = is_good(S)
print(flag)