import collections
from functools import reduce
from operator import xor

from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a

    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)

    def singleNumber3(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)

    def singleNumber4(self, nums: List[int]) -> int:
        # This can be simpler: reduce(xor, nums) (LeetCode imports operator.xor as xor).
        return reduce(xor, nums)

    def singleNumber5(self, nums: List[int]) -> int:
        # Nice! Here's another one-liner for Python 3, using the walrus operator :=:
        # 解释
        # [x := x ^ v for v in nums] 枚举nums，每个数字和x做xor, 结果放到了[]里，[]的最后一个就是所有数字异或的值
        # (x:=0, ) 上面的x没有初始化，所以用 x:=0 先初始化一下
        # 最后的返回是个元组，结果在元组[1]的最后一个，所以[-1][-1] 或者 [1][-1] 也行
        return (x := 0, [x := x ^ v for v in nums])[-1][-1]

    def singleNumber6(self, nums: List[int]) -> int:
        # 这个不是最优的方法，找到最少的值，输出值(而不是个数)
        return collections.Counter(nums).most_common()[-1][0]


if __name__ == '__main__':
    assert 1 == Solution().singleNumber([2,2,1])