s = input()
# 名前は問題文のまま、world,stageの方が良さそう
world = int(s[0]) 
stage = int(s[2]) 

if stage == 8:
    print(str(world+1)+'-1')
else:
    print(str(world)+'-'+str(stage+1))