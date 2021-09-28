# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy=cur=TreeNode()
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop(-1)
            cur.right=root
            cur=cur.right
            root=root.right
            cur.left=None
        return dummy.right