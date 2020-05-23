from typing import List


def exh(A: List[int], k: int) -> int:
  L = set([0])
  for a in A:
    L = L | set(map(lambda x: x + a, L))
    L = set(sorted(filter(lambda x: x <= k, L)))
  return max(L)
