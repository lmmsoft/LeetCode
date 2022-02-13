### [2169\. Count Operations to Obtain Zero](https://leetcode.com/problems/count-operations-to-obtain-zero/)

Difficulty: **Easy**


You are given two **non-negative** integers `num1` and `num2`.

In one **operation**, if `num1 >= num2`, you must subtract `num2` from `num1`, otherwise subtract `num1` from `num2`.

*   For example, if `num1 = 5` and `num2 = 4`, subtract `num2` from `num1`, thus obtaining `num1 = 1` and `num2 = 4`. However, if `num1 = 4` and `num2 = 5`, after one operation, `num1 = 4` and `num2 = 1`.

Return _the **number of operations** required to make either_ `num1 = 0` _or_ `num2 = 0`.

**Example 1:**

```
Input: num1 = 2, num2 = 3
Output: 3
Explanation: 
- Operation 1: num1 = 2, num2 = 3\. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1\. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1\. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1\. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
```

**Example 2:**

```
Input: num1 = 10, num2 = 10
Output: 1
Explanation: 
- Operation 1: num1 = 10, num2 = 10\. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10\. Since num1 == 0, we are done.
So the total number of operations required is 1.
```

**Constraints:**

*   `0 <= num1, num2 <= 10<sup>5</sup>`


#### Solution
- 题意：类似于辗转相减法，直到一个是零，问一共操作多少次
- 解法：模拟即可， 不需要优化或剪枝

Language: **Python3**

```python3
class Solution:
    def foo(self, n1, n2):
        if n1 == 0 or n2 == 0:
            return True, n1, n2
        if n2 > n1:
            return False, n1, n2 - n1
        else:
            return False, n1 - n2, n2
​
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
​
        while True:
            stop, num1, num2 = self.foo(num1, num2)
            if stop:
                break
            cnt += 1
        return cnt
​
```