### [1167\. Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)
- https://leetcode.com/problems/minimum-cost-to-connect-sticks/
- https://leetcode.com/contest/biweekly-contest-7/problems/minimum-cost-to-connect-sticks/

Difficulty: **Medium**


You have some `sticks` with positive integer lengths.

You can connect any two sticks of lengths `X` and `Y` into one stick by paying a cost of `X + Y`.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given `sticks` into one stick in this way.

**Example 1:**

```
Input: sticks = [2,4,3]
Output: 14
```

**Example 2:**

```
Input: sticks = [1,8,3,5]
Output: 30
```

**Constraints:**
```
1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
```

#### Solution
- 贪心，简单的堆操作
- 每次取出数值最小的两个，再放入，用堆来保证每次操作logN复杂度

Language: **Python3**

```python3
import heapq
from typing import List
​
​
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        h = sticks
        s = 0
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            heapq.heappush(h, a + b)
            s += a + b
        return s
​
​
if __name__ == '__main__':
    assert Solution().connectSticks([2, 4, 3]) == 14
    assert Solution().connectSticks([1, 8, 3, 5]) == 30
​
```