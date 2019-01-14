import bisect


class Solution:
    def searchInsert_brute_forces(self, nums, target) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for id, n in enumerate(nums):
            if n >= target:
                return id

        return len(nums)

    def searchInsert_std_lib(self, nums, target) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)

    def searchInsert(self, nums, target) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l


if __name__ == '__main__':
    assert 2 == Solution().searchInsert([1, 3, 5, 6], 5)
    assert 1 == Solution().searchInsert([1, 3, 5, 6], 2)
    assert 4 == Solution().searchInsert([1, 3, 5, 6], 7)
    assert 0 == Solution().searchInsert([1, 3, 5, 6], 0)

    assert 0 == Solution().searchInsert([1], 1)
