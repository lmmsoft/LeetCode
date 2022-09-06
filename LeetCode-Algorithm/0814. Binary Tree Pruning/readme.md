# [814\. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

## Description

Difficulty: **Medium**  

Related Topics: [Tree](https://leetcode.com/tag/tree/), [Depth-First Search](https://leetcode.com/tag/depth-first-search/), [Binary Tree](https://leetcode.com/tag/binary-tree/)


Given the `root` of a binary tree, return _the same tree where every subtree (of the given tree) not containing a_ `1` _has been removed_.

A subtree of a node `node` is `node` plus every node that is a descendant of `node`.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

```
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```

**Example 2:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

```
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```

**Example 3:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

```
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 200]`.
*   `Node.val` is either `0` or `1`.


## Solution

深搜，必须搜到根部，先处理左右子树，再判断左右中间是否有1

WA了一次，没处理好整棵树都是0的情况

如果直接使用原始的pruneTree方法作为递归函数，返回值需要修改，改成TreeNode， 不存在就是Node，存在就原始值

Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
​
​
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
​
        root_has_1 = self.has_1(root)
        if not root_has_1:
            return None
​
        return root
​
    def has_1(self, node: Optional[TreeNode]):
        # node is empty
        if not node:
            return False
​
        left_has_1 = self.has_1(node.left)
        if not left_has_1:
            node.left = None
​
        right_has_1 = self.has_1(node.right)
        if not right_has_1:
            node.right = None
​
        if node.val == 1 or left_has_1 or right_has_1:
            return True
        return False
​
​
​
​
```