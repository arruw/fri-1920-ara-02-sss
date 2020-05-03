import unittest
from src.utils.io import readInput
from src.solvers.fptas import fptas as solve

class TestFptas(unittest.TestCase):

  EPS = 0.4

  def assertApprox(self, eps, optimal, result):
    self.assertGreaterEqual(result, optimal*eps)
    self.assertLessEqual(result, optimal)

  def test_ss1(self):
    A, k = readInput("input/ss1.txt")
    sss = solve(A, k, self.EPS)
    self.assertApprox(self.EPS, k, sss)

  def test_ss2(self):
    A, k = readInput("input/ss2.txt")
    sss = solve(A, k, self.EPS)
    self.assertApprox(self.EPS, k, sss)

  def test_ss3(self):
    A, k = readInput("input/ss3.txt")
    sss = solve(A, k, self.EPS)
    self.assertApprox(self.EPS, k, sss)

  def test_ss4(self):
    A, k = readInput("input/ss4.txt")
    sss = solve(A, k, self.EPS)
    self.assertApprox(self.EPS, k, sss)

  def test_ss5(self):
    A, k = readInput("input/ss5.txt")
    sss = solve(A, k, self.EPS)
    self.assertApprox(self.EPS, k, sss)

if __name__ == '__main__':
  unittest.main()