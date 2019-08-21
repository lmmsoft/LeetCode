### [922\. Sort Array By Parity IICopy for MarkdownCopy for MarkdownCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/sort-array-by-parity-ii/)

Difficulty: **Easy**


Given an array `A` of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever `A[i]` is odd, `i` is odd; and whenever `A[i]` is even, `i` is even.

You may return any answer array that satisfies this condition.

**Example 1:**

```
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

**Note:**

1.  `2 <= A.length <= 20000`
2.  `A.length % 2 == 0`
3.  `0 <= A[i] <= 1000`


#### Solution
- 双指针的题，虽然简单，但一次通过还是挺开心的，看了下大家代码，自己的基本算是比较优雅的
- 第一个指针找到下一个偶数位不是偶数的数
- 第二个指针找到下一个奇数位不是奇数的数
- 然后交换，寻找下面满足条件的数
- 注意别越界

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        l = len(A)
        while i < l - 1 and j < l:
            while i < l - 1 and A[i] % 2 == 0:
                i += 2
            while j < l and A[j] % 2 == 1:
                j += 2
            if i < l - 1 and j < l:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        return A
​
​
if __name__ == '__main__':
    assert Solution().sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7]
​
```