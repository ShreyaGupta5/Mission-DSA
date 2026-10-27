class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize an m x n grid filled with '#' (obstacles)
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        i, j = 0, 0
        grid[i][j] = '.'
        
        # Carve a path: move right across the first row, then down the last column
        # Or alternatively zig-zag or move right then down:
        while i < m - 1 or j < n - 1:
            if j < n - 1 and (i % 2 == 0 or i == m - 1):
                j += 1
            elif i < m - 1:
                i += 1
            elif j > 0:
                j -= 1
            grid[i][j] = '.'
            
        # Convert each row list into a string
        return ["".join(row) for row in grid]
