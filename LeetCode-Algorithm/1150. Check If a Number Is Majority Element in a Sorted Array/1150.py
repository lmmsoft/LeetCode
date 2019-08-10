from typing import List


class Solution:
    def isMajorityElement2(self, nums: List[int], target: int) -> bool:
        cnt = sum(1 for i in nums if target == i)
        return cnt > len(nums) / 2

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return sum(target == i for i in nums) > len(nums) / 2
        # return sum(1 for i in nums if target == i) > len(nums) / 2


if __name__ == '__main__':
    assert Solution().isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5)
    assert not Solution().isMajorityElement([10, 100, 101, 101], target=101)
