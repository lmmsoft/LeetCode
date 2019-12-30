### [1302\. Deepest Leaves Sum](https://leetcode.com/contest/biweekly-contest-16/problems/deepest-leaves-sum/)

Difficulty: **Medium**

Given a binary tree, return the sum of values of its deepest leaves.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png)**

```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```

**Constraints:**

*   The number of nodes in the tree is between `1` and `10^4`.
*   The value of nodes is between `1` and `100`.

#### Solution
- 水题
Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        s = 0
        nodes = [root]
        next_nodes = []
        while nodes:
            for n in nodes:
                s += n.val
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
            if not next_nodes:
                return s
            
            nodes = next_nodes
            next_nodes = []
            s=0
```