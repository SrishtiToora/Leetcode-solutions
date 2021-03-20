# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res=[]
        ans=[]
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
                if curr.right:
                    q.put(curr.right)
                if curr.left:
                    q.put(curr.left)
                
                size-=1
            ans.append(a[0])
            if len(a)!=0:
                res.append(a)
        return ans