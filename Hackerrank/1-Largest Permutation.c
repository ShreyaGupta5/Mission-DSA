#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int* largestPermutation(int k, int arr_count, int* arr) {
    
    int* pos = (int*)malloc((arr_count + 1) * sizeof(int));
    for (int i = 0; i < arr_count; i++) {
        pos[arr[i]] = i; 
    }

    for (int i = 0; i < arr_count && k > 0; i++) {
        int target_val = arr_count - i; 

        if (arr[i] != target_val) {
            
            int target_idx = pos[target_val];

          
            pos[arr[i]] = target_idx;
            pos[target_val] = i;

           
            swap(&arr[i], &arr[target_idx]);

            k--; 
        }
    }
    free(pos); 
    return arr;
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int* arr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int* result = largestPermutation(k, n, arr);

    for (int i = 0; i < n; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    free(arr); 
    return 0;
}
