class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        MOD = 10**9 + 7
      
        # Initialize DP table: dp[i][j] = [min_product, max_product] at cell (i, j)
        # Each cell stores both minimum and maximum products to handle negative numbers
        dp = [[[grid[0][0], grid[0][0]] for _ in range(cols)] for _ in range(rows)]
      
        # Initialize first column (can only come from above)
        for row in range(1, rows):
            prev_product = dp[row - 1][0][0]
            current_value = grid[row][0]
            dp[row][0][0] = prev_product * current_value  # min product
            dp[row][0][1] = prev_product * current_value  # max product
      
        # Initialize first row (can only come from left)
        for col in range(1, cols):
            prev_product = dp[0][col - 1][0]
            current_value = grid[0][col]
            dp[0][col][0] = prev_product * current_value  # min product
            dp[0][col][1] = prev_product * current_value  # max product
      
        # Fill the DP table for remaining cells
        for row in range(1, rows):
            for col in range(1, cols):
                current_value = grid[row][col]
              
                if current_value >= 0:
                    # For non-negative values:
                    # - Minimum comes from multiplying with previous minimum
                    # - Maximum comes from multiplying with previous maximum
                    min_from_above = dp[row - 1][col][0]
                    min_from_left = dp[row][col - 1][0]
                    dp[row][col][0] = min(min_from_above, min_from_left) * current_value
                  
                    max_from_above = dp[row - 1][col][1]
                    max_from_left = dp[row][col - 1][1]
                    dp[row][col][1] = max(max_from_above, max_from_left) * current_value
                else:
                    # For negative values:
                    # - Minimum comes from multiplying with previous maximum (sign flip)
                    # - Maximum comes from multiplying with previous minimum (sign flip)
                    max_from_above = dp[row - 1][col][1]
                    max_from_left = dp[row][col - 1][1]
                    dp[row][col][0] = max(max_from_above, max_from_left) * current_value
                  
                    min_from_above = dp[row - 1][col][0]
                    min_from_left = dp[row][col - 1][0]
                    dp[row][col][1] = min(min_from_above, min_from_left) * current_value
      
        # Get the maximum product at the bottom-right cell
        max_product = dp[-1][-1][1]
      
        # Return -1 if the maximum product is negative, otherwise return modulo result
        return -1 if max_product < 0 else max_product % MOD
