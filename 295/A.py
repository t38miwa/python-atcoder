N=int(input())

W=input().split()

keywords = {"and", "not", "that", "the", "you"}
for word in W:
    if word in keywords:
        print("Yes")
        break
else:
    print("No")