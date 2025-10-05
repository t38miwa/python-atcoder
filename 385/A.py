A,B,C = map(int,input().split())

result = False
if A+B == C:
    result = True
if A == B+C:
    result = True
if A+C == B:
    result = True
if A == B == C:
    result = True

if result:
    print('Yes')
else:
    print('No')