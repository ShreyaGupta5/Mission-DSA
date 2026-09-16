class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Calculate C(n + k - 1, 2 * k)
        result = 1

        for i in range(1, 2 * k + 1):
            result = result * (n + k - i) // i

        return result % MOD
