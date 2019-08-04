from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:

        def cal(nums, isGreater):
            s = 0
            for i in range(0, len(nums) - 1):
                a, b = nums[i], nums[i + 1]
                if isGreater:
                    diff = 0 if a > b else (b - a + 1)
                    nums[i + 1] -= diff
                else:
                    diff = 0 if b > a else (a - b + 1)
                s += diff
                isGreater = not isGreater
            return s

        s1 = cal(nums[:], True)
        s2 = cal(nums[:], False)
        return min(s1, s2)

    def movesToMakeZigzag2(self, nums: List[int]) -> int:
        n = len(nums)
        a = [float("inf")] + nums + [float("inf")]
        evens = sum(max(0, a[i] + 1 - min(a[i - 1], a[i + 1])) for i in range(2, n + 1, 2))
        odds = sum(max(0, a[i] + 1 - min(a[i - 1], a[i + 1])) for i in range(1, n + 1, 2))
        return min(evens, odds)


if __name__ == '__main__':
    assert Solution().movesToMakeZigzag([10, 4, 4, 10, 10, 6, 2, 3]) == 13
    assert Solution().movesToMakeZigzag([2, 7, 10, 9, 8, 9]) == 4
    assert Solution().movesToMakeZigzag([1, 2, 3]) == 2
    assert Solution().movesToMakeZigzag([9, 6, 1, 6, 2]) == 4
