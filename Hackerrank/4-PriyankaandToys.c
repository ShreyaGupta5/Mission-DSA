#include <stdio.h>
#include <stdlib.h> 
#include <limits.h> 

int compare(const void *a, const void *b) {
    return ((int)a - (int)b);
}

int toys(int w_count, int* w) {
    if (w_count == 0) {
        return 0;
    }

    qsort(w, w_count, sizeof(int), compare);

    int containers = 1;
    int current_container_min_weight = w[0];

    for (int i = 1; i < w_count; i++) {
        if (w[i] > current_container_min_weight + 4) {
    
            containers++;
            current_container_min_weight = w[i];
        }
    }

    return containers;
}

int main() {
    int n;
    scanf("%d", &n);

    int *w = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &w[i]);
    }

    int result = toys(n, w);
    printf("%d\n", result);

    free(w);
    return 0;
}
