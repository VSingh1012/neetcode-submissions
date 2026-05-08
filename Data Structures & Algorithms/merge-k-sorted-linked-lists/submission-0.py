# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None
        # Taking list of lists and making smaller and smaller

        while len(lists) > 1:
            mergedList = [] 

            for x in range(0, len(lists), 2):
                l1 = lists[x]
                l2 = lists[x + 1] if x + 1 < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2))

            lists = mergedList

        return lists[0]




    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
    
        
        while list1 and list2:
            if list1.val <= list2.val: 
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next

            tail = tail.next 

        if list2:
            tail.next = list2
        elif list1:
            tail.next = list1
        
        return dummy.next
              