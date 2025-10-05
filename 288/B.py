n, k = map(int, input().split())
s = []

for i in range(n):
    temp = input()
    if i < k:
        s.append(temp)
        
s.sort()
print(*s, sep='\n')