### [74\. Search a 2D MatrixCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/search-a-2d-matrix/)

Difficulty: **Medium**


Write an efficient algorithm that searches for a value in an _m_ x _n_ matrix. This matrix has the following properties:

*   Integers in each row are sorted from left to right.
*   The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

**Example 2:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```


#### Solution
- 比较简单的二分变形题，把递增数组变成了矩阵，只要把二分的l,r转化成二维的i,j即可
- 这题可以联系用标准库bisect来试试，参考：
    - https://leetcode.com/problems/search-a-2d-matrix/discuss/26248/6-12-lines-O(log(m)-%2B-log(n))-myself%2Blibrary

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            mid = (l + r) // 2
            i, j = mid // col, mid % col
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
​
​
def test_solution():
    assert Solution().searchMatrix(matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target=3)
    assert not Solution().searchMatrix(matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target=13)
    assert not Solution().searchMatrix([], 0)
    assert not Solution().searchMatrix([[]], 1)
    assert not Solution().searchMatrix([[1, 1]], 2)
​
​
if __name__ == '__main__':
    test_solution()
​
```