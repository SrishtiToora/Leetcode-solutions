# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack=[]
        root=TreeNode(preorder[0])
        stack.append(root)
        for i in range(1,len(preorder)):
            if stack[-1].val > preorder[i]:
                stack[-1].left=TreeNode(preorder[i])
                stack.append(stack[-1].left)
                
            else:
                while len(stack)>0 and stack[-1].val<preorder[i]:
                    last=stack.pop(-1)
                last.right=TreeNode(preorder[i])
                stack.append(last.right)
        
        return root
                