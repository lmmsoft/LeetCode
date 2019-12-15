from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        a = c.most_common(1)
        return a[0][0]


if __name__ == '__main__':
    assert Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
