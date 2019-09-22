### [1201\. Ugly Number III](https://leetcode.com/contest/weekly-contest-155/problems/ugly-number-iii/)

Difficulty: **Medium**

Write a program to find the `n`-th ugly number.

Ugly numbers are** positive integers** which are divisible by `a` **or** `b` **or** `c`.

**Example 1:**

```
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.```

**Example 2:**

```
Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.
```

**Example 3:**

```
Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
```

**Example 4:**

```
Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
```

**Constraints:**

*   `1 <= n, a, b, c <= 10^9`
*   `1 <= a * b * c <= 10^18`
*   It's guaranteed that the result will be in range `[1, 2 * 10^9]`

#### Solution

Language: **Python3**

```python3
class Solution:
    def gcd(self, a, b):
        x = a % b
        while (x != 0):
            a = b
            b = x
            x = a % b
        return b
​
    def lcm(self, a, b):
        yue = self.gcd(a, b)
        return a * b // yue
​
    def check(self, m, a, b, c):
        ca = m // a
        cb = m // b
        cc = m // c
​
        cab = m // self.lcm(a, b)
        cbc = m // self.lcm(b, c)
        cac = m // self.lcm(a, c)
​
        abc = self.lcm(self.lcm(a, b), c)
        cabc = m // abc
​
        # a + b + c - ab - bc - ac + 2abc
​
        if a != b and b != c:
            return ca + cb + cc - cab - cac - cbc +  cabc
        if a == b == c:
            return ca
        if a == b != c:
            return cb + cc - cbc
        if a != b == c:
            return ca + cb - cab
​
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        if a > b:
            a, b = b, a
        if b > c:
            a, b = b, a
        if a > b:
            a, b = b, a
​
        l, r = 1, a * n + 10
        while l <= r:
            mid = (l + r) // 2
            cnt = self.check(mid, a, b, c)
            if cnt < n:
                l = mid + 1
            elif cnt > n:
                r = mid - 1
            else:
                while True:
                    pre = self.check(mid - 1, a, b, c)
                    if pre < cnt:
                        print(mid)
                        return mid
                    else:
                        mid -= 1
​
​
```