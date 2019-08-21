from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))


if __name__ == '__main__':
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1
