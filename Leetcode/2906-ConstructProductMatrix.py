class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        # Step 1: Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        
        # Step 2: Prefix product
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
        # Step 3: Suffix product
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
        # Step 4: Result = prefix * suffix
        result_flat = [(prefix[i] * suffix[i]) % MOD for i in range(size)]
        
        # Step 5: Convert back to 2D grid
        result = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(result_flat[idx])
                idx += 1
            result.append(row)
        
        return result
