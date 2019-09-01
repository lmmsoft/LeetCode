### [1175\. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/)
- https://leetcode.com/contest/weekly-contest-152/problems/prime-arrangements/
- https://leetcode.com/problems/prime-arrangements/

Difficulty: **Easy**


Return the number of permutations of 1 to `n` so that prime numbers are at prime indices (1-indexed.)

_(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)_

Since the answer may be large, return the answer **modulo `10^9 + 7`**.

**Example 1:**

```
Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
```

**Example 2:**

```
Input: n = 100
Output: 682289015
```

**Constraints:**

*   `1 <= n <= 100`


#### Solution
- 题意 1-n, 质数必须在质数index上(1-base)，求排列数
- 水题，找到1 to N 质数个数p， 质数的排列数是 p! 其余是 (N-p)!
- 看了下速度统计，快的把100以内质数打表了
    - primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
- 慢的就写代码计算质数
- from math import factorial 标准库里的阶乘有优化，比for循环快

Language: **Python3**

```python3
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
​
        def is_prime(n):
            return all(n % j for j in range(2, int(n ** 0.5) + 1)) and n > 1
​
        cnt = 0
        for i in range(1, n + 1):
            if is_prime(i):
                cnt += 1
​
        m = 10 ** 9 + 7
​
        def jc(n):
            s = 1
            for i in range(2, n + 1):
                s *= i
            return s
​
        a = jc(cnt)
        b = jc(n - cnt)
        return a * b % m
​
​
​
```