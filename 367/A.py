A, B, C = map(int, input().split())

if B < C:
    # Case: Sleeping time does not cross midnight (e.g., 8 to 14)
    if B <= A < C:
        print("No")
    else:
        print("Yes")
else:
    # Case: Sleeping time crosses midnight (e.g., 21 to 7)
    if C <= A or A < B:
        print("Yes")
    else:
        print("No")
