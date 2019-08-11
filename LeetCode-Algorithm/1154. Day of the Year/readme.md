### [1154\. Day of the Year](https://leetcode.com/problems/day-of-the-year/)
- https://leetcode.com/problems/day-of-the-year/
- https://leetcode.com/contest/weekly-contest-149/problems/day-of-the-year/

Difficulty: **Easy**


Given a string `date` representing a date formatted as `YYYY-MM-DD`, return the day number of the year.

**Example 1:**

```
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
```

**Example 2:**

```
Input: date = "2019-02-10"
Output: 41
```

**Example 3:**

```
Input: date = "2003-03-01"
Output: 60
```

**Example 4:**

```
Input: date = "2004-03-01"
Output: 61
```

**Constraints:**

*   `date.length == 10`
*   `date[4] == date[7] == '-'`, and all other `date[i]`'s are digits
*   `date` represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.


#### Solution
- 比赛时候用strptime转成datetime，然后用当年第一题相减得到天数
- 赛后看了讨论去，用标准库的精妙方法还不少
    - 比如用datetime.timetuple().tm_yday
    - datetime.strftime("%j")
    
Language: **Python3**

```python3
from datetime import datetime
​
​
class Solution:
    def dayOfYear(self, date: str) -> int:
        d = datetime.strptime(date, "%Y-%m-%d")
        d0 = datetime(d.year, 1, 1)
        return (d-d0).days+1
​
​
if __name__ == '__main__':
    assert Solution().dayOfYear("2019-01-09") == 9
    assert Solution().dayOfYear("2019-02-10") == 41
    assert Solution().dayOfYear("2019-03-01") == 60
    assert Solution().dayOfYear("2004-03-01") == 61
​
```