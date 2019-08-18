### [1161\. Maximum Level Sum of a Binary Tree](https://leetcode.com/contest/weekly-contest-150/problems/maximum-level-sum-of-a-binary-tree/)
- https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
- https://leetcode.com/contest/weekly-contest-150/problems/maximum-level-sum-of-a-binary-tree/

Difficulty: **Medium**

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `X` such that the sum of all the values of nodes at level `X` is **maximal**.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/05/03/capture.JPG)**

```
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```

**Note:**

1.  The number of nodes in the given tree is between `1` and `10^4`.
2.  `-10^5 <= node.val <= 10^5`

#### Solution
- 题意：求二叉树哪一层的和最大，返回层数
- 解法 BFS

Language: **Python3**

```python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
​
​
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
​
        return mx_level
​
​
from typing import List, Optional
​
​
def array_to_tree_nodel(l: List[int]) -> Optional[TreeNode]:
    head: Optional[TreeNode] = None
    tree_node_list: List[Optional[TreeNode]] = [None] * len(l)
​
    for idx, val in enumerate(l):
        if val is None:
            continue
        node = TreeNode(val)
        if idx == 0:
            head = node
        else:
            parent_idx = (idx + 1) // 2 - 1
            if tree_node_list[parent_idx]:
                if idx % 2:  # left tree
                    tree_node_list[parent_idx].left = node
                else:
                    tree_node_list[parent_idx].right = node
​
        tree_node_list[idx] = node
​
    return head
​
​
if __name__ == '__main__':
    null = None
    assert Solution().maxLevelSum(array_to_tree_nodel([1, 7, 0, 7, -8, null, null])) == 2
​
```