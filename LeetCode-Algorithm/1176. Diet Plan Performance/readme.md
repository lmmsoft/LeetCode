### [5174\. Diet Plan PerformanceCopy for Markdown](https://leetcode.com/problems/diet-plan-performance/)
- https://leetcode.com/contest/weekly-contest-152/problems/diet-plan-performance/
- https://leetcode.com/problems/diet-plan-performance/

Difficulty: **Easy**


A dieter consumes `calories[i]` calories on the `i`-th day.  For every consecutive sequence of `k` days, they look at _T_, the total calories consumed during that sequence of `k` days:

*   If `T < lower`, they performed poorly on their diet and lose 1 point; 
*   If `T > upper`, they performed well on their diet and gain 1 point;
*   Otherwise, they performed normally and there is no change in points.

Return the total number of points the dieter has after all `calories.length` days.

Note that: The total points could be negative.

**Example 1:**

```
Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
Output: 0
Explaination: calories[0], calories[1] < lower and calories[3], calories[4] > upper, total points = 0.
```

**Example 2:**

```
Input: calories = [3,2], k = 2, lower = 0, upper = 1
Output: 1
Explaination: calories[0] + calories[1] > upper, total points = 1.
```

**Example 3:**

```
Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
Output: 0
Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] < lower, total points = 0.
```

**Constraints:**

*   `1 <= k <= calories.length <= 10^5`
*   `0 <= calories[i] <= 20000`
*   `0 <= lower <= upper`


#### Solution
- 求连续k个数的和，然后比较，用滑动窗口即可做到O(N)复杂度

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        point = 0
        s = sum(calories[0: k - 1])
        for i in range(k - 1, len(calories)):
            s += calories[i]
            if i - k >= 0:
                s -= calories[i - k]
​
            if s < lower:
                point -= 1
            elif s > upper:
                point += 1
​
        return point
​
​
if __name__ == '__main__':
    assert Solution().dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3) == 0
    assert Solution().dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1) == 1
    assert Solution().dietPlanPerformance(calories=[6, 5, 0, 0], k=2, lower=1, upper=5) == 0
​
```