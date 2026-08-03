class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            res = -float('inf')
            score = 0
            for k in range(i, min(i + 3, n)):
                score += stoneValue[k]
                res = max(res, score - dp(k + 1))
            
            memo[i] = res
            return res

        diff = dp(0)
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"
