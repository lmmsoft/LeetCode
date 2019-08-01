### [1137\. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)
- https://leetcode.com/problems/n-th-tribonacci-number/
- https://leetcode.com/contest/weekly-contest-147/problems/n-th-tribonacci-number/
- https://leetcode.com/contest/weekly-contest-147/submissions/detail/246850654/

Difficulty: **Easy**


The Tribonacci sequence T<sub style="display: inline;">n</sub> is defined as follows: 

T<sub style="display: inline;">0</sub> = 0, T<sub style="display: inline;">1</sub> = 1, T<sub style="display: inline;">2</sub> = 1, and T<sub style="display: inline;">n+3</sub> = T<sub style="display: inline;">n</sub> + T<sub style="display: inline;">n+1</sub> + T<sub style="display: inline;">n+2</sub> for n >= 0.

Given `n`, return the value of T<sub style="display: inline;">n</sub>.

**Example 1:**

```
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

**Example 2:**

```
Input: n = 25
Output: 1389537
```

**Constraints:**

*   `0 <= n <= 37`
*   The answer is guaranteed to fit within a 32-bit integer, ie. `answer <= 2^31 - 1`.


#### Solution
- 水题，我用了数组保存，其实只要三个变量，依次累加即可

Language: **Python3**

```python3
class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1]
        for i in range(3, n+1):
            l.append(l[i - 3] + l[i - 2] + l[i - 1])
        return l[n]
​
    def tribonacci2(self, n):
        a, b, c = 1, 0, 0
        for _ in xrange(n): a, b, c = b, c, a + b + c
        return c​   

if __name__ == '__main__':
    assert Solution().tribonacci(4) == 4
    assert Solution().tribonacci(25) == 1389537
​
```