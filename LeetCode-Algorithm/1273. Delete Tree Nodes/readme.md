### [1273\. Delete Tree Nodes](https://leetcode.com/problems/delete-tree-nodes/)
- https://leetcode.com/contest/biweekly-contest-14/problems/delete-tree-nodes/

Difficulty: **Medium**


A tree rooted at node 0 is given as follows:

*   The number of nodes is `nodes`;
*   The value of the `i`-th node is `value[i]`;
*   The parent of the `i`-th node is `parent[i]`.

Remove every subtree whose sum of values of nodes is zero.

After doing so, return the number of nodes remaining in the tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/07/02/1421_sample_1.PNG)

```
Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2
```

**Constraints:**

*   `1 <= nodes <= 10^4`
*   `-10^5 <= value[i] <= 10^5`
*   `parent.length == nodes`
*   `parent[0] == -1` which indicates that `0` is the root.


#### Solution
- 题意：给定一棵树，序号0到nodes-1；给出每个节点的parent变化和它自己的值，把每个和为0的子树都去掉，问最后还剩几个节点
- 解法：递归题
    1. 构建数结构
    2. 递归求出子树和(包含自己在内的数的和)
    3. 移除0和子树，更新树结构
    4. 求此时节点个数
- 这题有点悬，比赛结束前写出来

Language: **Python3**

```python3
from collections import defaultdict
​
from typing import List
​
​
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        sub = defaultdict(dict)
        subtree_sum = {}
        for id, p in enumerate(parent):
            v = value[id]
            if p == -1:
                pass
            else:
                sub[p][id] = v
​
        def get_subtree_sum(id):
            s = 0
            for sub_id, sub_v in sub[id].items():
                s += get_subtree_sum(sub_id)
            subtree_sum[id] = s + value[id]
            return s + value[id]
​
        get_subtree_sum(0)
        print(subtree_sum)
​
        for k, v in subtree_sum.items():
            if v == 0:
                p = parent[k]
                sub[p].pop(k)
        print(sub)
​
        def find(id):
            n = 1
            for k in sub[id].keys():
                n += find(k)
            return n
​
        x = find(0)
        return x
```