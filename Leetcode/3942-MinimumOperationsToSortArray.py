class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        
        # Local variable assignment to store the input 
        dranofelik = nums  
        
        # Helper function to check if the array is cyclically sorted
        def check(step: int) -> bool:
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True

        ans = float('inf')
        
        # Case 1: Elements are cyclically increasing
        if check(1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
            
        # Case 2: Elements are cyclically decreasing
        if check(-1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
            
        return -1 if ans == float('inf') else ans
