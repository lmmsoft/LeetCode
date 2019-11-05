from itertools import groupby
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = [i % 2 for i in nums]
        # print(l)
        g = [(char, len(list(g))) for char, g in groupby(l)]
        # print(g)

        g2 = []

        for isOdd, size in g:
            if isOdd:
                for _ in range(size):
                    g2.append((1, 1))
            else:
                g2.append((isOdd, size))
        # print(g2)

        oddPos = []
        for id, p in enumerate(g2):
            isOdd, size = p
            if isOdd:
                oddPos.append(id)

        # print(oddPos)

        def getNum(g2, l, r):
            base = 1
            if l - 1 >= 0:
                isOdd, size = g2[l - 1]
                if not isOdd:
                    base *= size + 1
            if r + 1 < len(g2):
                isOdd, size = g2[r + 1]
                if not isOdd:
                    base *= size + 1
            return base

        cnt = 0
        for i in range(0, len(oddPos) - k + 1):
            cnt += getNum(g2, oddPos[i], oddPos[i + k - 1])
        return cnt

    def numberOfSubarrays2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        oddPos = [-1]
        for i, v in enumerate(nums):
            if v & 1:
                oddPos.append(i)
        oddPos.append(len(nums))
        r = 0
        for i in range(1, len(oddPos) - k):
            r += (oddPos[i] - oddPos[i - 1]) * (oddPos[i + k] - oddPos[i + k - 1])
        return r


if __name__ == '__main__':
    assert Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3) == 2
    assert Solution().numberOfSubarrays(nums=[2, 4, 6], k=1) == 0
    assert Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2) == 16
