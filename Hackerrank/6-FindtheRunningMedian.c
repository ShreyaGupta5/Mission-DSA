#include <stdio.h>
#include <stdlib.h>

void insertSorted(int *arr, int n, int val) {
    int i = n - 1;
    while (i >= 0 && arr[i] > val) {
        arr[i + 1] = arr[i];
        i--;
    }
    arr[i + 1] = val;
}

void printMedian(int *arr, int n) {
    double median;
    if (n % 2 == 0) {
        median = (arr[n / 2 - 1] + arr[n / 2]) / 2.0;
    } else {
        median = (double)arr[n / 2];
    }
    printf("%.1f\n", median);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input size.\n");
        return 1;
    }

    int *arr = (int *)malloc(n * sizeof(int));
    if (!arr) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    int size = 0;
    for (int i = 0; i < n; i++) {
        int val;
        if (scanf("%d", &val) != 1) {
            printf("Invalid input.\n");
            free(arr);
            return 1;
        }

        insertSorted(arr, size, val);
        size++;

        printMedian(arr, size);
    }

    free(arr);
    return 0;
}
