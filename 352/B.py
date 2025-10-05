"""AtCoder Beginner Contest 352 B"""
s = input()
t = input()

result = []
s_index = 0
t_index = 0
while s_index < len(s):
    while s[s_index] != t[t_index]:
        t_index += 1
    result.append(t_index + 1)
    s_index += 1
    t_index += 1

print(*result)