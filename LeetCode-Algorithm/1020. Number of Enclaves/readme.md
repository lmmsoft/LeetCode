### [1020\. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)
- https://leetcode.com/problems/number-of-enclaves/
- https://leetcode.com/contest/weekly-contest-130/problems/number-of-enclaves/

Difficulty: **Medium**


Given a 2D array `A`, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we **cannot** walk off the boundary of the grid in any number of moves.

**Example 1:**

```
Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
```

**Example 2:**

```
Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
```

**Note:**

1.  `1 <= A.length <= 500`
2.  `1 <= A[i].length <= 500`
3.  `0 <= A[i][j] <= 1`
4.  All rows have the same size.


#### Solution
- 一开始想用并查集，找到中间相连在一起的块数，后来发现不需要求快数，只要求不在岸边的个数就行
- 于是就比较简单了，分为两步
    1. 把连在岸边的去掉（从最外面一圈开始搜索，DFS比较容易实现，BFS也可以）
    2. 统计中间个数（直接求和就行）

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        Li, Lj = len(A), len(A[0])
​
        def dfs(i, j):
            A[i][j] = 0
            for ii, jj in [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]:
                if 0 <= ii < Li and 0 <= jj < Lj and A[ii][jj] == 1:
                    dfs(ii, jj)
​
        for j in range(0, Lj):
            if A[0][j]:
                dfs(0, j)
            if A[Li - 1][j]:
                dfs(Li - 1, j)
​
        for i in range(0, Li):
            if A[i][0]:
                dfs(i, 0)
            if A[i][Lj - 1]:
                dfs(i, Lj - 1)
​
        res = sum(sum(row) for row in A)
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3
    assert Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == 0
​
```