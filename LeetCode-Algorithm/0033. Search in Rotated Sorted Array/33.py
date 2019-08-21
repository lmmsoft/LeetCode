from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

    def search2(self, nums, target):
        return nums.index(target) if target in nums else -1


if __name__ == '__main__':
    assert Solution().search(A=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert Solution().search(A=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert Solution().search([1], 0) == -1
    assert Solution().search([3, 1], 1) == 1
    assert Solution().search([8, 9, 2, 3, 4], 9) == 1
