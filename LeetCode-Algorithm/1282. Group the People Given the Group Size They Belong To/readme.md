### [1282\. Group the People Given the Group Size They Belong To](https://leetcode.com/contest/weekly-contest-166/problems/group-the-people-given-the-group-size-they-belong-to/)

Difficulty: **Medium**

There are `n` people whose **IDs** go from `0` to `n - 1` and each person belongs **exactly** to one group. Given the array `groupSizes` of length `n` telling the group size each person belongs to, return the groups there are and the people's **IDs** each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

**Example 1:**

```
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
```

**Example 2:**

```
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
```

**Constraints:**

*   `groupSizes.length == n`
*   `1 <= n <= 500`
*   `1 <= groupSizes[i] <= n`

#### Solution
- 水题，暴力即可
- 数字按照每组个数分组，水题

Language: **Python3**

```python3
from collections import defaultdict
from typing import List
​
​
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for id, g in enumerate(groupSizes):
            d[g].append(id)
        res = []
        for size, l in d.items():
            while l:
                small = []
                cnt = size
                while cnt:
                    small.append(l.pop())
                    cnt -= 1
                res.append(small)
        #print(res)
        return res
```