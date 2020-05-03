from typing import List, Tuple

def readInput(filePath: str) -> Tuple[List[int], int]:
  """
  Read input in format
  ```
  n
  k
  a_1
  a_2
  ...
  a_n
  ```
  """
  with open(filePath) as f:
    lines = list(map(lambda l: int(l.replace('\n', '')), f.readlines()))
  
  n = lines[0]
  k = lines[1]
  A = lines[2:n+2]
  return (A, k)