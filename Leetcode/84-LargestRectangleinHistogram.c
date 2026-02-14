#include <stdio.h>
#include <stdlib.h>

typedef struct StackNode {
    int index;
    struct StackNode* next;
} StackNode;

typedef struct Stack {
    StackNode* top;
} Stack;

Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = NULL;
    return stack;
}

int isEmpty(Stack* stack) {
    return stack->top == NULL;
}

void push(Stack* stack, int index) {
    StackNode* newNode = (StackNode*)malloc(sizeof(StackNode));
    newNode->index = index;
    newNode->next = stack->top;
    stack->top = newNode;
}

int pop(Stack* stack) {
    if (isEmpty(stack)) {
        return -1;
    }
    StackNode* temp = stack->top;
    int index = temp->index;
    stack->top = temp->next;
    free(temp);
    return index;
}

int peek(Stack* stack) {
    if (isEmpty(stack)) {
        return -1; 
    return stack->top->index;
}

int largestRectangleArea(int* heights, int heightsSize) {
    Stack* stack = createStack();
    int maxArea = 0;
    int i = 0;

    while (i < heightsSize) {
        if (isEmpty(stack) || heights[peek(stack)] <= heights[i]) {
            push(stack, i);
            i++;
        } else {
            int h = heights[pop(stack)];
            int w = isEmpty(stack) ? i : i - peek(stack) - 1;
            if (h * w > maxArea) {
                maxArea = h * w;
            }
        }
    }

    while (!isEmpty(stack)) {
        int h = heights[pop(stack)];
        int w = isEmpty(stack) ? i : i - peek(stack) - 1;
        if (h * w > maxArea) {
            maxArea = h * w;
        }
    }

    while (!isEmpty(stack)) {
        pop(stack);
    }
    free(stack);

    return maxArea;
}
