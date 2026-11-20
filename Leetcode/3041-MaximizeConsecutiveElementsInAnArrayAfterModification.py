class Solution:
  def maxSelectedElements(self, nums: list[int]) -> int:
    # dp[x] stores the max length of a consecutive sequence ending at value x
    dp = {}

    # Sort to build consecutive sequences in ascending order
    for num in sorted(nums):
      # Update num + 1 first so we don't overwrite dp[num] before reading it
      dp[num + 1] = dp.get(num, 0) + 1
      dp[num] = dp.get(num - 1, 0) + 1

    return max(dp.values())
