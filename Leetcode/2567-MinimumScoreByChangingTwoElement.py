from typing import List

class Solution:

  def minimizeSum(self, nums: List[int]) -> int:
    # Sort the array in ascending order
    nums.sort()

    # Compare the 3 ways to change two extreme elements:
    # 1. Change the 2 smallest elements
    # 2. Change the 2 largest elements
    # 3. Change 1 smallest and 1 largest element
    return min(
        nums[-1] - nums[2],
        nums[-3] - nums[0],
        nums[-2] - nums[1],
    )
