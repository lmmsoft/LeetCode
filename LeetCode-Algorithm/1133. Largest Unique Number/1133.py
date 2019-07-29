from typing import List
from collections import Counter


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = Counter()
        for a in A:
            c[a] += 1
        res = -1
        for k, v in c.items():
            if v == 1:
                res = max(res, k)
        return res


if __name__ == '__main__':
    assert Solution().largestUniqueNumber([9, 9, 8, 8]) == -1
    assert Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]) == 8
