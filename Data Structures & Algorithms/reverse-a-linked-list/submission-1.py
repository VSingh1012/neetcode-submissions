# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # one for the start and one for the end   
        start = head
        prev = None

    
        # n1 -> n2 -> n3

        while start:
            next_ptr = start.next
            start.next = prev
            prev = start
            start = next_ptr



        return prev
            
            

        
            
            
        


        # 0 1 2 3

        # n1 -> n2 -> n3 -> n4
        # n4 -> n3 -> n2 -> n1

        
