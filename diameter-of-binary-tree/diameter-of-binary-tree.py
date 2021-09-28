# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res= -101
        def solve(node,res):
            
            if node is None:
                return 0
            left=solve(node.left,res)
            right=solve(node.right,res)
            
            temp= max(left,right)+1
            ans=max(temp, left+right+1)
            
            self.res=max(self.res,ans)
            return temp
        # self.res= float("-inf")
        solve(root,self.res)
        return self.res -1
            
            # if not node:
            #     return 0
            # L=depth(node.left)
            # R=depth(node.right)
            # self.ans=max(self.ans,L+R+1)
            # return max(L,R)+1
        # depth(root)
        # return self.ans-1
        