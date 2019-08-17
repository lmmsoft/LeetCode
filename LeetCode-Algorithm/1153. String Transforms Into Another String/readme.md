### [1153\. String Transforms Into Another String](https://leetcode.com/contest/biweekly-contest-6/problems/string-transforms-into-another-string/)

Difficulty: **Hard**

Given two strings `str1` and `str2` of the same length, determine whether you can transform `str1` into `str2` by doing **zero or more** _conversions_.

In one conversion you can convert **all** occurrences of one character in `str1` to **any** other lowercase English character.

Return `true` if and only if you can transform `str1` into `str2`.

**Example 1:**

```
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
```

**Example 2:**

```
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
```

**Note:**

1.  `1 <= str1.length == str2.length <= 10^4`
2.  Both `str1` and `str2` contain only lowercase English letters.

#### Solution
- https://leetcode.com/contest/biweekly-contest-6/ranking/
- 字符串变化
- 每次可以把所有某个字母变成另外一个，问能否变成
- 原来同样的字母，变后一定一样
- 如果原来26个小写字母都有了，目标也是26个小写字母，就无法变化了，因为没有零时字母供变化


Language: **Python3**

```python3
from collections import defaultdict
​
​
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        p1 = defaultdict(list)
        p2 = defaultdict(list)
        for idx, s in enumerate(str1):
            p1[s].append(idx)
        for idx, s in enumerate(str2):
            p2[s].append(idx)
        # check same s with same positio
        for p in p1.values():
            if len(p) > 1:
                s = {str2[idx] for idx in p}
                if len(s) > 1:
                    return False
        # check num
        if len(p1) < 26 or len(p2) < 26:
            return True
        else:
            return False
​
​
if __name__ == '__main__':
    assert Solution().canConvert(str1="aabcc", str2="ccdee")
    assert not Solution().canConvert(str1="leetcode", str2="codeleet")
    assert Solution().canConvert("ab", "ba")
    assert not Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")
    assert Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz")
​
    assert Solution().canConvert(
        "abcdefghijklmnopqrstuvwxyz",
        "bcdefghijklmnopqrstuvwxyzq")
​
```