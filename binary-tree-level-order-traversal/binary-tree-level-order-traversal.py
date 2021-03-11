# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        q=queue.Queue()
        if root is None:
            return None
        q.put(root)
        print(q)
        while not q.empty():
            a=[]
            size=q.qsize()
            while size!=0:
                curr=q.get()
                a.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                size-=1
            if len(a)!=0:
                res.append(a)
        return res
            