# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head

        fast = head

        if not head or not head.next: 
            return False

        while slow and fast: 
            slow = slow.next
            fast = fast.next 
            fast = fast.next

            if (fast and slow) and slow.val == fast.val: # Can't be the condition
                return True
                
    
        
        return False

            

        