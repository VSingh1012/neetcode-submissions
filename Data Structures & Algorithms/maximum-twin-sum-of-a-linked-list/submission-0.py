# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        n = 0
        stk = []
        start = head
        maxSum = 0
        # calculates the n 
        while start: # O(n)
            n += 1
            start = start.next
        # idk how to do this in one pass

        # second pass for twin sums
        node = head

        for i in range(n):
            if stk and i == stk[-1][1]:
                maxSum = max(maxSum, node.val + stk.pop()[0])
            else:   
                stk.append((node.val, (n - i - 1)))

            node = node.next


        return maxSum
            

                









        


