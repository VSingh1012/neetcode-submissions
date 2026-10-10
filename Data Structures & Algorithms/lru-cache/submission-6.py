
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = None 
        self.tail = None
        self.hsh = {} # hash to hold the addresses of the pointers to the nodes

    def get(self, key: int) -> int:

        node = self.hsh.get(key, None)
        if not node:
            return -1 

        # node exists and is now "used"
        # now we move to the back after making sure node isn't already there
        if self.tail and self.tail is not node:
            tail = self.tail
            tail.next = node
            # for moving existing node (from front or middle)
            _prev = node.prev
            _next = node.next
            if _prev:
                _prev.next = _next
            _next.prev = _prev
            if node is self.head: 
                self.head = _next
            node.next = None 
            node.prev = tail         
            self.tail = node

        # val -> (key, value)        
        return node.val[1]

    

    def put(self, key: int, value: int) -> None:
        node = self.hsh.get(key, None)

        new_node = None

        if node:
            # node exists update value
            node.val = (key, value)
            if node is self.tail: # don't need to move it around (node is at the back already when you update it)
                return
            new_node = node
        else:
            new_node = Node((key, value))
            self.hsh[key] = new_node
            self.size += 1

            if not self.head:
                self.head = new_node

        # Add the new node to the back of the list then decide what we need to do
        if self.tail:
            tail = self.tail
            tail.next = new_node

            # for moving existing node (from front or middle)
            _prev = new_node.prev
            _next = new_node.next
            if _prev: # means existing node
                _prev.next = _next
            if _next:
                _next.prev = _prev

            # updating the head pointer
            if new_node is self.head:
                self.head = _next

            new_node.next = None 
            new_node.prev = tail 
        self.tail = new_node


        # now check the size of the current list
        if self.size > self.capacity:
            # disconnect the head node and set new head
            del self.hsh[self.head.val[0]]
            head = self.head
            head_next = head.next
            head.next = None
            head_next.prev = None
            self.head = head_next
            self.size -= 1




        
            



            






