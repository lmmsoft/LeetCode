### [1198\. Find Smallest Common Element in All Rows](https://leetcode.com/contest/biweekly-contest-9/problems/find-smallest-common-element-in-all-rows/)

Difficulty: **Medium**

Given a matrix `mat` where every row is sorted in **increasing** order, return the **smallest common element** in all rows.

If there is no common element, return `-1`.

**Example 1:**

```
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
```

**Constraints:**

*   `1 <= mat.length, mat[i].length <= 500`
*   `1 <= mat[i][j] <= 10^4`
*   `mat[i]` is sorted in increasing order.

#### Solution

Language: **Python3**
- 水题，直接set()暴力即可

```python3
from typing import List
​
​
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        s = set(mat[1])
        for i in range(1, len(mat)):
            s2 = set(mat[i])
            s = s & s2
​
        return min(s) if s else -1
```