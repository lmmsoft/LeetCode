import bisect


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = bisect.bisect_right(nums, target - 1)
        r = bisect.bisect_right(nums, target)
        if l < r:
            return [l, r - 1]
        return [-1, -1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 7))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 5))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 4))
