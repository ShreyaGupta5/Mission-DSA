class Solution:
    def deleteMiddle(self, head):
        if not head.next:   # Only one node
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next  # Delete middle node

        return head
