### [1104\. Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)

Difficulty: **Easy**


In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

![](https://assets.leetcode.com/uploads/2019/06/24/tree.png)

Given the `label` of a node in this tree, return the labels in the path from the root of the tree to the node with that `label`.

**Example 1:**

```
Input: label = 14
Output: [1,3,4,14]
```

**Example 2:**

```
Input: label = 26
Output: [1,2,6,10,26]
```

**Constraints:**

*   `1 <= label <= 10^6`


#### Solution

Language: **Python3**

```python3
from typing import List
import math
​
​
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        height: int = math.floor(math.log(label, 2)) + 1
        # end: list = [2 ** i for i in range(height + 1)]
        res = []
        for i in reversed(range(1, height + 1)):  # height to 1
            # from 2**(i-1) to 2**i+-1
​
            res.append(label)
​
            if i % 2 == 1:
                # odd, left to right
                label //= 2
                start = 2 ** (i - 2)
                end = 2 ** (i - 1) - 1
                label = end - label + start
​
            else:
                start = 2 ** (i - 1)
                end = 2 ** i - 1
                label = end - label + start
                label //= 2
        return list(reversed(res))
​
​
if __name__ == '__main__':
    assert Solution().pathInZigZagTree(16) == [1, 3, 4, 15, 16]
    assert Solution().pathInZigZagTree(14) == [1, 3, 4, 14]
    assert Solution().pathInZigZagTree(26) == [1, 2, 6, 10, 26]
​
```

解释，如果每行都从左向右，那么 根=子/2，这里要注意偶数行是从又向左，转换一下数字即可