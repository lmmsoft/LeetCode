### [9\. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Difficulty: **Easy**


Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**

```
Input: 121
Output: true
```

**Example 2:**

```
Input: -121
Output: false
Explanation: From left to right, it reads -121\. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Follow up:**

Coud you solve it without converting the integer to a string?


#### Solution
- 编辑器里一次AC, 耶！

Language: **Python3**

```python3
class Solution:
    def isPalindrome1(self, x: int) -> bool:
        return str(x) == ''.join(reversed(str(x)))

    def isPalindrome(self, x: int) -> bool:
        return str(x) == (str(x))[::-1]

```