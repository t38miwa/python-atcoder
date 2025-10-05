s = input()

i_world = int(s[0])
j_world = int(s[2])

if 1 <= j_world <= 7:
    print(f"{i_world}-{j_world+1}")
else:
    print(f"{i_world+1}-{1}")