N, S = int(input()), input()

if '-' in S and 'o' in S:
    parts = S.split('-')
    lengths = map(len, parts)
    max_length = max(lengths)
    print(max_length)
else:
    # 'o' だけ、または '-' だけ、という場合は -1
    print(-1)