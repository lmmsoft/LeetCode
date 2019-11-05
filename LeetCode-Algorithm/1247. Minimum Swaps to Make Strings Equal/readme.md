### [1247\. Minimum Swaps to Make Strings Equal](https://leetcode.com/contest/weekly-contest-161/problems/minimum-swaps-to-make-strings-equal/)
- https://leetcode.com/contest/weekly-contest-161/problems/minimum-swaps-to-make-strings-equal/
- https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

Difficulty: **Medium**

You are given two strings `s1` and `s2` of equal length consisting of letters `"x"` and `"y"` **only**. Your task is to make these two strings equal to each other. You can swap any two characters that belong to **different** strings, which means: swap `s1[i]` and `s2[j]`.

Return the minimum number of swaps required to make `s1` and `s2` equal, or return `-1` if it is impossible to do so.

**Example 1:**

```
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".```

**Example 2: **

```
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.```

**Example 3:**

```
Input: s1 = "xx", s2 = "xy"
Output: -1
```

**Example 4:**

```
Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4
```

**Constraints:**

*   `1 <= s1.length, s2.length <= 1000`
*   `s1, s2` only contain `'x'` or `'y'`.

#### Solution
- 比赛时是Easy赛后变成Medium
- 题意：两个字符串s1 s2, 每次可以交换任意两个字母，问多少次交换后s1 s2可以一样，不行返回-1
- 解法，看了前几名的代码，基本差不多
- for c1,c2 in zip(s1,s2), 然后c1和c2是xx yy忽略，分别统计xy yx的个数
- 如果xy和yx个数不同，返回-1
- 否则返回 (xy//2+yx//2) + (2 if xy%2==yx%2==1 else 0)
- xy和yx都是奇数的话，最后需要多1次交换

Language: **Python3**

```python3
from collections import Counter
​
​
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        c = Counter(s1 + s2)
        # if c['x'] != c['y']:
        #     return -1
        a, b = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    a += 1
                else:
                    b += 1
        r = a // 2 + b // 2
        if a % 2 and b % 2:
            r += 2
        if a%2 != b%2:
            return -1
​
        return r
```