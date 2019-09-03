### [14\. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Difficulty: **Easy**


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Note:**

All given inputs are in lowercase letters `a-z`.


#### Solution
- 没考虑边界情况，WA了两次
- 我的写法比较啰嗦，不漂亮
- 看到了一个漂亮的答案，用strs.pop()取出第一个，然后找到长度，从后往前比较

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        mn = min(len(s) for s in strs)
        for i in range(mn):
            pre = None
            for s in strs:
                if not pre:
                    pre = s[i]
                elif pre == s[i]:
                    pass
                else:
                    return res
            res += pre
        return res
​
​
if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(['aa', 'a']) == 'a'
​
```