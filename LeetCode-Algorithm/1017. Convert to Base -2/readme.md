### [1017\. Convert to Base -2](https://leetcode.com/problems/convert-to-base-2/)

Difficulty: **Medium**


Given a number `N`, return a string consisting of `"0"`s and `"1"`s that represents its value in base `**-2**` (negative two).

The returned string must have no leading zeroes, unless the string is `"0"`.


**Example 1:**

```
Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
```


**Example 2:**

```
Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
```


**Example 3:**

```
Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
```

**<span style="display: inline;">Note:</span>**

1.  <span style="display: inline;">`0 <= N <= 10^9`</span>


#### Solution
- 模拟题，按照进制转换的除法依次计算即可
- 也有变态发方法，用异或直接 O(1)搞定，详见lee的解法

Language: **Python3**

```python3
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        n = N
        z = []
        plusOrMinus: int = -1
        while n != 0:
            if n % 2:
                z.append('1')
                n += plusOrMinus
            else:
                z.append('0')
​
            plusOrMinus *= -1
            n = n // 2
​
        ans = ''.join(z[::-1])
        ans2 = str(int(ans))
        print(ans2)
        return ans2
​
​
```