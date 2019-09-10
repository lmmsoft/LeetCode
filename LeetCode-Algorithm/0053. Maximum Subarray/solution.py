from typing import List


class Solution:
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        _max = nums[0]
        for n in nums:
            if s < 0:
                s = n
            else:
                s += n
            _max = max(_max, s)
        return _max

    def maxSubArray(self, nums: List[int]) -> int:
        Sum = 0
        Min = float("inf")
        Max = float("-inf")
        for n in nums:
            Min = min(Sum, Min)  # 先把前面的最小值算出来
            Sum += n  # 再计算当前和
            Max = max(Max, Sum - Min)
        return Max


if __name__ == '__main__':
    assert 1 == Solution().maxSubArray([1])
    assert 6 == Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert -1 == Solution().maxSubArray([-1])
    assert 1 == Solution().maxSubArray([1])

'''
[-2, 1,-3, 4,-1,2,1,-5,4]
[-2,-1,-4, 0,-1,1,2,-3,1]
'''
