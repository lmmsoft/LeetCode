### [788\. Rotated Digits](https://leetcode.com/problems/rotated-digits/)

Difficulty: **Easy**


X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number `N`, how many numbers X from `1` to `N` are good?

```
Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
```

**Note:**

*   N  will be in range `[1, 10000]`.


#### Solution

Language: **Python3**

```python3
class Solution:
    def rotatedDigits(self, N: int) -> int:
​
        a = "0182569"
        b = "0185296"
        d = {}
        for aa, bb in zip(a, b):
            d[aa] = bb
​
        def check(i):
            s = str(i)
            s2 = []
            for ch in s:
                if ch in d:
                    s2.append(d[ch])
                else:
                    return 0
            i2 = int(''.join(s2))
            if i2 != i:
                return 1
            return 0
​
        cnt = 0
        for i in range(1, N+1):
            if check(i):
                cnt += 1
        return cnt
```