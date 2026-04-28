class Solution:
    def minOperations(self, grid, x):
        nums = []
        
        # Step 1: Flatten grid
        for row in grid:
            for num in row:
                nums.append(num)
        
        # Step 2: Check feasibility
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Step 3: Sort and find median
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Step 4: Count operations
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations
