### [1119\. Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string/)
- https://leetcode.com/problems/remove-vowels-from-a-string/
- https://leetcode.com/contest/biweekly-contest-4/problems/remove-vowels-from-a-string/

Difficulty: **Easy**


Given a string `S`, remove the vowels `'a'`, `'e'`, `'i'`, `'o'`, and `'u'` from it, and return the new string.

**Example 1:**

```
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
```

**Example 2:**

```
Input: "aeiou"
Output: ""
```

**Note:**

1.  `S` consists of lowercase English letters only.
2.  `1 <= S.length <= 1000`


#### Solution
- string replace题，直接调用库函数 1AC
Language: **Python3**

```python3
class Solution:
    def removeVowels(self, S: str) -> str:
        for c in "aeiou":
            S = S.replace(c, '')
        return S
```