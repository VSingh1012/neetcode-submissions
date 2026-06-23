# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node):

            if not node:
                return 

            if node.right or node.left:
                left = node.left 
                right = node.right
                node.left = right
                node.right = left

                dfs(node.left)
                dfs(node.right)


        dfs(root)

        return root        


        


        





            

            