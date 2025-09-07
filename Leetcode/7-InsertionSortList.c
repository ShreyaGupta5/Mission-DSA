struct ListNode* insertionSortList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head; 
    }

    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = NULL;

    struct ListNode* current = head;
    while (current != NULL) {
        struct ListNode* next_node = current->next;

        struct ListNode* prev = dummy;
        while (prev->next != NULL && prev->next->val < current->val) {
            prev = prev->next;
        }

       
        current->next = prev->next;
        prev->next = current;

        current = next_node; 
    }

    return dummy->next; 
}
