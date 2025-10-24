# 長さ9の文字列S　＝　ovowowovo
# 長さ3の文字列tの出現回数
# 1 <= i <= 9-3+1 =7 つまりiは1から7の数
# Sのi文字目からi+2文字目までからなる部分文字列がtに一致する

N,K = map(int,input().split())
S = input()

counts = {}
for i in range(N-K+1):
    if S[i:i+K] in counts:
        counts[S[i:i+K]] += 1
    else:
        counts[S[i:i+K]] = 1

max_val = max(counts.values())
keys_of_max_val = sorted([key for key in counts if counts[key] == max_val])
print(max_val)
print(' '.join(keys_of_max_val))