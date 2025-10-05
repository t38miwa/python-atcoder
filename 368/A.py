n, k = map(int, input().split())
a = list(map(int, input().split()))

yama = a[-k:]
yama_join = ' '.join(map(str, yama))
a_join = ' '.join(map(str, a[:-k]))

print(yama_join, a_join)
