class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(0, len(nums)):
            n = index + 1
            if nums[index] == n:  # 数字匹配位置，不用移动
                continue
            elif not self.isvalid(nums[index], nums):  # 数字不合法，置零
                nums[index] = 0
                continue
            else:  # 数字合法，但不在正确位置
                numToMove = nums[index]
                nums[index] = 0
                self.move(numToMove, nums)

        for index in range(0, len(nums)):
            if nums[index] != index + 1:
                return index + 1

        return len(nums) + 1

    # move n to position n-1
    def move(self, numToMove, nums):
        if not self.isvalid(nums[numToMove - 1], nums):  # 目标位置原有数字不合法，直接替换就行
            nums[numToMove - 1] = numToMove
            return
        elif nums[numToMove - 1] == numToMove:
            # 目标位置原有数字合法，但是匹配位置，不需要移动
            return
        else:
            # 目标位置原有数字合法，递归移动
            numToMove2 = nums[numToMove - 1]
            nums[numToMove - 1] = numToMove
            self.move(numToMove2, nums)
            return

    def isvalid(self, numberToCheck, nums):
        if numberToCheck <= 0 or numberToCheck > len(nums):
            return False
        return True


if __name__ == '__main__':
    assert 3 == Solution().firstMissingPositive([1, 2, 0])
    assert 2 == Solution().firstMissingPositive([3, 4, -1, 1])
    assert 1 == Solution().firstMissingPositive([7, 8, 9, 11, 12])

    assert 5 == Solution().firstMissingPositive([4, 3, 2, 1])

    assert 2 == Solution().firstMissingPositive([1, 1])
