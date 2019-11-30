### [1271\. Hexspeak](https://leetcode.com/problems/hexspeak/)
- https://leetcode.com/contest/biweekly-contest-14/problems/hexspeak/

Difficulty: **Easy**


A decimal number can be converted to its _Hexspeak representation_ by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit `0` with the letter `O`, and the digit `1` with the letter `I`.  Such a representation is _valid_ if and only if it consists only of the letters in the set `{"A", "B", "C", "D", "E", "F", "I", "O"}`.

Given a string `num` representing a decimal integer `N`, return the Hexspeak representation of `N` if it is valid, otherwise return `"ERROR"`.

**Example 1:**

```
Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.
```

**Example 2:**

```
Input: num = "3"
Output: "ERROR"
```

**Constraints:**

*   `1 <= N <= 10^12`
*   There are no leading zeros in the given string.
*   All answers must be in uppercase letters.


#### Solution
- 题意：把十进制转换成十六进制，0变O,1变I, a到f变A到F，其他有2到9返回ERROR
- 水题，模拟即可

Language: **Python3**
```python3
class Solution:
    def toHexspeak(self, num: str) -> str:
        i = int(num)
        h = hex(i)
        h2 = str(h)[2:]
        l = []
        for ch in h2:
            if ch == "0":
                l.append('O')
            elif ch == "1":
                l.append("I")
            elif ch == 'a':
                l.append("A")
            elif ch == 'b':
                l.append("B")
            elif ch == 'c':
                l.append("C")
            elif ch == 'd':
                l.append("D")
            elif ch == 'e':
                l.append("E")
            elif ch == 'f':
                l.append("F")
            else:
                return "ERROR"
        return ''.join(l)
```