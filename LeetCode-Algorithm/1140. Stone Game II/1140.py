from typing import List


class Solution:
    def stoneGameII_1(self, piles: List[int]) -> int:
        L = len(piles)

        d = {}

        # 预处理，后缀和 s[i] = sum(s[i:L])
        s = []
        for num in piles:
            s.append(num)
        for i in range(L - 2, -1, -1):
            s[i] += s[i + 1]

        # 当前从pos开始取, M的只是
        def search(pos: int, M: int):
            nonlocal s
            nonlocal d

            if (pos, M) in d:
                return d[(pos, M)]

            # 可以取到最后一个，那就直接全拿走
            if pos + 2 * M >= L:
                return s[pos]

            # 取不到最后一个，那就每种情况都取一遍M 1 to 2*M，选择最佳值
            b_get_list = []
            for x in range(1, 2 * M + 1):
                a_get_current = s[pos + x] - s[pos]  # 自己这轮拿的数量
                b_get_all = search(pos + x, max(M, x))  # 对方后面拿到的总数
                b_get_list.append(b_get_all)

            # 最佳情况是 让对方后面拿的总数最小，于是自己就最大了
            b_get = min(b_get_list)
            a_get = s[pos] - b_get

            d[(pos, M)] = a_get

            return a_get

        return search(0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        L = len(piles)
        for i in range(L - 2, -1, -1):
            piles[i] += piles[i + 1]

        from functools import lru_cache

        @lru_cache(None)
        def dp(pos, M):
            if pos + 2 * M >= L:
                return piles[pos]

            return piles[pos] - min([dp(pos + x, max(x, M)) for x in range(1, 2 * M + 1)])

        return dp(0, 1)


if __name__ == '__main__':
    # 26, 24,17,8,4
    assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10
