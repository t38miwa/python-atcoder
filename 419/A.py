S = input()

lang = {'red':'SSS','blue':'FFF','green':'MMM'}

for k,v in lang.items():
    if k == S:
        print(v)
        exit()
print('Unknown')