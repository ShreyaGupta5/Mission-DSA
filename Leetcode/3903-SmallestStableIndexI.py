class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Store minimum from i to the end
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # Maximum from start to i
        left = 0

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1
