### [1197\. Minimum Knight Moves](https://leetcode.com/contest/biweekly-contest-9/problems/minimum-knight-moves/)

Difficulty: **Medium**

In an **infinite** chess board with coordinates from `-infinity` to `+infinity`, you have a **knight** at square `[0, 0]`.

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

![](https://assets.leetcode.com/uploads/2018/10/12/knight.png)

Return the minimum number of steps needed to move the knight to the square `[x, y]`.  It is guaranteed the answer exists.

**Example 1:**

```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```

**Example 2:**

```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
```

**Constraints:**

*   `|x| + |y| <= 300`

#### Solution
- 题意：棋盘跳马，从(0,0)到给定点最少多少步
- 方法 BFS
- 一开始没剪枝，总是超时，后来只利用堆成剪枝就过了
- 剪枝策略： 只需要考虑 abs(x), abs(y) 点即可，BFS的时候只需要考虑 x>=-2 and y >=-2的点即可，超过-2走回来不划算，当然我比赛是怕不够，用-20剪枝也过了
- 通项公式
    - rank1 uwi使用的就是O(1)的通向公式
    - 解释可以参考
        - https://stackoverflow.com/questions/2339101/knights-shortest-path-on-chessboard/41704071#41704071
        - https://blog.csdn.net/qq_17550379/article/details/101195668
    

Language: **Python3**

```python3
​
class Solution:
    def minKnightMoves1(self, x: int, y: int) -> int:

        x = abs(x)
        y = abs(y)

        d = {(0, 0): 0}

        l = [(0, 0)]
        ab = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        # step = 0
        if x==0 and y==0:
            return 0
        while True:
            l2 = []
            while l:
                xx, yy = l.pop()
                s = d[(xx, yy)]
                for a, b in ab:
                    aa, bb = xx + a, yy + b
                    if aa == x and bb == y:
                        return s + 1
                    if (aa, bb) not in d:
                        d[(aa, bb)] = s + 1
                        if aa <-20 or bb<-20:
                            continue
                        l2.append((aa, bb))
            l = l2

    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x + y == 1:
            return 3
        res = max(max((x + 1)//2, (y + 1)//2), (x + y + 2)//3)
        res += (res ^ x ^ y) & 1
        return res
```