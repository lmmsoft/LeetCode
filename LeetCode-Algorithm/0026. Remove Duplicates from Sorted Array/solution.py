class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        index = 0
        for x in nums:
            if x != nums[index]:
                index += 1
                nums[index] = x
        print(nums)
        return index + 1


if __name__ == '__main__':
    assert 2 == Solution().removeDuplicates([1, 1, 2])
    assert 5 == Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
