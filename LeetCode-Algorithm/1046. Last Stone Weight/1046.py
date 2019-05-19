from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones = sorted(stones)
            a = stones.pop()
            b = stones.pop()
            if a != b:
                stones.append(a - b)
        if len(stones):
            return stones[0]
        return 0


if __name__ == '__main__':
    assert 1 == Solution().lastStoneWeight([3, 5, 7])
    assert 0 == Solution().lastStoneWeight([3, 5, 8])
