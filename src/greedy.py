from typing import List
from time import time
from src.utils.io import readInput

def greedy(A: List[int], k: int) -> int:
  S = set()
  G = 0
  for a in sorted(A, reverse=True):
    if G + a > k: continue
    S.add(a)
    G += a
  return G


def main(filePath: str):
  A, k = readInput(filePath)
  start = time()
  sss = greedy(A, k)
  stop = time()
  print(f'{filePath} {stop-start:.2f}s {sss}')


if __name__ == "__main__":
  main("input/ss1.txt")
