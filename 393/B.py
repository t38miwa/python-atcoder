S = input()

count = 0
for i in range(len(S)):
    for j in range(len(S)):
        for k in range(len(S)):
            if i<j and j<k:
                if j-i == k-j and S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    count += 1
print(count)