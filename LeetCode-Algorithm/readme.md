### [58\. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

Difficulty: **Easy**


Given a string _s_ consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.

If the last word does not exist, return 0.

**Note:** A word is defined as a character sequence consists of non-space characters only.

**Example:**

```
Input: "Hello World"
Output: 5
```


#### Solution
- 水题，注意去掉尾部的" " 再split() 否则最后是""

Language: **Python3**

```python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
​
​
if __name__ == '__main__':
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("a ") == 1
    assert Solution().lengthOfLastWord("a") == 1
​
```