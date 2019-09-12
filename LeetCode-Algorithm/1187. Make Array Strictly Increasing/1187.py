from collections import defaultdict

import bisect
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        pre_dp = {-1: 0}  # pre_dp[i] 表示当前元素为i时所需替换的最小次数
        for cur_num in arr1:
            cur_dp = defaultdict(lambda: float('inf'))
            for pre_num, min_operations in pre_dp.items():
                # 当上一个数小于当前数的时候，当前数不用改变，替换的次数也不用增加
                if pre_num < cur_num:
                    cur_dp[cur_num] = min(cur_dp[cur_num], min_operations)

                # 在arr2里二分查找大于pre_num上一个数的数，对应的数的替换的次数加一，看是否更小
                pos = bisect.bisect_right(arr2, pre_num)
                if pos < len(arr2):
                    cur_dp[arr2[pos]] = min(cur_dp[arr2[pos]], min_operations + 1)
            pre_dp = cur_dp  # 把dp压缩到一维
        return min(pre_dp.values()) if pre_dp else -1


if __name__ == '__main__':
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]) == 1
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]) == 2
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]) == -1
