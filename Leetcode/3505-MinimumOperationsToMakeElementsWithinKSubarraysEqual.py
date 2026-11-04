class Solution:

  def minOperations(self, nums: list[int], x: int, k: int) -> int:
    n = len(nums)

    # 1. Coordinate Compression to handle large values in Fenwick Tree
    unique_vals = sorted(list(set(nums)))
    val_to_idx = {v: i + 1 for i, v in enumerate(unique_vals)}
    m = len(unique_vals)

    # Fenwick Trees: one for counting frequencies, one for maintaining actual sums
    bit_count = [0] * (m + 1)
    bit_sum = [0] * (m + 1)

    def update(idx, count_delta, sum_delta):
      while idx <= m:
        bit_count[idx] += count_delta
        bit_sum[idx] += sum_delta
        idx += idx & (-idx)

    def query(idx):
      c, s = 0, 0
      while idx > 0:
        c += bit_count[idx]
        s += bit_sum[idx]
        idx -= idx & (-idx)
      return c, s

    def find_kth(target):
      # Binary lifting to find the 1-based index where prefix frequency reaches target
      idx = 0
      current_count = 0
      bit_mask = 1
      while bit_mask <= m:
        bit_mask <<= 1
      bit_mask >>= 1

      while bit_mask > 0:
        if (
            idx + bit_mask <= m
            and current_count + bit_count[idx + bit_mask] < target
        ):
          idx += bit_mask
          current_count += bit_count[idx]
        bit_mask >>= 1
      return idx + 1

    # Calculate optimal cost for each size-x window
    costs = [0] * (n - x + 1)
    target_left = (x + 1) // 2

    for i in range(n):
      # Add incoming element
      v = nums[i]
      idx = val_to_idx[v]
      update(idx, 1, v)

      # Remove outgoing element from sliding window
      if i >= x:
        old_v = nums[i - x]
        old_idx = val_to_idx[old_v]
        update(old_idx, -1, -old_v)

      # Calculate minimum L1 distance to the window median
      if i >= x - 1:
        median_idx = find_kth(target_left)
        median_val = unique_vals[median_idx - 1]

        # Elements less than or equal to median
        left_cnt, left_sum = query(median_idx)

        # Total elements currently in window
        total_cnt, total_sum = query(m)

        right_cnt = total_cnt - left_cnt
        right_sum = total_sum - left_sum

        # Total cost to make all window elements equal to median
        cost = (median_val * left_cnt - left_sum) + (
            right_sum - median_val * right_cnt
        )
        costs[i - x + 1] = cost

    # 2. Dynamic Programming to select k non-overlapping windows
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
      dp[i][0] = 0

    for i in range(1, n + 1):
      for j in range(1, k + 1):
        # Case A: Do not pick a subarray ending at index i-1
        dp[i][j] = dp[i - 1][j]
        # Case B: Pick a subarray of size x ending at index i-1
        if i >= x:
          if dp[i - x][j - 1] != float('inf'):
            dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + costs[i - x])

    return dp[n][k]
