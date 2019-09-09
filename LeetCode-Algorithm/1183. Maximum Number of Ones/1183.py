class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, side: int, maxOnes: int) -> int:  # Soltuion: Fold Matrix

        # Take 7*5, side=3, maxOnes=3 as example:
        # . . .|. . .|.                 1 1 .|1 1 .|1
        # . . .|. . .|. fold  6 4 4     1 . .|1 . .|1
        # . . .|. . .|. ----\ 6 4 4 ==> . . .|. . .|.
        # ------------- ----/ 3 2 2     -------------
        # . . .|. . .|.         ||      1 1 .|1 1 .|1
        # . . .|. . .|.         \/      1 . .|1 . .|1
        #                  6+6+4 = 16

        # Matrix Horizonalize [:] -> [..]
        if width < height:
            width, height = height, width

        # Fold
        x, x0 = divmod(width, side)
        y, y0 = divmod(height, side)
        count = [
            x0 * y0, (side - x0) * y0,
            x0 * (side - y0), (side - x0) * (side - y0)
        ]

        value = [
            (x + 1) * (y + 1), x * (y + 1),
            (x + 1) * y, x * y,
        ]

        # Sum the largest ones
        ans = 0
        for cnt, val in zip(count, value):
            if maxOnes > cnt:
                ans += cnt * val
                maxOnes -= cnt
            else:
                return ans + maxOnes * val
        return ans

    # 二维坐标储存
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        mp = {}
        for i in range(width):
            ii = i % sideLength
            for j in range(height):
                jj = j % sideLength
                k = (ii, jj)  # 对应到sideLength边长正方形里的坐标
                mp[k] = mp.get(k, 0) + 1  # 对应坐标的个数加一
        a = list(mp.values())
        a.sort(reverse=True)
        return sum(a[:maxOnes])  # 最多几个，就最大几个格子的总数

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


if __name__ == '__main__':
    assert Solution().maximumNumberOfOnes(width=3, height=3, sideLength=2, maxOnes=1) == 4
    assert Solution().maximumNumberOfOnes(width=3, height=3, sideLength=2, maxOnes=2) == 6
