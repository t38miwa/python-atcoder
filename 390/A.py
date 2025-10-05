A = input().split()

result = False
if ''.join(A) == '12345':
    result = False

for i in range(len(A)-1):
    A[i],A[i+1] = A[i+1],A[i]
    if ''.join(A) == '12345':
        result =True
        break
    else:
        A[i],A[i+1] = A[i+1],A[i]
        result = False

print("Yes" if result else "No")