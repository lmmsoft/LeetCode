### [541\. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

Difficulty: **Easy**

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

**Example:**  

```
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
```

**Restrictions:**

1.  The string consists of lower English letters only.
2.  Length of the given string and k will in the range [1, 10000]


#### Solution
- 水题，理解题意，使用合适的库函数，非常重要，这题写得好的和不好的能差几十行

Language: **Python3**

```python3
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        for i in range(0, len(s), 2 * k):
            l[i:i + k] = list(reversed(l[i:i + k]))
        return ''.join(l)
```