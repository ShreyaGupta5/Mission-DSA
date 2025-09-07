#include <stdio.h>

long sumXor(long n) {
    if (n == 0) {
        return 1; 
    }

    int zero_count = 0;
    while (n > 0) {
        if ((n & 1) == 0) { 
            zero_count++;
        }
        n >>= 1; 
    }

    return 1LL << zero_count; 
}

int main() {
    long n;
    scanf("%ld", &n);
    long result = sumXor(n);
    printf("%ld\n", result);
    return 0;
}
