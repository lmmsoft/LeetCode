### [1130\. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)
- https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
- https://leetcode.com/contest/weekly-contest-146/problems/minimum-cost-tree-from-leaf-values/

Difficulty: **Medium**


Given an array `arr` of positive integers, consider all binary trees such that:

*   Each node has either 0 or 2 children;
*   The values of `arr` correspond to the values of each **leaf** in an in-order traversal of the tree.  _(Recall that a node is a leaf if and only if it has 0 children.)_
*   The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

**Example 1:**

```
Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
```

**Constraints:**

*   `2 <= arr.length <= 40`
*   `1 <= arr[i] <= 15`
*   It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than `2^31`).


#### Solution
- 比赛没什么思路，运气比较好，贪心水过， WA了一次，没看清题意

Language: **Python3**

```python3
from typing import List


class Solution:
    # 我比赛的解法，贪心
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        s = 0
        while len(arr) > 1:
            min_i = -1
            min_v = 100
            for i, a in enumerate(arr):
                if a < min_v:
                    min_i = i
                    min_v = a

            l = len(arr)
            if min_i == 0:
                s += arr[0] * arr[1]
            elif min_i == l - 1:
                s += arr[l - 2] * arr[l - 1]
            else:
                id = min_i - 1 if arr[min_i - 1] < arr[min_i + 1] else min_i + 1
                s += arr[min_i] * arr[id]
            arr.pop(min_i)
        print(s)
        return s

    # Discussion的贪心解法，更简洁
    # Pick up the leaf node with minimum value.
    # Combine it with its inorder neighbor which has smaller value between neighbors.
    # Once we get the new generated non-leaf node, the node with minimum value is useless (For the new generated subtree will be represented with the largest leaf node value.)
    # Repeat it until there is only one node.

    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            mini_idx = arr.index(min(arr))
            if 0 < mini_idx < len(arr) - 1:
                res += min(arr[mini_idx - 1], arr[mini_idx + 1]) * arr[mini_idx]
            else:
                res += arr[1 if mini_idx == 0 else mini_idx - 1] * arr[mini_idx]
            arr.pop(mini_idx)
        return res


if __name__ == '__main__':
    assert Solution().mctFromLeafValues([6, 2, 4]) == 32
    assert Solution().mctFromLeafValues([15, 13, 5, 3, 15]) == 500

​
```