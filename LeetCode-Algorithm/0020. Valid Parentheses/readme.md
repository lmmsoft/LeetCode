### [20\. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Difficulty: **Easy**


Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```


#### Solution
- 水题，用stack，另外可以重构一下，把代码写漂亮一点

Language: **Python3**

```python3
class Solution:
    def isValid(self, s: str) -> bool:
        d1 = {
            '(': 1,
            '{': 2,
            '[': 3,
        }
        d2 = {
            ')': 1,
            '}': 2,
            ']': 3,
        }
​
        stack = []
        for c in s:
            if len(stack):
                if c in list(d2.keys()):
                    if d2[c] == d1.get(stack[-1], 0):
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
​
            else:
                stack.append(c)
​
        return not len(stack)
​
​
if __name__ == '__main__':
    assert Solution().isValid("()")
    assert Solution().isValid("()[]{}")
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("{[]}")
​
```