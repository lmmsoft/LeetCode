### [1145\. Binary Tree Coloring Game](https://leetcode.com/problems/binary-tree-coloring-game/)
- https://leetcode.com/problems/binary-tree-coloring-game/
- https://leetcode.com/contest/weekly-contest-148/problems/binary-tree-coloring-game/

Difficulty: **Medium**


Two players play a turn based game on a binary tree.  We are given the `root` of this binary tree, and the number of nodes `n` in the tree.  `n` is odd, and each node has a distinct value from `1` to `n`.

Initially, the first player names a value `x` with `1 <= x <= n`, and the second player names a value `y` with `1 <= y <= n` and `y != x`.  The first player colors the node with value `x` red, and the second player colors the node with value `y` blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an **uncolored** neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a `y` to ensure you win the game, return `true`.  If it is not possible, return `false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png)

```
Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
```

**Constraints:**

*   `root` is the root of a binary tree with `n` nodes and distinct node values from `1` to `n`.
*   `n` is odd.
*   `1 <= x <= n <= 100`


#### Solution
- 后手的想要取得最多的节点数，只可能去左右子节点或者父亲节点，三种情况，一一枚举即可
- 左右字数的个数就是自身的个数，去父亲节点的个数是总数减去当前节点
- 基本上大家的思路都是dfs把每个节点的子节点个数先求出，顺便找到x对应的节点，然后统计三种情况的最小值
- 我的思路是对的，最后比较的代码比较冗余

Language: **Python3**

```python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        d: dict = {}
        x_node: TreeNode = None

        def dfs(n: TreeNode):
            nonlocal x_node

            if not n:
                return 0
            else:
                if n.val == x:
                    x_node = n

                num = dfs(n.left) + dfs(n.right) + 1
                d[n.val] = num
                return num

        dfs(root)

        # check_left
        if x_node.left:
            num1 = d[x_node.left.val]
            num2 = n - num1
            if num1 > num2:
                return True
        # check right
        if x_node.right:
            num1 = d[x_node.right.val]
            num2 = n - num1
            if num1 > num2:
                return True
        # check parent
        num2 = d[x_node.val]
        num1 = n - num2
        if num1 > num2:
            return True

        return False


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t10 = TreeNode(10)
    t11 = TreeNode(11)

    t1.left, t1.right = t2, t3
    t2.left, t2.right = t4, t5
    t3.left, t3.right = t6, t7
    t4.left, t4.right = t8, t8
    t5.left, t5.right = t10, t11

    assert Solution().btreeGameWinningMove(t1, 11, 3)
​
```