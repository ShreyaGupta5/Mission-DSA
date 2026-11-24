import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # Upper bound optimization to prevent unnecessary large integer math
        max_possible_prod = math.lcm(*nums) * max(nums)
        
        for i in range(n):
            prod = 1
            l = 1
            g = 0
            for j in range(i, n):
                prod *= nums[j]
                if prod > max_possible_prod:
                    break
                l = math.lcm(l, nums[j])
                g = math.gcd(g, nums[j])
                
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                    
        return ans
