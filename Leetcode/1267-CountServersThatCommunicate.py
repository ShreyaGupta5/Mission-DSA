class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Arrays to store the total number of servers in each row and column
        row_counts = [0] * m
        col_counts = [0] * n
        
        # First pass: Count servers in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        communicating_servers = 0
        
        # Second pass: Count servers that can communicate
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # A server can communicate if there is more than 1 server in its row or column
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers
