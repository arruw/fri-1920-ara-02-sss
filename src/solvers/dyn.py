from typing import List


def dyn(A: List[int], k: int) -> int:
  A = sorted(A)
  DP = [
    [0 for s in range(k+1)],
    [0 for s in range(k+1)]
  ]

  i = 1
  while i <= len(A):
    for j in range(1, k+1):
      skip = DP[(i+1)%2][j]
      take = DP[(i+1)%2][j-A[i-1]] + A[i-1] if j-A[i-1] >= 0 else skip
      DP[i%2][j] = max(skip, take)
    i += 1

  return DP[(i+1)%2][k]
