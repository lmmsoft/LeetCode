# 1008. Construct Binary Search Tree from Preorder Traversal
- https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
- https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/
- https://leetcode.com/contest/weekly-contest-127/problems/construct-binary-search-tree-from-preorder-traversal/
- https://leetcode-cn.com/contest/weekly-contest-127/problems/construct-binary-search-tree-from-preorder-traversal/

# Solution
- 二叉树，给先序遍历，要求返回二叉搜索树
- 我现推了递推的做法，用stack，有个小bug，比赛赛后几分钟改对了，很遗憾
- 比赛时应该想到递归的解法的，又短又好使
- 另外要注意比赛提交不能带上 class TreeNode:

- 解法1： 思路和我一样，但代码很漂亮的stack实现
    - https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252722/Python-stack-solution-beats-100-on-runtime-and-memory
```python
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root
```

    - 解法2： 递归，插入
        - https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252632/Python-or-simple-solution-%3A-40-ms-13.1-MB

- todo 自己手拍一遍递归解法，再仔细看看大家的递归解法
    - https://leetcode.com/contest/weekly-contest-127/ranking/