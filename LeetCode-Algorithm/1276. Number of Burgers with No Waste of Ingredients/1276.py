from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = tomatoSlices / 2 - cheeseSlices
        y = cheeseSlices - x
        if x == int(x) and y == int(y) and x>=0 and y>=0:
            return [int(x), int(y)]
        return []


if __name__ == '__main__':
    assert Solution().numOfBurgers(16, 7) == [1, 6]
    assert Solution().numOfBurgers(17, 4) == []
    assert Solution().numOfBurgers(4, 17) == []
    assert Solution().numOfBurgers(0, 0) == [0, 0]
    assert Solution().numOfBurgers(2, 1) == [0, 1]
