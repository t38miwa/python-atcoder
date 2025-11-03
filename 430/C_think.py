from bisect import bisect_left

N, A, B = map(int, input().split())
S = list(input())

sA = [0]
sB = [0]
for c in S:
  sA.append(sA[-1] + (1 if c == "a" else 0))
  sB.append(sB[-1] + (1 if c == "b" else 0))
print(sA)
print(sB)

ans = 0
for l in range(N):
  r_a = bisect_left(sA, sA[l] + A)
  r_b = bisect_left(sB, sB[l] + B)
  ans += max(r_b - r_a, 0)

print(ans)