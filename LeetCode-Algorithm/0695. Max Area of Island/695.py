from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ii = len(grid)
        jj = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ii or j >= jj or not grid[i][j]:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        areas = [dfs(i, j) for i in range(ii) for j in range(jj) if grid[i][j]]

        return max(areas) if areas else 0