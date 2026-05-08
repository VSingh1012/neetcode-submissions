# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    from collections import deque

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        res = [] 
        q = deque()
        q.append(root) 

        while q:
            node = q.popleft()
            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
         
        return ",".join(res)
                 


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serialized = data.split(",")
        if serialized[0] == "null":
            return None

        # list form of the nodes, now we need an algorithm 
        root = TreeNode(int(serialized[0]))
        q = deque([root]) 
        index = 1        

        while q:
            node = q.popleft()

            if (serialized[index] != "null"):
                node.left = TreeNode(int(serialized[index]))
                q.append(node.left)
            index += 1
            if (serialized[index] != "null"):
                node.right = TreeNode(int(serialized[index]))
                q.append(node.right)
            index += 1 

        return root


        

