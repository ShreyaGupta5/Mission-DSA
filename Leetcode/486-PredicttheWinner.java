class Solution {
    public boolean predictTheWinner(int[] nums) {
        int n = nums.length;
        // Even number of elements means Player 1 can always win by choosing all even or odd indices
        if (n % 2 == 0) {
            return true;
        }
        
        int[] dp = nums.clone();
        
        // Build the DP state from smaller subarrays to the larger target array
        for (int diff = 1; diff < n; diff++) {
            for (int left = n - 1 - diff; left >= 0; left--) {
                int right = left + diff;
                // Maximum relative score difference current player can achieve
                dp[right] = Math.max(nums[left] - dp[right], nums[right] - dp[right - 1]);
            }
        }
        
        return dp[n - 1] >= 0;
    }
}
