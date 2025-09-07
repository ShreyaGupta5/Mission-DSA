#include <stdio.h>
#include <string.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    long long counts[1000]; 
    for (int i = 0; i < 1000; ++i) counts[i] = 0;

    for (int i = 0; i < n; ++i) {
        int m, d;
        scanf("%d %d", &m, &d);

        if (m < 2) continue;

        char s[16];
        snprintf(s, sizeof(s), "%d", d);

        int valid = 1;
        for (int k = 0; s[k] != '\0'; ++k) {
            int digit = s[k] - '0';
            if (digit >= m) { valid = 0; break; }
        }
        if (!valid) continue;

        int val = 0;
        for (int k = 0; s[k] != '\0'; ++k) {
            int digit = s[k] - '0';
            val = val * m + digit;
        }

        if (val >= 0 && val < 1000) counts[val]++; 
      
    }

    long long ans = 0;
    for (int v = 0; v < 1000; ++v) {
        if (counts[v] > 1) {
            ans += counts[v] * (counts[v] - 1) / 2;
        }
    }

    printf("%lld\n", ans);
    return 0;
}
