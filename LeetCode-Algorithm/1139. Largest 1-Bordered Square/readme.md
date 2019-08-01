### [1139\. Largest 1-Bordered Square](https://leetcode.com/problems/largest-1-bordered-square/)
https://leetcode.com/problems/largest-1-bordered-square/  
- https://leetcode.com/contest/weekly-contest-147/problems/largest-1-bordered-square/
- https://leetcode.com/contest/weekly-contest-147/submissions/detail/246868715/


Difficulty: **Medium**


Given a 2D `grid` of `0`s and `1`s, return the number of elements in the largest **square** subgrid that has all `1`s on its **border**, or `0` if such a subgrid doesn't exist in the `grid`.

**Example 1:**

```
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
```

**Example 2:**

```
Input: grid = [[1,1,0,0]]
Output: 1
```

**Constraints:**

*   `1 <= grid.length <= 100`
*   `1 <= grid[0].length <= 100`
*   `grid[i][j]` is `0` or `1`


#### Solution
- 01矩阵里，找最大的边框都是1的矩形
- 我用的O(N^4)暴力，枚举起终点，边长，检测每个点
- 其实可以优化到O(N^3)，就是检测每个点，可以前求出没行列的和，那么L(a to b) = S(0 to b) - S(0 to a)
- 低级失误，WA了一次，返回 size*size,我只返回了size

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
​
        # check all zero
        ss = 0
        for i in grid:
            ss += sum(i)
        if ss == 0:
            return 0
        if ss < 4:
            return 1
​
        len_i = len(grid)
        len_j = len(grid[0])
        size = min(len_i, len_j)
        for s in range(size, 1, -1):  # size to 2
            # from 0 to len_i - s
            for i in range(0, len_i - s + 1):
                for j in range(0, len_j - s + 1):
                    # check
                    failed = False
                    ii, jj = i + s - 1, j + s - 1
                    for ss in range(s):
                        if grid[i + ss][j] == 0:
                            failed = True
                            break
                        if grid[i][j + ss] == 0:
                            failed = True
                            break
​
                        if grid[i + ss][jj] == 0:
                            failed = True
                            break
                        if grid[ii][j + ss] == 0:
                            failed = True
                            break
                    if not failed:
                        print(s * s)
​
                        return s * s
        return 1
​
​
if __name__ == '__main__':
    assert Solution().largest1BorderedSquare([[1, 1, 1], [1, 1, 0], [1, 1, 1], [0, 1, 1], [1, 1, 1]]) == 4
    assert Solution().largest1BorderedSquare([[0, 0], [0, 0]]) == 0
    assert Solution().largest1BorderedSquare([[1, 1, 0, 0]]) == 1
    assert Solution().largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 9
​
```