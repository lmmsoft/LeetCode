from collections import defaultdict
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l % k != 0:
            return False
        g = l // k
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        for _ in range(g):
            key = min(d.keys())
            for i in range(key, key + k):
                if d[i]:
                    d[i] -= 1
                    if d[i]==0:
                        d.pop(i)
                else:
                    return False
        return True


if __name__ == '__main__':
    assert Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4)
    assert Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)
    assert Solution().isPossibleDivide(nums = [3,3,2,2,1,1], k = 3)
    assert Solution().isPossibleDivide(nums = [1,2,3,4], k = 3)