class Solution:
    def maxPathScore(self, grid, k):   # ✅ FIXED NAME
        m, n = len(grid), len(grid[0])
        
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        def get_cost(val):
            return 0 if val == 0 else 1
        
        start_cost = get_cost(grid[0][0])
        if start_cost <= k:
            dp[0][0][start_cost] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                for cost, score in list(dp[i][j].items()):
                    
                    # move right
                    if j + 1 < n:
                        val = grid[i][j+1]
                        new_cost = cost + get_cost(val)
                        if new_cost <= k:
                            new_score = score + val
                            dp[i][j+1][new_cost] = max(
                                dp[i][j+1].get(new_cost, -1),
                                new_score
                            )
                    
                    # move down
                    if i + 1 < m:
                        val = grid[i+1][j]
                        new_cost = cost + get_cost(val)
                        if new_cost <= k:
                            new_score = score + val
                            dp[i+1][j][new_cost] = max(
                                dp[i+1][j].get(new_cost, -1),
                                new_score
                            )
        
        if not dp[m-1][n-1]:
            return -1
        
        return max(dp[m-1][n-1].values())
