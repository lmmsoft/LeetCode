### [53\. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- https://leetcode.com/problems/maximum-subarray/comments/
- https://leetcode-cn.com/problems/maximum-subarray/comments/

Difficulty: **Easy**


Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(_n_) solution, try coding another solution using the divide and conquer approach, which is more subtle.


#### Solution
- Apparently, this is a optimization problem, which can be usually solved by DP
- https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
- 2019-09-10 更新
    - 原来是dp思路
    - 新的方式是问题转移， 最大子序列 = 总和 - 前面的最小序列，然后递推求当前的[和]与[前面最小序列和]即可

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        _max = nums[0]
        for n in nums:
            if s < 0:
                s = n
            else:
                s += n
            _max = max(_max, s)
        return _max
​
    def maxSubArray(self, nums: List[int]) -> int:
        Sum = 0
        Min = float("inf")
        Max = float("-inf")
        for n in nums:
            Min = min(Sum, Min)  # 先把前面的最小值算出来
            Sum += n  # 再计算当前和
            Max = max(Max, Sum - Min)
        return Max
​
​
if __name__ == '__main__':
    assert 1 == Solution().maxSubArray([1])
    assert 6 == Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert -1 == Solution().maxSubArray([-1])
    assert 1 == Solution().maxSubArray([1])
​
'''
[-2, 1,-3, 4,-1,2,1,-5,4]
[-2,-1,-4, 0,-1,1,2,-3,1]
'''
​
```


```python
Analysis of this problem:
Apparently, this is a optimization problem, which can be usually solved by DP. So when it comes to DP, the first thing for us to figure out is the format of the sub problem(or the state of each sub problem). The format of the sub problem can be helpful when we are trying to come up with the recursive relation.

At first, I think the sub problem should look like: maxSubArray(int A[], int i, int j), which means the maxSubArray for A[i: j]. In this way, our goal is to figure out what maxSubArray(A, 0, A.length - 1) is. However, if we define the format of the sub problem in this way, it's hard to find the connection from the sub problem to the original problem(at least for me). In other words, I can't find a way to divided the original problem into the sub problems and use the solutions of the sub problems to somehow create the solution of the original one.

So I change the format of the sub problem into something like: maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] which must has A[i] as the end element. Note that now the sub problem's format is less flexible and less powerful than the previous one because there's a limitation that A[i] should be contained in that sequence and we have to keep track of each solution of the sub problem to update the global optimal value. However, now the connect between the sub problem & the original one becomes clearer:

maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]; 
And here's the code

public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
        dp[0] = A[0];
        int max = dp[0];
        
        for(int i = 1; i < n; i++){
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(max, dp[i]);
        }
        
        return max;
}
```