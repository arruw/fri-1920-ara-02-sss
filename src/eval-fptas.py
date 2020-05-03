import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple
from random import random, randint, sample
from statistics import mean, stdev
from time import time
from src.solvers.fptas import fptas


def generate(n: int) -> Tuple[List[int], int]:
  A = []
  for _ in range(n):
    A.append(randint(1, int(n/2)))
  
  k = sum(sample(A, int(n*random())))
  return (A, k)


def main():
  data = []
  for x in range(10, 101, 5):
    print(f'x={x}')
    for _ in range(20):
      A, k = generate(200)
      start = time()
      sss = fptas(A, k, 10/x)
      data.append((10/x, time()-start))

  sns.lineplot(
    x=list(map( lambda x: x[0], data)),
    y=list(map( lambda x: x[1], data)),
    err_style='band'
  )
  plt.xlabel('$\epsilon$')
  plt.ylabel('$t[s]$')
  plt.savefig('output/eval-fptas.png')
  plt.show()


if __name__ == "__main__":
  main()
