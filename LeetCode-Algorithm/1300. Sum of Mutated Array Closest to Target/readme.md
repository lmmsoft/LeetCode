### [1300\. Sum of Mutated Array Closest to Target](https://leetcode.com/contest/biweekly-contest-16/problems/sum-of-mutated-array-closest-to-target/)
- https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
Difficulty: **Medium**

Given an integer array `arr` and a target value `target`, return the integer `value` such that when we change all the integers larger than `value` in the given array to be equal to `value`, the sum of the array gets as close as possible (in absolute difference) to `target`.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from `arr`.

**Example 1:**

```
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
```

**Example 2:**

```
Input: arr = [2,3,5], target = 10
Output: 5
```

**Example 3:**

```
Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
```

**Constraints:**

*   `1 <= arr.length <= 10^4`
*   `1 <= arr[i], target <= 10^5`

#### Solution

Language: **Python3**
- 题意：给一个数组，选一个数value，数组里所有比value大的数都改成value，希望次数数组的和尽可能接近给定的targer，求数value，如果有两个value打平，返回小的那个
- 我用了三分的思路解，似乎暴力，二分都可以过
- 暴力： max(arr)每次减1直到0，依次求解target，
- 二分：二分value
- 三分，从0到max(arr) 距离target肯定是先减小再增大，每次去掉1/3的区间，最后一个或两个再比较一下就行
- 排序by Lee215
    - https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/Python-Sort-Solution
    - 先排序，每次移除最小的数字，target也减去这个数(因为value比它大，不会对总结果有影响)，把剩下数最大的最小的数乘以len(arr)， 如果超过target则退出循环
    - 退出循环有两个条件，如果数组变成空，则返回max(arr), 如果是找到，则返回，五舍六入，找到最小值

```python3
​
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        mn = 0
        mx = max(arr)
​
        def cal(n):
            return sum(n if a > n else a for a in arr)
​
        while mn + 1 < mx:
            l: int = mn + (mx - mn) // 3
            r: int = mn + (mx - mn) * 2 // 3
            sl = cal(l)
            sr = cal(r)
            if abs(sl - target) <= abs(sr - target):
                # l 接近，淘汰 [r,mx]
                mx = r - 1
            else:
                mn = l + 1
​
        sl = cal(mn)
        sr = cal(mx)
        res =0
        if abs(sl - target) <= abs(sr - target):
            res = mn
        else:
            res = mx
        return res
```