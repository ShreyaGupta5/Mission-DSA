class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # Create sorted tuples of (digit_sum, value)
        sorted_pairs = sorted((get_digit_sum(x), x) for x in nums)
        
        # Map each target value to its correct index in the sorted order
        target_map = {val: i for i, (_, val) in enumerate(sorted_pairs)}
        
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if visited[i] or target_map[nums[i]] == i:
                continue
            
            # Cycle detection
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = target_map[nums[j]]
                cycle_size += 1
                
            ans += (cycle_size - 1)
            
        return ans
