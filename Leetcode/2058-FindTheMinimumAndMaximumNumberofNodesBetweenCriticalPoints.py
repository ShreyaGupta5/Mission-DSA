# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_distance = float('inf')
        first_cp_index = -1
        prev_cp_index = -1
        
        prev_node = head
        curr_node = head.next
        index = 1
        
        while curr_node and curr_node.next:
            next_node = curr_node.next
            
            # Check for local maxima or local minima
            is_critical = (
                (curr_node.val > prev_node.val and curr_node.val > next_node.val) or
                (curr_node.val < prev_node.val and curr_node.val < next_node.val)
            )
            
            if is_critical:
                if first_cp_index == -1:
                    first_cp_index = index
                else:
                    min_distance = min(min_distance, index - prev_cp_index)
                prev_cp_index = index
                
            prev_node = curr_node
            curr_node = next_node
            index += 1
            
        # If fewer than two critical points exist
        if prev_cp_index == first_cp_index:
            return [-1, -1]
            
        max_distance = prev_cp_index - first_cp_index
        return [min_distance, max_distance]
