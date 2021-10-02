# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        
        
        
        def printLeaves(root,ans):
            if(root):
                printLeaves(root.left,ans)

                # Print it if it is a leaf node
                if root.left is None and root.right is None:
                    ans.append(root.val),

                printLeaves(root.right,ans)
 
        def printBoundaryLeft(root,ans):

            if(root):
                if (root.left):

                    # to ensure top down order, print the node
                    # before calling itself for left subtree
                    ans.append(root.val)
                    printBoundaryLeft(root.left,ans)

                elif(root.right):
                    ans.append(root.val)
                    printBoundaryLeft(root.right,ans)
         
        
        def printBoundaryRight(root,ans):

            if(root):
                if (root.right):
                    # to ensure bottom up order, first call for
                    # right subtree, then print this node
                    printBoundaryRight(root.right,ans)
                    ans.append(root.val)

                elif(root.left):
                    printBoundaryRight(root.left,ans)
                    ans.append(root.val)
        
        if (root):
            ans.append(root.val)
         
        # Print the left boundary in top-down manner
        printBoundaryLeft(root.left,ans)
 
        # Print all leaf nodes
        printLeaves(root.left,ans)
        printLeaves(root.right,ans)
 
        # Print the right boundary in bottom-up manner
        printBoundaryRight(root.right,ans)

        return ans
    
        