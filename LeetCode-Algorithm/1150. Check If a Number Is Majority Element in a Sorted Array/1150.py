from bisect import bisect_left
from collections import Counter
import math
from typing import List


class Solution:
    def isMajorityElement2(self, nums: List[int], target: int) -> bool:
        cnt = sum(1 for i in nums if target == i)
        return cnt > len(nums) / 2

    def isMajorityElement3(self, nums: List[int], target: int) -> bool:
        return sum(target == i for i in nums) > len(nums) / 2
        # return sum(1 for i in nums if target == i) > len(nums) / 2

    def isMajorityElement4(self, nums: List[int], target: int) -> bool:
        return Counter(nums)[target] > len(nums) / 2

    def isMajorityElement5(self, nums: List[int], target: int) -> bool:
        return nums.count(target) > len(nums) / 2

    # O(log N) solution
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        idx = bisect_left(nums, target)
        times = int(math.floor(len(nums) / 2) + 1)
        return idx + times - 1 < len(nums) and nums[idx + times - 1] == target


if __name__ == '__main__':
    assert Solution().isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5)
    assert not Solution().isMajorityElement([10, 100, 101, 101], target=101)
