class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Find all valid divisors of n in O(sqrt(n)) time
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        ans = 0
        
        # Step 2: Validate each divisor k
        for k in divisors:
            valid = True
            last_max = -float('inf')
            
            for i in range(0, n, k):
                drops = 0
                block_min = nums[i]
                block_max = nums[i]
                
                # Check circular drops and track local min/max within the block
                for j in range(k):
                    curr = nums[i + j]
                    nxt = nums[i + (j + 1) % k]  # Wraps around to the start of the block
                    
                    if curr > nxt:
                        drops += 1
                    if curr < block_min:
                        block_min = curr
                    if curr > block_max:
                        block_max = curr
                
                # Conditions for a valid partition:
                # 1. At most 1 drop allows a block to be cyclically sorted.
                # 2. Monotonicity across blocks (current min must be >= previous max).
                if drops > 1 or block_min < last_max:
                    valid = False
                    break
                    
                last_max = block_max
                
            if valid:
                ans += k
                
        return ans
