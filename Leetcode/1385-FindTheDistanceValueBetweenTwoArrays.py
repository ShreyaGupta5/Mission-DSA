import bisect
from typing import List


class Solution:

  def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    ans = 0
    for x in arr1:
      i = bisect.bisect_left(arr2, x - d)
      if i == len(arr2) or arr2[i] > x + d:
        ans += 1
    return ans
