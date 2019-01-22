class Solution:
    def rotate_kN(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(0, k):
            self.move1(nums)

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return a
        """
        l = len(nums)
        k = k % l
        nums[0: l] = list(reversed(nums))
        nums[0: k] = list(reversed(nums[0: k]))
        nums[k: l] = list(reversed(nums[k: l]))

    def move_k(self, nums):
        end = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = end


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert [5, 6, 7, 1, 2, 3, 4] == nums
