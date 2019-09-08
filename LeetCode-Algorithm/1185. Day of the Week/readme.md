### [5183\. Day of the Week](https://leetcode.com/contest/weekly-contest-153/problems/day-of-the-week/)

Difficulty: **Easy**

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the `day`, `month` and `year` respectively.

Return the answer as one of the following values `{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}`.

**Example 1:**

```
Input: day = 31, month = 8, year = 2019
Output: "Saturday"
```

**Example 2:**

```
Input: day = 18, month = 7, year = 1999
Output: "Sunday"
```

**Example 3:**

```
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
```

**Constraints:**

*   The given dates are valid dates between the years `1971` and `2100`.

#### Solution
- 水题，直接用标准库搞
- Lee 有公式，可以直接搞
    - Zeller Formula https://leetcode.com/problems/day-of-the-week/discuss/377384/JavaC%2B%2BPython-Zeller-Formula
    - Sakamoto’s Algorithm https://leetcode.com/problems/day-of-the-week/discuss/377400/Java-Sakamoto's-Algorithm
    - 两个算法看上去很像，但是Lee不需要记录一个常量数组

Language: **Python3**

```python3
from datetime import datetime
​
​
class Solution:
    def dayOfTheWeek1(self, day: int, month: int, year: int) -> str:
        d = datetime(year, month, day)
        a = d.weekday()
​
        r = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", ]
        return r[a]
​
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][
            datetime(year, month, day).weekday()]
​
​
if __name__ == '__main__':
    assert Solution().dayOfTheWeek(day=31, month=8, year=2019) == "Saturday"
    assert Solution().dayOfTheWeek(day=18, month=7, year=1999) == "Sunday"
    assert Solution().dayOfTheWeek(day=15, month=8, year=1993) == "Sunday"
​
```