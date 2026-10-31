class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        
        memo = {}
        
        def dfs(r, c, direction):
            # Out of bounds check
            if r >= m or c >= n:
                return 0
            
            # Memoization check
            if (r, c, direction) in memo:
                return memo[(r, c, direction)]
            
            # If the current cell is a mirror (1)
            if grid[r][c] == 1:
                if direction == 0:    # Entered moving Right -> Deflected Down
                    res = dfs(r + 1, c, 1)
                elif direction == 1:  # Entered moving Down -> Deflected Right
                    res = dfs(r, c + 1, 0)
                memo[(r, c, direction)] = res
                return res
            
            # Base Case: Reached the destination empty cell
            if r == m - 1 and c == n - 1:
                return 1
            
            # If the current cell is empty (0), we can choose either direction
            ways_right = dfs(r, c + 1, 0)
            ways_down = dfs(r + 1, c, 1)
            
            res = (ways_right + ways_down) % MOD
            memo[(r, c, direction)] = res
            return res
        
        # Start at (0, 0) with a dummy direction (-1) since it's the starting empty cell
        return dfs(0, 0, -1)
