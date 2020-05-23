from typing import List


def greedy(A: List[int], k: int) -> int:
  S = set()
  G = 0
  for a in sorted(A, reverse=True):
    if G + a > k: continue
    S.add(a)
    G += a
  return G
