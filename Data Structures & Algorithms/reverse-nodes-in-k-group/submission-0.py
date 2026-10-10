# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head


        # FIRST PASS: go through and see how many groups there are
        fp = head
        i = 0
        while fp:
            i += 1
            fp = fp.next
        total_groups = i // k
        
        # Calculate pivots and initialize variables        
        pivot = dummy
        node = dummy.next 
        g = 0
        prev = None

        # Start reversing and keep track of groups

        while node and g < total_groups:
            for i in range(k):
                node_next = node.next
                node.next = prev
                prev = node
                node = node_next
                # reverse the links
            g += 1
            piv_next = pivot.next
            piv_next.next = node
            pivot.next = prev
            pivot = piv_next

        return dummy.next

         


        



    

    
        