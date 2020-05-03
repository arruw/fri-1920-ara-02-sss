from typing import List, Tuple, Set
from time import time
from functools import reduce
from src.utils.io import readInput


def fptas(A: List[int], k: int, eps: float) -> int:
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


def main(filePath: str):
  A, k = readInput(filePath)
  start = time()
  sss = fptas(A, k, 0.2)
  stop = time()
  print(f'{filePath} {stop-start:.2f}s {sss}')


if __name__ == "__main__":
  main("input/ss1.txt")
