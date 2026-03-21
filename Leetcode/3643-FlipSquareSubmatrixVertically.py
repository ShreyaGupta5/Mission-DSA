class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        # For each column in the submatrix
        for j in range(y, y + k):
            top = x
            bottom = x + k - 1
            
            # Reverse column (vertical swap)
            while top < bottom:
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
                top += 1
                bottom -= 1
        
        return grid
