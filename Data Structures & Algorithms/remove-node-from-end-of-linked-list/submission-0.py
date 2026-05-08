# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # greedy approach 

        # [DN, 5] n = 1

        dummy = ListNode()

        dummy.next = head

        right = head

        o = 0

        while o < n: 
            right = right.next
            o += 1 

        left = dummy

        while right: 
            left = left.next
            right = right.next

        leftNext = left.next
        left.next = leftNext.next

        return dummy.next


        