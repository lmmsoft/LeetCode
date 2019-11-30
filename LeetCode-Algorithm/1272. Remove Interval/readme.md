### [1272\. Remove Interval](https://leetcode.com/problems/remove-interval/)
- https://leetcode.com/contest/biweekly-contest-14/problems/remove-interval/

Difficulty: **Medium**


Given a **sorted** list of disjoint `intervals`, each interval `intervals[i] = [a, b]` represents the set of real numbers `x` such that `a <= x < b`.

We remove the intersections between any interval in `intervals` and the interval `toBeRemoved`.

Return a **sorted** list of `intervals` after all such removals.

**Example 1:**

```
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
```

**Example 2:**

```
Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
```

**Constraints:**

*   `1 <= intervals.length <= 10^4`
*   `-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9`


#### Solution
- 题意：去除区间，给一堆有序的区间，和一个要去除的区间，把去除的部分去掉，返回剩下的有序区间
- 枚举区间相交的6种情况 比较 每个区间的a,b 和要去除的d_a,d_b，六种情况，有完全去掉;有保留左半；有保留右半；有保留左右，去除中间，有完全保留
- 最后去掉a==b的区间，重新排序即可

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        del_a, del_b = toBeRemoved
        for a, b in intervals:
            if del_b <= a or b < del_a:
                res.append([a, b])
            elif del_a <= a < del_b < b:
                res.append([del_b, b])
            elif del_a <= a and b < del_b:
                pass
            elif a <= del_a < b and a < del_b < b:
                res.append([a, del_a])
                res.append([del_b, b])
            elif a <= del_a < b < del_b:
                res.append([a, del_a])
        # r2 = []
        # for a, b in res:
        #     if a < b:
        #         r2.append([a, b])
        # r2 = sorted(r2)
        return res
​
```