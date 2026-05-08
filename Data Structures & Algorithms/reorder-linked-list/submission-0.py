# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

     
         

        l2 = slow.next

        prev = slow.next = None

        while l2:
            nextNode = l2.next
            l2.next = prev
            prev = l2
            l2 = nextNode
    

        first, second = head, prev

        while second: 
            firstNext, secondNext = first.next, second.next
            first.next = second
            second.next = firstNext
            first, second = firstNext, secondNext 
           






        

        

        



        

        

        




        