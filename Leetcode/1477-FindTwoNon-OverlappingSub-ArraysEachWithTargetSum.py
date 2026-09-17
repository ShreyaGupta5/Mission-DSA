class Solution:
    def minSumOfLengths(self, arr, target):

        n = len(arr)

        # dp[i] = shortest valid subarray ending at or before i
        dp = [float('inf')] * n

        # prefix sum -> index
        prefix = {0: -1}

        curr_sum = 0
        ans = float('inf')

        for i in range(n):

            curr_sum += arr[i]

            # Check if there is a subarray with sum = target
            if curr_sum - target in prefix:

                left = prefix[curr_sum - target]
                length = i - left

                # If this is not the first valid subarray,
                # combine it with the best previous one
                if left >= 0 and dp[left] != float('inf'):
                    ans = min(ans, length + dp[left])

                # Store the shortest valid subarray ending at i
                if i == 0:
                    dp[i] = length
                else:
                    dp[i] = min(dp[i - 1], length)

            else:
                # No new subarray ending at i
                if i > 0:
                    dp[i] = dp[i - 1]

            # Store prefix sum
            if curr_sum not in prefix:
                prefix[curr_sum] = i

        return -1 if ans == float('inf') else ans
