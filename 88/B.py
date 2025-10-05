n = int(input())
a = list(map(int,input().split()))

# それぞれが最大値を交互に取得していくので、aのリストをソートし、先頭から交互に取るように実装すればいい
# その時の選択（最大値を取る）ことが全体の最適になるgreedy法
sorted_a = sorted(a,reverse=True)

alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += sorted_a[i]
    else:
        bob += sorted_a[i]
        
print(alice-bob)