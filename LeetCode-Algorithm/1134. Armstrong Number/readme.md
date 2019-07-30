# 1134. Armstrong Number
User Accepted: 882

User Tried: 888

Total Accepted: 892

Total Submissions: 1064

Difficulty: Easy

The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.
 
```
Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.


Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
```
# Link
- https://leetcode.com/contest/biweekly-contest-5/problems/armstrong-number/
- https://leetcode.com/contest/biweekly-contest-5/submissions/detail/246711778/
- https://leetcode.com/contest/biweekly-contest-5
- https://leetcode.com/contest/biweekly-contest-5/ranking/

# Code
- 这题大家思路都差不多，实现也类似，算法的时候看人品，和代码关系不大

- Best, 24ms 
```python
class Solution:
    def isArmstrong(self, N: int) -> bool:
        num = str(N)
        digits = len(num)
        
        res = 0
        for i in range(len(num)):
            res += int(num[i]) ** digits
        return res == N
```

- My Solution
```python
class Solution:
    def isArmstrong(self, N: int) -> bool:
        s = 0
        k = len(str(N))
        for c in str(N):
            s += (int(c)) ** k

        if s == N:
            return True
        return False


if __name__ == '__main__':
    assert Solution().isArmstrong(153)
    assert not Solution().isArmstrong(123)
```