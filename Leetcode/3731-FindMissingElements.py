from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        mn = min(nums)
        mx = max(nums)

        ans = []
        for num in range(mn + 1, mx):
            if num not in s:
                ans.append(num)

        return ans
