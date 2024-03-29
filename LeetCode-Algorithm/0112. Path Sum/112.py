# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            # reach bottom
            if root.val == targetSum:
                return True
            return False

        targetSum2 = targetSum - root.val

        if root.left:
            l = self.hasPathSum(root.left, targetSum2)
            if l:
                return True
        if root.right:
            r = self.hasPathSum(root.right, targetSum2)
            if r:
                return True
        return False