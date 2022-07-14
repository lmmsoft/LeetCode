# [105\. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Description

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Hash Table](https://leetcode.com/tag/hash-table/), [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/), [Tree](https://leetcode.com/tag/tree/), [Binary Tree](https://leetcode.com/tag/binary-tree/)


Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return _the binary tree_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

**Constraints:**

*   `1 <= preorder.length <= 3000`
*   `inorder.length == preorder.length`
*   `-3000 <= preorder[i], inorder[i] <= 3000`
*   `preorder` and `inorder` consist of **unique** values.
*   Each value of `inorder` also appears in `preorder`.
*   `preorder` is **guaranteed** to be the preorder traversal of the tree.
*   `inorder` is **guaranteed** to be the inorder traversal of the tree.


## Solution

经典的二叉树题目，根据一棵树的前序遍历与中序遍历构造二叉树
中序遍历的第一个是当前树的根节点，可以在前序遍历里找到它，左边就是左子树，右边是右子树，依次递归，最后构建子树并层层返回即可


Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
​
        mid = preorder[0]
​
        mid_index_in_inorder = inorder.index(mid)
​
        inorder_left = inorder[:mid_index_in_inorder]
        inorder_right = inorder[mid_index_in_inorder + 1:]
​
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]
​
        # print(f"mid:{mid}\ninorder_left:{inorder_left}\npreorder_left:{preorder_left}\ninorder_right:{inorder_right}\npreorder_right:{preorder_right}\n")
​
        # build left
        left_node = None
        if inorder_left:
            left_node = self.buildTree(preorder_left, inorder_left)
​
        # build right
        right_node = None
        if preorder_right:
            right_node = self.buildTree(preorder_right, inorder_right)
​
        return TreeNode(mid, left_node, right_node)
```