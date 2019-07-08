from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        s1 = set([0])

        for n in nums:
            s2 = set()
            for item in s1:
                s2.add(item + n)
            s1 = s1.union(s2)
        if (s / 2) in s1:
            return True
        return False


if __name__ == '__main__':
    assert Solution().canPartition([1, 5, 11, 5])
    assert not Solution().canPartition([1, 2, 3, 5])
