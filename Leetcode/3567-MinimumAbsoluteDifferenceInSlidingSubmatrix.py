from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                values = []

                # collect k x k submatrix elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])

                # sort values
                values.sort()

                # find minimum difference between distinct values
                min_diff = float('inf')
                for t in range(1, len(values)):
                    if values[t] != values[t - 1]:
                        min_diff = min(min_diff, values[t] - values[t - 1])

                result[i][j] = min_diff if min_diff != float('inf') else 0

        return result
