# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, prev, cnt, max_cnt, result):
            if not root:
                return prev, cnt, max_cnt

            prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, result)
            if prev:
                if root.val == prev.val:
                    cnt += 1
                else:
                    cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
                del result[:]
                result.append(root.val)
            elif cnt == max_cnt:
                result.append(root.val)
            return inorder(root.right, root, cnt, max_cnt, result)

        if not root:
            return []
        result = []
        inorder(root, None, 1, 0, result)
        return result