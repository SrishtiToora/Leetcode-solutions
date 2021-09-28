# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root,res):
            if root is None:
                return 0
            l=solve(root.left,res)
            r=solve(root.right,res)
            temp=max(max(l,r)+root.val, root.val)
            ans=max(temp,l+r+root.val)
            self.res=max(self.res,ans)
            return temp
        self.res=float('-inf')
        solve(root,self.res)
        return self.res
            