### [1163\. Last Substring in Lexicographical OrderCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/last-substring-in-lexicographical-order/)

Difficulty: **Hard**


Given a string `s`, return the last substring of `s` in lexicographical order.

**Example 1:**

```
Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
```

**Example 2:**

```
Input: "leetcode"
Output: "tcode"
```

**Note:**

1.  `1 <= s.length <= 10^5`
2.  <font face="monospace" style="display: inline;">s</font> contains only lowercase English letters.


#### Solution
- 暴力 O(N^2)
- 先找到最大的字母，然后求最大字母到终点组成的子串的最大值
- 优化的话或许可以用后缀数组，最小表示法，我暂时还不会

Language: **Python3**

```python3
from collections import defaultdict
​
​
class Solution:
    def lastSubstring2(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        z = max(d.keys())
        ids = d[z]
        return max(s[start:] for start in ids)
​
    def lastSubstring(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s): d[c].append(i)
        return max(s[start:] for start in (d[max(d.keys())]))
​
​
if __name__ == '__main__':
    assert Solution().lastSubstring("abab") == 'bab'
    assert Solution().lastSubstring("leetcode") == 'tcode'
​
```