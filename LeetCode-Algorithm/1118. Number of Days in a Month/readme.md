### [1118\. Number of Days in a Month](https://leetcode.com/problems/number-of-days-in-a-month/)
- https://leetcode.com/problems/number-of-days-in-a-month/
- https://leetcode.com/contest/biweekly-contest-4/problems/number-of-days-in-a-month/

Difficulty: **Easy**


Given a year `Y` and a month `M`, return how many days there are in that month.

**Example 1:**

```
Input: Y = 1992, M = 7
Output: 31
```

**Example 2:**

```
Input: Y = 2000, M = 2
Output: 29
```

**Example 3:**

```
Input: Y = 1900, M = 2
Output: 28
```

**Note:**

1.  `1583 <= Y <= 2100`
2.  `1 <= M <= 12`


#### Solution
- 闰月判断，太熟悉了，直接打表，居然忘了闰年处理余4的情况，1WA1AC

- Language: **Python3**

```python3
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        d1: list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d2: list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (Y % 400 == 0) or (Y % 4 == 0 and Y % 100 != 0):
            return d2[M]
        return d1[M]
```