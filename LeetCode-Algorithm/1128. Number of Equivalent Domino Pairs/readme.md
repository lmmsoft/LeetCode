### [1128\. Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)
- https://leetcode.com/problems/number-of-equivalent-domino-pairs
- https://leetcode.com/contest/weekly-contest-146/problems/number-of-equivalent-domino-pairs/

Difficulty: **Easy**


Given a list of `dominoes`, `dominoes[i] = [a, b]` is _equivalent_ to `dominoes[j] = [c, d]` if and only if either (`a==c` and `b==d`), or (`a==d` and `b==c`) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs `(i, j)` for which `0 <= i < j < dominoes.length`, and `dominoes[i]` is equivalent to `dominoes[j]`.

**Example 1:**

```
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
```

**Constraints:**

*   `1 <= dominoes.length <= 40000`
*   `1 <= dominoes[i][j] <= 9`


#### Solution
- 题目读懂后不算太难，详见代码中的注释
- 速写可以用
    - Counter()方便计数
    - 用a, b 代替 d[0], d[1]

Language: **Python3**

```python3
from collections import Counter
from typing import List


class Solution:
    # 比赛时候写的算法，比较笨
    # 1: 可以用s= defaultdict(int)来优化默认值
    # 2：总和可以不用组合数，每次增加 s[i]的原始值即可
    def numEquivDominoPairs2(self, dominoes: List[List[int]]) -> int:
        s = {}
        for d in dominoes:
            i = (d[0], d[1]) if d[0] < d[1] else (d[1], d[0])
            if i in s:
                s[i] = s[i] + 1
            else:
                s[i] = 1
        num = 0
        for k, v in s.items():
            if v > 1:
                num += v * (v - 1) // 2
        return int(num)

    # 赛后重写的代码，用Counter来优化defaultdict计数
    # 用a,b 来代替 d[0] d[1], 代码更简练易读
    # 用每次增加，省略组合数相加的过程，也避免浮点数错误
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            ans += c[(a, b)]
            c[(a, b)] += 1
        print(ans)
        return ans


if __name__ == '__main__':
    assert Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
    assert Solution().numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3

```