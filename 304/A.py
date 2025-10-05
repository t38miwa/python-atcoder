# 入力の読み込み
N = int(input())
people = []

for _ in range(N):
    name, age = input().split()
    age = int(age)
    people.append((name, age))

# 年齢が最も小さい人を見つける
min_age_person_index = min(range(N), key=lambda i: people[i][1])

# 出力：最小年齢の人を起点として時計回りに出力
for i in range(N):
    index = (min_age_person_index + i) % N
    print(people[index][0])
