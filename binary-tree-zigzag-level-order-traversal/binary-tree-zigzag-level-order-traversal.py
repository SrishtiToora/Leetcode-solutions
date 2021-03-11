# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        res=[]
        level=0
        self.zigzag(root,level,res)
        return res
        
    def zigzag(self,root,level,res):
        if root is None:
            return None
        if len(res)<level+1:
            res.append([])
        if level%2==1:
            res[level].append(root.val)
        else:
            res[level].insert(0,root.val)
        self.zigzag(root.right,level+1,res)
        self.zigzag(root.left,level+1,res)
        print(res)