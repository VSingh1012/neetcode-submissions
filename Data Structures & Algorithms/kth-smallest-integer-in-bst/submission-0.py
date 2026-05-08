# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []

        def isSmallest(node):

            if not node:
                return 

            isSmallest(node.left)
            arr.append(node.val)
            isSmallest(node.right)


        
        isSmallest(root)
        return arr[k-1]




