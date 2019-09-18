### [69\. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

Difficulty: **Easy**


Implement `int sqrt(int x)`.

Compute and return the square root of _x_, where _x_ is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

**Example 1:**

```
Input: 4
Output: 2
```

**Example 2:**

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
```


#### Solution
- hint1 顺序遍历sqrt_num
- hint2 二分

Language: **Python3**

```python3
class Solution:
    def mySqrt1(self, x: int) -> int:
        for i in range(x // 2 + 3):
            if i * i > x:
                return i - 1
​
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while True:
            mid = (l + r) // 2
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
​
            if mid ** 2 > x:
                r = mid
            else:
                l = mid + 1
​
​
if __name__ == '__main__':
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
​
```