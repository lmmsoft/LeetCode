### [67\. Add Binary](https://leetcode.com/problems/add-binary/)

Difficulty: **Easy**


Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"
```


#### Solution
- 自己裸写32ms, 用标准库56ms, 内存一样
- 标准库用法：
    - int("10")==10
    - int("10",2)==2
    - int("10",3)==3
    - int("10",16)==16
- 标准库用法：
    - format(2,'b)=='10'
    - format(8,'o')=='10'
    - format(10,'d')=='10'
    - format(15,'x')=='f'
    - format(16,'x')=='10'
    - format(900,'e')=='9.000000e+02'
    - format(900.1234,'f')=='900.123400'
    - For more details: help('FORMATTING')
    - ord('A')==65
    - ord('a')==97
    - ord('@')==64
    - format(97,'c')=='a
    - format(65,'c')=='A'
    - format(64,'@')=='@

Language: **Python3**

```python3
class Solution:
    def addBinary2(self, a: str, b: str) -> str:
        def str2int(s):
            sum = 0
            base = 1
            for c in s[::-1]:
                sum += int(c) * base
                base = base << 1
            return sum
​
        aa = str2int(a)
        bb = str2int(b)
        cc = aa + bb
        res = str(bin(cc))[2:]
        print(res)
        return res
​
    def addBinary(self, a: str, b: str) -> str:
        return str(
            bin(
                int(a, 2) + int(b, 2)
            )
        )[2:]
​
​
if __name__ == '__main__':
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary(a="1010", b="1011") == "10101"
​
```