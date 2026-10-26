class Solution:

  def countIslands(self, grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    count = 0

    def dfs(r, c):
      # Stack overflow protection in Python for large grids
      stack = [(r, c)]
      visited[r][c] = True
      total_val = 0

      while stack:
        curr_r, curr_c = stack.pop()
        total_val += grid[curr_r][curr_c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          nr, nc = curr_r + dr, curr_c + dc
          if 0 <= nr < m and 0 <= nc < n:
            if not visited[nr][nc] and grid[nr][nc] > 0:
              visited[nr][nc] = True
              stack.append((nr, nc))

      return total_val

    for i in range(m):
      for j in range(n):
        if grid[i][j] > 0 and not visited[i][j]:
          island_sum = dfs(i, j)
          if island_sum % k == 0:
            count += 1

    return count
