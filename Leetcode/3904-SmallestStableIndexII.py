class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Precompute the minimum values from right to left (Suffix Min)
        right_min = [0] * n
        right_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])
            
        # Step 2: Iterate left to right, maintaining the running prefix maximum
        left_max = float('-inf')
        for i in range(n):
            left_max = max(left_max, nums[i])
            
            # Check the stability condition
            if left_max - right_min[i] <= k:
                return i  # Return immediately as we want the smallest index
                
        return -1
