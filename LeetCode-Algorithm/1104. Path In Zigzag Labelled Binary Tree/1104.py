from typing import List
import math


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        height: int = math.floor(math.log(label, 2)) + 1
        # end: list = [2 ** i for i in range(height + 1)]
        res = []
        for i in reversed(range(1, height + 1)):  # height to 1
            # from 2**(i-1) to 2**i+-1

            res.append(label)

            if i % 2 == 1:
                # odd, left to right
                label //= 2
                start = 2 ** (i - 2)
                end = 2 ** (i - 1) - 1
                label = end - label + start

            else:
                start = 2 ** (i - 1)
                end = 2 ** i - 1
                label = end - label + start
                label //= 2
        return list(reversed(res))


if __name__ == '__main__':
    assert Solution().pathInZigZagTree(16) == [1, 3, 4, 15, 16]
    assert Solution().pathInZigZagTree(14) == [1, 3, 4, 14]
    assert Solution().pathInZigZagTree(26) == [1, 2, 6, 10, 26]
