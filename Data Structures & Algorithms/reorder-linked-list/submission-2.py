# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next
            fast = fast.next            
            slow = slow.next

        p2 = slow.next
        slow.next = None
        curr = self.reverseList(p2)

        start = head

        while start and curr:
            nextLeftNode = start.next
            nextRightNode = curr.next
            start.next = curr
            curr.next = nextLeftNode
            start = nextLeftNode
            curr = nextRightNode

        
    
            
        

    
    def reverseList(self, head):
        prev = None
        node = head

        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        
        return prev





        
        



        