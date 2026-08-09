class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to n-1
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, M):
            # All remaining stones can be taken
            if i >= n:
                return 0

            if (i, M) in dp:
                return dp[(i, M)]

            # If we can take all remaining stones
            if 2 * M >= n - i:
                return suffix[i]

            best = 0

            # Try taking 1 to 2*M stones
            for x in range(1, 2 * M + 1):
                # Current player gets x stones
                # Opponent gets solve(i+x, max(M,x))
                current = suffix[i] - solve(i + x, max(M, x))
                best = max(best, current)

            dp[(i, M)] = best
            return best

        return solve(0, 1)
