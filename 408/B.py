N = int(input())
A = list(map(int,input().split()))

print(len(set(A)))
set_A = set(A)
sorted_A = sorted(set_A)
print(*sorted_A)