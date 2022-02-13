import math
from typing import List


class Solution:

    def minimumRemoval(self, beans: List[int]) -> int:
        # 先排序
        beans = sorted(beans)
        s = sum(beans)
        min_cnt = math.inf
        for idx, target in enumerate(beans):
            cnt = s - target * (len(beans) - idx)
            min_cnt = min(min_cnt, cnt)

        return min_cnt


assert Solution().minimumRemoval([4, 1, 6, 5]) == 4
assert Solution().minimumRemoval([2, 10, 3, 2]) == 7
assert Solution().minimumRemoval([25, 27, 1, 10, 8, 35, 17, 5, 4, 16]) == 68
