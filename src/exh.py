from typing import List
from time import time
from src.utils.io import readInput

def exh(A: List[int], k: int) -> int:
  L = set([0])
  for a in A:
    L = L | set(map(lambda x: x + a, L))
    L = set(sorted(filter(lambda x: x <= k, L)))
  return max(L)


def main(filePath: str):
  A, k = readInput(filePath)
  start = time()
  sss = exh(A, k)
  stop = time()
  print(f'{filePath} {stop-start:.2f}s {sss}')


if __name__ == "__main__":
  main("input/ss1.txt")
