from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Step 1: Calculate the absolute differences
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        
        # If total differences are less than or equal to k, we can make all differences 0
        if sum(d) <= k:
            return 0
        
        # Step 2: Binary search for the maximum threshold of the difference
        left, right = 0, max(d)
        while left < right:
            mid = (left + right) >> 1
            if sum(max(v - mid, 0) for v in d) <= k:
                right = mid
            else:
                left = mid + 1
        
        # Step 3: Reduce all differences greater than 'left' down to 'left'
        for i, v in enumerate(d):
            if v > left:
                k -= (v - left)
                d[i] = left
        
        # Step 4: Distribute any remaining k operations (decrementing values equal to 'left' by 1)
        for i, v in enumerate(d):
            if k == 0:
                break
            if v == left:
                k -= 1
                d[i] -= 1
        
        # Step 5: Compute the sum of squared differences
        return sum(v * v for v in d)
