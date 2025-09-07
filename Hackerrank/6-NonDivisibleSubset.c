#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) { return a > b ? a : b; }

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;

    int freq = (int)calloc(k, sizeof(int));
    if (!freq) return 0;

    for (int i = 0; i < n; ++i) {
        int x; scanf("%d", &x);
        int r = x % k;
        if (r < 0) r += k; 
        freq[r]++;
    }

    int count = 0;

    if (freq[0] > 0) count++;

    for (int i = 1; i <= k/2; ++i) {
        int j = k - i;
        if (i == j) {
            
            if (freq[i] > 0) count++;
        } else {
            count += max(freq[i], freq[j]);
        }
    }

    printf("%d\n", count);

    free(freq);
    return 0;
}
