# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, n1,n2):
            if root == None:
                return None
            elif root==n1 or root==n2:
                return root
            left=lca(root.left,n1,n2)
            right=lca(root.right,n1,n2)
            if left!= None and right!= None:
                return root
            elif left!=None:
                return left
            else:
                return right
        return lca(root,p,q)