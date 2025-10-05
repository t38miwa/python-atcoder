H = int(input())

# The height of the plant on the morning of day i is 2^i - 1
height = 0  # Initial height at day 0

day = 0
while height <= H:
    day += 1
    height += 2 ** day

print(day)
