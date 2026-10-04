"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        copies = {} # key is the curr_pointer, 
        fp = head

        # two pass attempt
        while fp:
            new_node = Node(fp.val)
            copies[fp] = new_node
            fp = fp.next

        sp = head # second pass

        while sp:
            copies[sp].next = copies[sp.next] if sp.next else None
            copies[sp].random = copies[sp.random] if sp.random else None
            sp = sp.next

        
        return copies[head] if head else None


    












