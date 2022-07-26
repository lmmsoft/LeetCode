# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def find(root, ts, li):

            if not root:
                return

            li = li.copy()
            li.append(root.val)

            if not root.left and not root.right:
                if root.val == ts:

                    self.l.append(li)
                return

            find(root.left, ts - root.val, li)
            find(root.right, ts - root.val, li)

        find(root, targetSum, [])
        return self.l