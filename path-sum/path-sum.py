# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val==sum:
            return True
        else:
            if root.left is not None:
                root.left.val+=root.val
            if root.right is not None:
                root.right.val+=root.val
            return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        
            
        