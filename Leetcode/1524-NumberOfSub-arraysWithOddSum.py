from typing import List


class Solution:

  def numOfSubarrays(self, arr: List[int]) -> int:
    MOD = 10**9 + 7
    even_count = 1  # Accounts for the initial empty prefix sum of 0
    odd_count = 0
    prefix_sum = 0
    result = 0

    for num in arr:
      prefix_sum += num

      if prefix_sum % 2 == 1:
        # Odd prefix sum minus any previous even prefix sum gives an odd subarray
        result = (result + even_count) % MOD
        odd_count += 1
      else:
        # Even prefix sum minus any previous odd prefix sum gives an odd subarray
        result = (result + odd_count) % MOD
        even_count += 1

    return result
