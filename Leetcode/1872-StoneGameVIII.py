class Solution:

  def stoneGameVIII(self, stones: List[int]) -> int:
    # Compute prefix sums
    s = list(accumulate(stones))
    # The max score difference starting from the last valid choice
    res = s[-1]
    # Traverse backwards from n-2 down to 1
    for i in range(len(stones) - 2, 0, -1):
      res = max(res, s[i] - res)
    return res
