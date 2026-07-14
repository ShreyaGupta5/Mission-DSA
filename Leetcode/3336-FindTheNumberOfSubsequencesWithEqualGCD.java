import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int subsequencePairCount(int[] nums) {
        int maxVal = Arrays.stream(nums).max().getAsInt();
        int n = nums.length;
        
        // Memoization table: mem[i][gcd1][gcd2]
        Integer[][][] mem = new Integer[n][maxVal + 1][maxVal + 1];

        return solve(nums, 0, 0, 0, mem);
    }

    private int solve(int[] nums, int i, int gcd1, int gcd2, Integer[][][] mem) {
        // Base case: if we process all elements, check if both subsequences 
        // are non-empty and if their GCDs are equal.
        if (i == nums.length) {
            return (gcd1 > 0 && gcd1 == gcd2) ? 1 : 0;
        }

        // Return cached result
        if (mem[i][gcd1][gcd2] != null) {
            return mem[i][gcd1][gcd2];
        }

        // 1. Skip nums[i]
        long count = solve(nums, i + 1, gcd1, gcd2, mem);

        // 2. Pick nums[i] for the first subsequence
        long take1 = solve(nums, i + 1, gcd(gcd1, nums[i]), gcd2, mem);

        // 3. Pick nums[i] for the second subsequence
        long take2 = solve(nums, i + 1, gcd1, gcd(gcd2, nums[i]), mem);

        // Store and return the result modulo 10^9 + 7
        return mem[i][gcd1][gcd2] = (int) ((count + take1 + take2) % MOD);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
