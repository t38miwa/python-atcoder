s=input()

a_index=[]
b_index=[]
c_index=[]

for i in range(len(s)):
    if s[i]=='A':
        a_index.append(i)
    if s[i]=='B':
        b_index.append(i)
    if s[i]=='C':
        c_index.append(i)

result=True
for i in range(len(a_index)-1):
    if a_index[i]+1!=a_index[i+1]:
        result=False
        break
for i in range(len(b_index)-1):
    if b_index[i]+1!=b_index[i+1]:
        result=False
        break
for i in range(len(c_index)-1):
    if c_index[i]+1!=c_index[i+1]:
        result=False
        break

# 'A'の最後が'B'の最初と連続しているか確認
if a_index and b_index:  # 両方が存在する場合のみ確認
    if a_index[-1] + 1 != b_index[0]:
        result = False

# 'B'の最後が'C'の最初と連続しているか確認
if b_index and c_index:  # 両方が存在する場合のみ確認
    if b_index[-1] + 1 != c_index[0]:
        result = False

if result:
    print('Yes')
else:
    print('No')