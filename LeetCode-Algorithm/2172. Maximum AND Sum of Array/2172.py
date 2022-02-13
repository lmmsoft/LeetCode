from collections import defaultdict
import random
from typing import List


# 神奇的随机算法
# https://leetcode.com/problems/maximum-and-sum-of-array/discuss/1766744/Python-Super-EASY-random-solution-(Just-for-fun)


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ans = 0
        for i in range(1000):  # guess enough times
            random.shuffle(nums)  # try different orders randomly
            cur = 0
            counter = defaultdict(int)
            for n in nums:
                j = 0
                for i in range(1, numSlots + 1):
                    if counter[i] < 2 and n & i > n & j:  # Greedy
                        j = i
                counter[j] += 1
                cur += n & j
            ans = max(ans, cur)

        return ans
