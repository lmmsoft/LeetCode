### [1168\. Optimize Water Distribution in a Village](https://leetcode.com/contest/biweekly-contest-7/problems/optimize-water-distribution-in-a-village/)
- https://leetcode.com/contest/biweekly-contest-7/problems/optimize-water-distribution-in-a-village/
- https://leetcode.com/problems/optimize-water-distribution-in-a-village/discuss

Difficulty: **Hard**

There are `<font face="monospace" style="display: inline;">n</font>` houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house `i`, we can either build a well inside it directly with cost `wells[i]`, or pipe in water from another well to it. The costs to lay pipes between houses are given by the array `pipes`, where each `pipes[i] = [house1, house2, cost]` represents the cost to connect `house1` and `house2` together using a pipe. Connections are bidirectional.

Find the minimum total cost to supply water to all houses.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/05/22/1359_ex1.png)**

```
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: 
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
```

**Constraints:**

*   `1 <= n <= 10000`
*   `wells.length == n`
*   `0 <= wells[i] <= 10^5`
*   `1 <= pipes.length <= 10000`
*   `1 <= pipes[i][0], pipes[i][1] <= n`
*   `0 <= pipes[i][2] <= 10^5`
*   `pipes[i][0] != pipes[i][1]`

#### Solution
- 转化成最小生成树
- 比赛时没想到添加新节点的办法，只想到把井盖变成连接其他节点的路径长度，然后用贪心乱搞，可惜TLE了
- 赛后用户添加0节点的方法，到0节点的距离是井盖的价值，然后最短路
s
Language: **Python3**

```python3
from typing import List, Tuple
​
​
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parents = [x for x in range(0, n + 1)]
        members = [1] * (n + 1)
​
        def find(x: int) -> int:
            while parents[x] != x:
                x = parents[x]
            return x
​
        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if members[px] < members[py]:
                px, py = py, px
            members[px] += members[py]
            parents[py] = px
            return True
​
        edge: List[Tuple[int, int, int]] = []
        for a, b, cost in pipes:
            edge.append((cost, a, b))
​
        for i, cost in enumerate(wells):
            edge.append((cost, 0, i + 1))
​
        # Kruskal
        edge = sorted(edge)
        s = 0
        cnt = 0
        for cost, a, b in edge:
            if find(a) != find(b):
                s += cost
                union(a, b)
                cnt += 1
                if cnt == n:
                    break
​
        print(s)
        return s
​
​
if __name__ == '__main__':
    assert Solution().minCostToSupplyWater(n=2, wells=[10, 20], pipes=[[1, 2, 30]]) == 30
    assert Solution().minCostToSupplyWater(n=3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]]) == 3
    assert Solution().minCostToSupplyWater(
        n=6,
        wells=[4625, 65696, 86292, 68291, 37147, 7880],
        pipes=[[2, 1, 79394], [3, 1, 45649], [4, 1, 75810], [5, 3, 22340], [6, 1, 6222]]
    ) == 204321
​
```