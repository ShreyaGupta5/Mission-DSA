import math
from typing import List


class Solution:

  def numOfWays(self, nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    # Precompute combinatorics using Pascal's triangle or math.comb
    # math.comb(n, k) calculates nChooseK
    def dfs(node_list: List[int]) -> int:
      if len(node_list) <= 2:
        return 1

      root = node_list[0]
      left = [x for x in node_list[1:] if x < root]
      right = [x for x in node_list[1:] if x > root]

      ways_left = dfs(left)
      ways_right = dfs(right)

      # Combinations of merging left and right branches
      comb = math.comb(len(left) + len(right), len(left))

      return (comb * ways_left % MOD) * ways_right % MOD

    return (dfs(nums) - 1 + MOD) % MOD
