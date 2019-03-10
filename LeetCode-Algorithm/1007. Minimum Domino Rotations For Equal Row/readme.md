# 1007. Minimum Domino Rotations For Equal Row
- https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
- https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row/
- https://leetcode.com/contest/weekly-contest-127/problems/minimum-domino-rotations-for-equal-row/
- https://leetcode-cn.com/contest/weekly-contest-127/problems/minimum-domino-rotations-for-equal-row/

# solution
- 我的解法不是很漂亮，暴力+若干if else判断
    - 对于有两种数字的结果（各一半）
        - 统计 min ( count(a) in A, len(A)- count(a) in A )
    - 对于只有一个可能数字的情况
        - 暴力统计上下两种移动结果， min(up, down)
- 其他解法
    - 解法1: 利用骨牌只可能是1~6，暴力枚举这6种，每种上下，共12种情况
        - 这样代码比较好实现，排名第一就是这么搞的
    - 解法2： 使用python counter库
        - collection.Counter 可以统计成 dict()一样的数据
        - Counter之间可以相加
        - Counter.most_common(n) 取出n个最常见的结果
```python
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = a + b
        m = c.most_common(1)[0]
        if m[1] < n:
            return -1
        cand = m[0]
        ac, bc = 0, 0
        for i in range(n):
            if cand != A[i]:
                if cand != B[i]:
                    return -1
                ac += 1
            elif cand != B[i]:
                bc += 1
        return min(ac, bc)
```
    - 解法3: 其他解法和我看到的差不多 if else讨论