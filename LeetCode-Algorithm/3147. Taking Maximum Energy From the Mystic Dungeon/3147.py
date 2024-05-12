import math
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # r = -math.inf
        # l = len(energy)
        # for i, n in enumerate(energy):
        #     total = n
        #     while(i+k<l):
        #         i = i+k
        #         total += energy[i]
        #     if total>r:
        #         r = total
        # return r

        L = len(energy)
        sum_ij = {}  # key = (ii, j), value = sum from ii to j-k
        for ii in range(k):  # 1->k-1
            total = energy[ii]
            j = ii
            sum_ij[(ii, ii)] = total
            while (j + k < L):
                j = j + k
                total += energy[j]
                sum_ij[(ii, j)] = total

        r = -math.inf

        for i, n in enumerate(energy):
            ii = i - (i // k) * k
            end = (L // k) * k + ii
            if end >= L:
                end = end - k
            if end == 9:
                pass
            total_left = sum_ij[(ii, end)]
            total_right = 0
            if i - k >= 0:
                total_right = sum_ij[ii, i - k]
            total = total_left - total_right
            if total > r:
                r = total
        return r


if __name__ == '__main__':
    # assert Solution().maximumEnergy(energy=[5, 2, -10, -5, 1], k=3) == 3
    # assert Solution().maximumEnergy(energy=[-2, -3, -1], k=2) == -1
    assert Solution().maximumEnergy(energy=[5,-10,4,3,5,-9,9,-7], k=2) == 0
