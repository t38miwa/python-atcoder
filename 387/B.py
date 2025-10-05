count = 0
X = int(input())
for i in range(1,10):
    for j in range(1,10):
        if i*j != X:
            count += i*j

print(count)