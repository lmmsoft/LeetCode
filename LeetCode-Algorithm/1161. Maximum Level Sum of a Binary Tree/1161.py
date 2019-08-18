# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level, mx, mx_level = 0, 0, 0
        q = [root]
        while q:
            level += 1
            s = 0
            next = []
            while q:
                n = q.pop()
                s += n.val
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            q = next
            if s > mx:
                mx, mx_level = s, level

        return mx_level


from typing import List, Optional


def array_to_tree_nodel(l: List[int]) -> Optional[TreeNode]:
    head: Optional[TreeNode] = None
    tree_node_list: List[Optional[TreeNode]] = [None] * len(l)

    for idx, val in enumerate(l):
        if val is None:
            continue
        node = TreeNode(val)
        if idx == 0:
            head = node
        else:
            parent_idx = (idx + 1) // 2 - 1
            if tree_node_list[parent_idx]:
                if idx % 2:  # left tree
                    tree_node_list[parent_idx].left = node
                else:
                    tree_node_list[parent_idx].right = node

        tree_node_list[idx] = node

    return head


if __name__ == '__main__':
    null = None
    assert Solution().maxLevelSum(array_to_tree_nodel([1, 7, 0, 7, -8, null, null])) == 2
