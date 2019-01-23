class Solution:
    def maxSubArray(self, nums):
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


if __name__ == '__main__':
    assert 1 == Solution().maxSubArray([1])
    assert 6 == Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

'''
[-2, 1,-3, 4,-1,2,1,-5,4]
[-2,-1,-4, 0,-1,1,2,-3,1]
'''
