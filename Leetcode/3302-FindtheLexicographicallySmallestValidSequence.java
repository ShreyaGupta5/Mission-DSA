class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        int[] suffix = new int[n + 1];
        suffix[n] = m;

        int j = m - 1;

        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1];

            if (j >= 0 && word1.charAt(i) == word2.charAt(j)) {
                suffix[i] = j;
                j--;
            }
        }

        int[] ans = new int[m];
        int k = 0;
        boolean changed = false;

        for (int i = 0; i < n && k < m; i++) {

            if (word1.charAt(i) == word2.charAt(k)) {
                ans[k++] = i;
            }
            else if (!changed) {
                // Use this index by changing word1[i]
                if (i + 1 <= n && suffix[i + 1] <= k + 1) {
                    ans[k++] = i;
                    changed = true;
                }
            }
        }

        if (k != m) {
            return new int[0];
        }

        return ans;
    }
}
