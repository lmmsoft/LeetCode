import collections
from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        # 相同的值有N个，那么至少要分成n组，那么总数最少KN个才行
        pre = -1
        cnt_max = 0
        cnt_cur = 0
        for n in nums:
            if pre == -1:
                pre = n
                cnt_cur = 1
                continue
            if n == pre:
                cnt_cur += 1
            else:
                pre = n
                cnt_max = max(cnt_max, cnt_cur)
                cnt_cur = 1
        cnt_max = max(cnt_max, cnt_cur)

        if cnt_max * K > len(nums):
            return False
        return True

    def canDivideIntoSubsequences2(self, nums, K: int) -> bool:
        return max(collections.Counter(nums).values()) * K <= len(nums)

    def canDivideIntoSubsequences3(self, nums: List[int], K: int) -> bool:
        return collections.Counter(nums).most_common(1)[0][1] <= (len(nums) // K)


if __name__ == '__main__':
    s = Solution()
    assert s.canDivideIntoSubsequences([1, 2, 2, 3, 3, 4, 4], 3) == True
    assert s.canDivideIntoSubsequences([5, 6, 6, 7, 8], 3) == False
    assert s.canDivideIntoSubsequences([1], 1) == True
    assert s.canDivideIntoSubsequences([1], 2) == False
    assert s.canDivideIntoSubsequences([1, 1, 2, 2], 2) == True
    assert s.canDivideIntoSubsequences([1, 2, 3], 1) == True
    assert s.canDivideIntoSubsequences([5, 5, 5, 5, 5, 5], 6) == False
