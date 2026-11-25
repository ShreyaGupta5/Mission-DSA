from collections import Counter


class Solution:

  def smallestUniqueSubarray(self, nums: list[int]) -> int:
    n = len(nums)
    # Using a large prime base (> 10^5) and large prime modulo to avoid collisions
    base = 1315423911
    mod = (1 << 61) - 1

    # Precompute powers of base
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
      powers[i] = (powers[i - 1] * base) % mod

    def has_unique(length: int) -> bool:
      current_hash = 0
      for i in range(length):
        current_hash = (current_hash * base + nums[i]) % mod

      counts = Counter([current_hash])

      for i in range(1, n - length + 1):
        # Remove leftmost element and add the new rightmost element
        left_val = (nums[i - 1] * powers[length - 1]) % mod
        current_hash = (
            (current_hash - left_val) * base + nums[i + length - 1]
        ) % mod
        counts[current_hash] += 1

      return 1 in counts.values()

    left, right = 1, n
    ans = n

    while left <= right:
      mid = (left + right) // 2
      if has_unique(mid):
        ans = mid
        right = mid - 1
      else:
        left = mid + 1

    return ans
