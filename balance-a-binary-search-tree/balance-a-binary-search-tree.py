# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res=[]
        self.helper(root,res)
        print(res)
        return self.sortedArrayToBST(res)
        
    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid=len(nums)//2
        node=TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
    