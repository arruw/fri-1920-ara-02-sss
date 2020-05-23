from typing import List, Tuple, Set
from functools import reduce


def fptas(A: List[int], k: int, eps: float) -> int:
  A = sorted(A, reverse=True)
  delta = eps/(2*len(A))

  def trim(agg: Tuple[Set[int], float], a: int) -> Tuple[Set[int], float]:
    result, limit = agg
    if a > limit:
      result.add(a)
      limit = a * (1 + delta)
    return (result, limit)

  L = {0}
  for a in A:
    L = L | set(map(lambda x: x + a, L))
    L = set(sorted(filter(lambda x: x <= k, L)))
    L, _ = reduce(trim, L, ({0}, 0))
  return max(L)
