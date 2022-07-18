from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefsum = 0
        d = {0: 1}

        for num in nums:
            prefsum += num

            if prefsum - k in d:
                cnt += d[prefsum - k]

            d[prefsum] = d.get(prefsum, 0) + 1
        return cnt


if __name__ == '__main__':
    assert 2 == Solution().subarraySum(nums=[1, 1, 1], k=2)
    assert 2 == Solution().subarraySum(nums=[1, 2, 3], k=3)
    assert 3 == Solution().subarraySum(nums=[1, 1, 1, 1], k = 2)
