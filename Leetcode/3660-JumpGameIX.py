class Solution:
    def maxValue(self, nums):
        n = len(nums)

        # prefix maximum
        pre_max = [0] * n
        pre_max[0] = nums[0]

        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        ans = [0] * n
        suf_min = float('inf')

        # traverse from right to left
        for i in range(n - 1, -1, -1):

            # if smaller element exists on right
            if pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]

            suf_min = min(suf_min, nums[i])

        return ans
