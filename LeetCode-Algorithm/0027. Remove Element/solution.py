class Solution:
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: inti
        """
        index = 0
        for n in nums:
            if n != val:
                nums[index] = n
                index += 1
        return index
