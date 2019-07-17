### [1123\. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)
- https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
- https://leetcode.com/contest/weekly-contest-145/problems/lowest-common-ancestor-of-deepest-leaves/
- https://leetcode.com/contest/weekly-contest-145/ranking

Difficulty: **Medium**


Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

*   The node of a binary tree is a _leaf_ if and only if it has no children
*   The _depth_ of the root of the tree is 0, and if the depth of a node is `d`, the depth of each of its children is `d+1`.
*   The _lowest common ancestor_ of a set `S` of nodes is the node `A` with the largest depth such that every node in S is in the subtree with root `A`.

**Example 1:**

```
Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
```

**Example 2:**

```
Input: root = [1,2,3,4]
Output: [4]
```

**Example 3:**

```
Input: root = [1,2,3,4,5]
Output: [2,4,5]
```

**Constraints:**

*   The given tree will have between 1 and 1000 nodes.
*   Each node of the tree will have a distinct value between 1 and 1000.


#### Solution
- 最深叶节点的最近公共祖先, 题目读了很久，其实仔细看测试用例应该能猜出来的， 想得不够深入，所以代码稍微冗余了一点，还好 1AC
- 题意：对于所有叶节点，找到公共祖先里面深度最大的那个节点，返回节点的TreeNode对象
- 我的思路：
    - 深搜，记下每个节点的深度和父节点
    - 对于每个叶子节点，他们深度肯定是一样的（题意），反复找他们各自的父节点，直到父节点是同一个点，返回之~
    - rank24 (CyberZHG) 和我是完全一样的思路
    - rank11 (superluminal) 类似的思路，使用 BFS 实现
- 更简洁的思路(代码没能实现，已放弃)
    - 既然叶节点深度都一样，那么求每个节点左右子树的深度
        - 如果不一样，要的点肯定在深度高的那边
        - 如果一样，那么这个点一定是祖先节点，第一个遇到的就是最近公共祖先
        
Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
​
class Solution:
    # DFS, 60ms, 13.6mb内存
    def lcaDeepestLeaves1(self, root: TreeNode) -> TreeNode:
        self.parent: Dict[TreeNode, TreeNode] = {}
        self.deep_list: Dict[int, List[TreeNode]] = {}

        def dfs(n: TreeNode, deep: int):
            if deep in self.deep_list:
                self.deep_list[deep].append(n)
            else:
                self.deep_list[deep] = [n]

            if n.left:
                self.parent[n.left] = n
                dfs(n.left, deep + 1)
            if n.right:
                self.parent[n.right] = n
                dfs(n.right, deep + 1)

        dfs(root, 0)
        max_deep: int = max(self.deep_list.keys())

        leaves: list = self.deep_list[max_deep]
        while True:
            s = set()
            for l in leaves:
                s.add(l)
            if len(s) == 1:
                return list(s)[0]
            else:
                leaves = [self.parent[leaf] for leaf in leaves]

        return None
    
    # BFS 52ms, 13.3mb内存
    # rank 11 superluminal
    # 类似的思路，使用 BFS 实现
    def lcaDeepestLeaves2(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parent = {}
        queue = set([root])
        while True:
            next_queue = set()
            for node in queue:
                for child in (node.left, node.right):
                    if child:
                        parent[child] = node
                        next_queue.add(child)
            if not next_queue:
                break
            queue = next_queue
        # 此时的queue就是所有的叶子节点，因为他们的next_queue是空的
        while len(queue) > 1:
            queue = set(parent[n] for n in queue)
        for node in queue:
            return node
​
```