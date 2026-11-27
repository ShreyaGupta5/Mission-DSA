from math import inf
from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    # dp[w] = max items obtained from buying at most 1 copy of selected item types with cost w
    dp = [0] * (budget + 1)
    min_price = inf

    for factor, price in items:
      min_price = min(min_price, price)

      # Total yield for the first purchase: 1 (itself) + count of j != i where factor_j % factor == 0
      yield_count = sum(factor_j % factor == 0 for factor_j, _ in items)

      # Standard 0-1 Knapsack backward transition
      for w in range(budget, price - 1, -1):
        dp[w] = max(dp[w], dp[w - price] + yield_count)

    # Combine initial purchase yields with buying as many cheapest items as possible using leftover budget
    return max(
        initial_items + (budget - w) // min_price
        for w, initial_items in enumerate(dp)
    )
