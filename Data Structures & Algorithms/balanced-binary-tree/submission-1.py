# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # struggling to find a way to connect the depths at each node to the boolean value of their balance bruh
        if not root:
            return True

        # calculates depth at a certain node
        def dfs(node):
            if not node:
                return 0

            return 1 + max(dfs(node.left), dfs(node.right))

        leftHeight = dfs(root.left)
        rightHeight = dfs(root.right)

        return self.isBalanced(root.left) and self.isBalanced(root.right) if abs(leftHeight - rightHeight) <= 1 else False

        

        

        


         
        



        
         







