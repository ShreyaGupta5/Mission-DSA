#include <stdlib.h> 
#include <string.h> 
typedef struct {
    int* prefix_products;
    int size;
    int capacity;
} ProductOfNumbers;

ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* obj = (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));
    obj->capacity = 16; 
    obj->prefix_products = (int*)malloc(sizeof(int) * obj->capacity);
    obj->prefix_products[0] = 1;
    obj->size = 1;
    return obj;
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    if (num == 0) {

        obj->size = 1;
        obj->prefix_products[0] = 1;
    } else {
       
        if (obj->size == obj->capacity) {
            obj->capacity *= 2;
            obj->prefix_products = (int*)realloc(obj->prefix_products, sizeof(int) * obj->capacity);
        }
      
        obj->prefix_products[obj->size] = obj->prefix_products[obj->size - 1] * num;
        obj->size++;
    }
}


int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    if (k >= obj->size) {
        return 0;
    }
    return obj->prefix_products[obj->size - 1] / obj->prefix_products[obj->size - 1 - k];
}

// Destructor
void productOfNumbersFree(ProductOfNumbers* obj) {
    free(obj->prefix_products);
    free(obj);
}
