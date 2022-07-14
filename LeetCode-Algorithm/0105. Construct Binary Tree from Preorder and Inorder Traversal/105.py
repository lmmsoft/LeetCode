# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        mid = preorder[0]

        mid_index_in_inorder = inorder.index(mid)

        inorder_left = inorder[:mid_index_in_inorder]
        inorder_right = inorder[mid_index_in_inorder + 1:]

        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # print(f"mid:{mid}\ninorder_left:{inorder_left}\npreorder_left:{preorder_left}\ninorder_right:{inorder_right}\npreorder_right:{preorder_right}\n")

        # build left
        left_node = None
        if inorder_left:
            left_node = self.buildTree(preorder_left, inorder_left)

        # build right
        right_node = None
        if preorder_right:
            right_node = self.buildTree(preorder_right, inorder_right)

        return TreeNode(mid, left_node, right_node)

    def buildTree2_short_solution(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = Solution().buildTree(preorder, inorder)
    pass
