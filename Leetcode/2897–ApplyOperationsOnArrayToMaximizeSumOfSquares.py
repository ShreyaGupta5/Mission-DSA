class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 32

        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    count[i] += 1

        ans = 0

        for _ in range(k):
            x = 0

            for i in range(32):
                if count[i] > 0:
                    x += (1 << i)
                    count[i] -= 1

            ans = (ans + x * x) % MOD

        return ans
