# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val==key:
            if root.left is None and root.right is None:
                return None
            elif not root.left and root.right:
                return root.right
            elif not root.right and root.left:
                return root.left
            pnt=root.right
            while pnt.left:
                pnt=pnt.left
            root.val=pnt.val
            root.right=self.deleteNode(root.right,root.val)
        return root
            
        