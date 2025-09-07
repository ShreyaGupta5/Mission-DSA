#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char number[105];
    int remainder;
} Node;

typedef struct Queue {
    Node data[10000];
    int front;
    int rear;
} Queue;

void enqueue(Queue *q, Node val) {
    q->data[q->rear++] = val;
}

Node dequeue(Queue *q) {
    return q->data[q->front++];
}

int is_empty(Queue *q) {
    return q->front == q->rear;
}

void find_special_multiple(int n) {
    int visited[505] = {0};

    Queue q = {0};
    Node start;
    strcpy(start.number, "9");
    start.remainder = 9 % n;

    enqueue(&q, start);
    visited[start.remainder] = 1;

    while (!is_empty(&q)) {
        Node current = dequeue(&q);

        if (current.remainder == 0) {
            printf("%s\n", current.number);
            return;
        }

        Node next0;
        strcpy(next0.number, current.number);
        strcat(next0.number, "0");
        next0.remainder = (current.remainder * 10) % n;

        if (!visited[next0.remainder]) {
            visited[next0.remainder] = 1;
            enqueue(&q, next0);
        }

        Node next9;
        strcpy(next9.number, current.number);
        strcat(next9.number, "9");
        next9.remainder = (current.remainder * 10 + 9) % n;

        if (!visited[next9.remainder]) {
            visited[next9.remainder] = 1;
            enqueue(&q, next9);
        }
    }
}

int main() {
    int t, n;
    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);
        find_special_multiple(n);
    }

    return 0;
}
