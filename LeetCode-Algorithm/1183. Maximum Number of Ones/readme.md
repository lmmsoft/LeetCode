### [1183\. Maximum Number of Ones](https://leetcode.com/contest/biweekly-contest-8/problems/maximum-number-of-ones/)
- https://leetcode.com/problems/maximum-number-of-ones/discuss
- https://leetcode.com/contest/biweekly-contest-8/problems/maximum-number-of-ones/

Difficulty: **Hard**

Consider a matrix `M` with dimensions `width * height`, such that every cell has value `0` or `1`, and any **square** sub-matrix of `M` of size `sideLength * sideLength` has at most `maxOnes` ones.

Return the maximum possible number of ones that the matrix `M` can have.

**Example 1:**

```
Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
Output: 4
Explanation:
In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]
```

**Example 2:**

```
Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
Output: 6
Explanation:
[1,0,1]
[1,0,1]
[1,0,1]
```

**Constraints:**

*   `1 <= width, height <= 100`
*   `1 <= sideLength <= width, height`
*   `0 <= maxOnes <= sideLength * sideLength`

#### Solution
- 算是数学题或者规律题
- 要找到规律，放1的时候，在side宽度的正方形里，为了个数最大化，先左上角，然后从相邻的右上往左下依次排布
- 然后求出对应maxOnes时总数最多有多少个1即可
- 我比赛时大概想到了从左上往外排布的最优解，但是下一个应该是[side+side,side]我考虑的是[side+1, side]想复杂了，忘了对称性

Language: **Python3**

```python3
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, side: int, maxOnes: int) -> int:  # Soltuion: Fold Matrix
​
        # Take 7*5, side=3, maxOnes=3 as example:
        # . . .|. . .|.                 1 1 .|1 1 .|1
        # . . .|. . .|. fold  6 4 4     1 . .|1 . .|1
        # . . .|. . .|. ----\ 6 4 4 ==> . . .|. . .|.
        # ------------- ----/ 3 2 2     -------------
        # . . .|. . .|.         ||      1 1 .|1 1 .|1
        # . . .|. . .|.         \/      1 . .|1 . .|1
        #                  6+6+4 = 16
​
        # Matrix Horizonalize [:] -> [..]
        if width < height:
            width, height = height, width
​
        # Fold
        x, x0 = divmod(width, side)
        y, y0 = divmod(height, side)
        count = [
            x0 * y0, (side - x0) * y0,
            x0 * (side - y0), (side - x0) * (side - y0)
        ]
​
        value = [
            (x + 1) * (y + 1), x * (y + 1),
            (x + 1) * y, x * y,
        ]
​
        # Sum the largest ones
        ans = 0
        for cnt, val in zip(count, value):
            if maxOnes > cnt:
                ans += cnt * val
                maxOnes -= cnt
            else:
                return ans + maxOnes * val
        return ans
​
    # 二维坐标储存
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        mp = {}
        for i in range(width):
            ii = i % sideLength
            for j in range(height):
                jj = j % sideLength
                k = (ii, jj)  # 对应到sideLength边长正方形里的坐标
                mp[k] = mp.get(k, 0) + 1  # 对应坐标的个数加一
        a = list(mp.values())
        a.sort(reverse=True)
        return sum(a[:maxOnes])  # 最多几个，就最大几个格子的总数
​
    # 压缩到一维数组
    def maximumNumberOfOnes3(self, C, R, K, maxOnes):
        # every K*K square has at most maxOnes ones
        count = [0] * (K * K)
        for r in range(R):
            for c in range(C):
                code = (r % K) * K + c % K
                count[code] += 1
        count.sort()
        ans = 0
        for _ in range(maxOnes):
            ans += count.pop()
        return ans
​
​
if __name__ == '__main__':
    assert Solution().maximumNumberOfOnes(width=3, height=3, sideLength=2, maxOnes=1) == 4
    assert Solution().maximumNumberOfOnes(width=3, height=3, sideLength=2, maxOnes=2) == 6
​
```