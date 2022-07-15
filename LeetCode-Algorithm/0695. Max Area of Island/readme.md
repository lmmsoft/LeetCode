# [695\. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

## Description

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Depth-First Search](https://leetcode.com/tag/depth-first-search/), [Breadth-First Search](https://leetcode.com/tag/breadth-first-search/), [Union Find](https://leetcode.com/tag/union-find/), [Matrix](https://leetcode.com/tag/matrix/)


You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return _the maximum **area** of an island in_ `grid`. If there is no island, return `0`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 50`
*   `grid[i][j]` is either `0` or `1`.


## Solution

# 我自己的思路是 深搜 + 并查集，每个岛访问第一个点之后，就搜完全岛，并用第一个点的坐标标记，最后统计不同岛的个数就行
# 下面解法是看到discussion里面的巧妙解法，也是深搜，访问完一个点之后，把它标记成0，这样避免了重复搜索，同一个岛只搜一次，非常巧妙，代码实现也很简单！

Language: **Python3**

```python3
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ii=len(grid)
        jj=len(grid[0])
        
        def dfs(i,j):
            if i < 0 or j<0 or i>=ii or j>=jj or not grid[i][j]:
                return 0
            
            grid[i][j]=0
            
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
        
        areas = [dfs(i,j) for i in range(ii) for j in range(jj) if grid[i][j]]
        
        return max(areas) if areas else 0
```