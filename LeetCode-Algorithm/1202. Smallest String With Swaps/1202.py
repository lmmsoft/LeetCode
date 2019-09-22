from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)

        parents = [x for x in range(0, n + 1)]
        members = [1] * (n + 1)

        def find(x: int) -> int:
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if members[px] < members[py]:
                px, py = py, px
            members[px] += members[py]
            parents[py] = px
            return True

        for fa_id, b in pairs:
            union(fa_id, b)

        d_id = defaultdict(list)
        d_ch = defaultdict(list)
        for i, ch in enumerate(s):
            fa_id = find(i)
            d_id[fa_id].append(i)
            d_ch[fa_id].append(ch)

        res = ['' for _ in range(len(s))]  # 初始化res,保证长度
        for fa_id in d_id.keys():
            ids = sorted(d_id[fa_id])
            chs = sorted(d_ch[fa_id])
            for i, fa_id in enumerate(ids):
                res[fa_id] = chs[i]

        res2 = ''.join(res)
        print(res2)
        return res2


if __name__ == '__main__':
    assert Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]) == 'bacd'
    assert Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]) == 'abcd'
    assert Solution().smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]) == 'abc'
