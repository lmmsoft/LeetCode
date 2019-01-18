class Solution:
    def firstMissingPositive2(self, nums):
        i = 0
        while i != len(nums):
            if 1 <= nums[i] <= len(nums) and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        m = 1
        for i in nums:
            if i == m:
                m += 1
            else:
                break

        return m
