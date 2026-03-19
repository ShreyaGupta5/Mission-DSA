class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])

        # prefix count of X and Y
        px = [[0]*n for _ in range(m)]
        py = [[0]*n for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0

                top_x = px[i-1][j] if i > 0 else 0
                left_x = px[i][j-1] if j > 0 else 0
                diag_x = px[i-1][j-1] if i > 0 and j > 0 else 0

                top_y = py[i-1][j] if i > 0 else 0
                left_y = py[i][j-1] if j > 0 else 0
                diag_y = py[i-1][j-1] if i > 0 and j > 0 else 0

                px[i][j] = x + top_x + left_x - diag_x
                py[i][j] = y + top_y + left_y - diag_y

                # ✅ Correct condition
                if px[i][j] == py[i][j] and px[i][j] > 0:
                    count += 1

        return count
