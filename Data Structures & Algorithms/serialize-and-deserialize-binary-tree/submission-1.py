# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        res = []

    
        q = collections.deque()
        q.append(root)

        while q:
            curr_node = q.popleft()
            if curr_node: 
                res.append(str(curr_node.val))
                q.append(curr_node.left)
                q.append(curr_node.right)
            else:
                res.append("N")

        return ",".join(res)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:


        serialized_data = data.split(",")

        if (serialized_data[0] == "N"):
            return None

        # [1,2,3,null,null,4,5]

        root = TreeNode(int(serialized_data[0]))
        index = 1

        q = collections.deque([root])

        while q:
            node = q.popleft()

            if (serialized_data[index] != "N"):
                node.left = TreeNode(int(serialized_data[index]))
                q.append(node.left)
            index += 1

            if (serialized_data[index] != "N"):
                node.right = TreeNode(int(serialized_data[index]))
                q.append(node.right)
               
            index += 1


        return root
            
            

            

        

        





            
            


        


