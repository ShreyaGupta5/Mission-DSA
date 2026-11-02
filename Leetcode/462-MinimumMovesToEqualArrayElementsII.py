class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort the array to easily find the median
        nums.sort()
        
        # The median is at the middle index
        # Using integer division // 2 or bitwise shift >> 1
        median = nums[len(nums) // 2]
        
        # Calculate the total moves required
        return sum(abs(num - median) for num in nums)
