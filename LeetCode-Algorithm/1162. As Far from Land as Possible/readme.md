### [1162\. As Far from Land as Possible](https://leetcode.com/contest/weekly-contest-150/problems/as-far-from-land-as-possible/)
- https://leetcode.com/problems/as-far-from-land-as-possible/
- https://leetcode.com/contest/weekly-contest-150/problems/as-far-from-land-as-possible/


Difficulty: **Medium**

Given an N x N `grid` containing only values `0` and `1`, where `0` represents water and `1` represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the _Manhattan distance_: the distance between two cells `(x0, y0)` and `(x1, y1)` is `|x0 - x1| + |y0 - y1|`.

If no land or water exists in the grid, return `-1`.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG)**

```
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
```

**Example 2:**

**![](https://assets.leetcode.com/uploads/2019/05/03/1336_ex2.JPG)**

```
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
```

<span style="display: inline;">**Note:**</span>

1.  <span style="display: inline;">`1 <= grid.length == grid[0].length <= 100`</span>
2.  <span style="display: inline;">`grid[i][j]` is `0` or `1`</span>

#### Solution
- 思路：BFS
- 首先找到所有land，距离为0
- 然后找到距离为0上下左右的water，标记为land，距离为1
- 以此类推，接着再操作距离为2的water
- 走好找到所有的点，返回距离最大数

- 看了别人的代码，基本差不多，处理上下左右的实现比我的好一点，不需要子函数
```python
for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
    xi, yj = x+i, y+j
    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
```


Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        L = len(grid)
​
        s = sum(sum(r) for r in grid)
        if s == 0 or s == L * L:
            return -1
​
        def add(i, j, cnt, next):
            if 0 <= i < L and 0 <= j < L and grid[i][j] == 0:
                grid[i][j] = 1
                cnt += 1
                next.append((i, j))
            return cnt
​
        q = []
        cnt = 0
        for i in range(L):
            for j in range(L):
                if grid[i][j] == 1:
                    q.append((i, j))
                    cnt += 1
        mx = 0
        while cnt < L * L:
            mx += 1
            next = []
            while q:
                i, j = q.pop()
                cnt = add(i + 1, j, cnt, next)
                cnt = add(i - 1, j, cnt, next)
                cnt = add(i, j + 1, cnt, next)
                cnt = add(i, j - 1, cnt, next)
            q = next
        return mx
​
​
if __name__ == '__main__':
    assert Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
​
```