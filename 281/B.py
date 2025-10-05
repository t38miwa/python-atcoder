def is_sandwich_number(S):
    # Check if the length of S is exactly 8
    if len(S) != 8:
        return "No"

    # Check if the first and last characters are uppercase English letters
    if not (S[0].isupper() and S[-1].isupper()):
        return "No"

    # Check if the middle part (characters from index 1 to 6) is a 6-digit integer
    middle_part = S[1:7]
    if not (middle_part.isdigit() and 100000 <= int(middle_part) <= 999999):
        return "No"

    return "Yes"

# Read input
S = input().strip()

# Print output
print(is_sandwich_number(S))
