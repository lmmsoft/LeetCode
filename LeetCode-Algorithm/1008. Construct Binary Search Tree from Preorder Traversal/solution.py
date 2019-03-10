from typing import List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        li: Dict[TreeNode] = {}
        li[0] = root
        cur = 0

        for i in range(1, len(preorder)):
            t = TreeNode(preorder[i])
            if t.val < li[cur].val:
                li[cur].left = t

                li[cur + 1] = t
                cur += 1
            else:
                cur2 = cur - 1
                while True:
                    if cur2 == -1 or li[cur2].val > t.val:
                        # right of cur1
                        li[cur2 + 1].right = t
                        li[cur2 + 1] = t
                        cur = cur2 + 1
                        break
                    else:
                        cur2 -= 1

        return root


if __name__ == '__main__':
    ans = Solution().bstFromPreorder([7, 2, 20, 12, 8])
    Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
