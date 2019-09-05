### [28\. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

Difficulty: **Easy**


Implement .

Return the index of the first occurrence of needle in haystack, or **-1** if needle is not part of haystack.

**Example 1:**

```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2:**

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's  and Java's .


#### Solution
- 用标准库 index()时间比较慢 80%, 改用find() 直接就20%了，标准库内部的算法不太一样
- 当然最好是自己写KMP
    - TBD

Language: **Python3**

```python3
class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
​
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
​
​
if __name__ == '__main__':
    assert Solution().strStr(haystack="hello", needle="ll") == 2
    assert Solution().strStr(haystack="aaaaa", needle="bba") == -1
​
```