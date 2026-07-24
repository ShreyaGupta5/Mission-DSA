class Solution {

    private void fwht(int[] a) {
        int n = a.length;

        for (int len = 1; len < n; len <<= 1) {
            for (int i = 0; i < n; i += len << 1) {
                for (int j = 0; j < len; j++) {
                    int x = a[i + j];
                    int y = a[i + j + len];
                    a[i + j] = x + y;
                    a[i + j + len] = x - y;
                }
            }
        }
    }

    public int uniqueXorTriplets(int[] nums) {

        int SIZE = 2048;     // 2^11 > 1500

        int[] f = new int[SIZE];

        boolean[] vis = new boolean[SIZE];
        for (int x : nums) {
            if (!vis[x]) {
                vis[x] = true;
                f[x] = 1;
            }
        }

        fwht(f);

        for (int i = 0; i < SIZE; i++) {
            f[i] = f[i] * f[i] * f[i];
        }

        fwht(f);

        int ans = 0;

        for (int x : f) {
            if (x != 0) ans++;
        }

        return ans;
    }
}
