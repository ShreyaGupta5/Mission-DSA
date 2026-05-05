class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases: empty list, single node, or no rotation
        if not head or not head.next or k == 0:
            return head
        
        # 1. Calculate the length of the list and find the tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Make the list circular by connecting tail to head
        tail.next = head
        
        # 3. Find the new tail node: (length - k % length - 1)th node
        # 4. Find the new head node: (length - k % length)th node
        k = k % length
        steps_to_new_tail = length - k
        new_tail = tail # Start at old tail
        
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # 5. Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
