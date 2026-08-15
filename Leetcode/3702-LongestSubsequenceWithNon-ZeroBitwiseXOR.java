class Solution {
    public int longestSubsequence(int[] nums) {
        int xorSum = 0;
        boolean hasNonZero = false;
        
        for (int num : nums) {
            xorSum ^= num;
            if (num != 0) {
                hasNonZero = true;
            }
        }
        
        // If total XOR is already non-zero, take the whole array
        if (xorSum != 0) {
            return nums.length;
        }
        
        // If total XOR is zero, remove one non-zero element to make it non-zero
        if (hasNonZero) {
            return nums.length - 1;
        }
        
        // If the array consists entirely of zeros
        return 0;
    }
}
