import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        h = sticks
        s = 0
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            heapq.heappush(h, a + b)
            s += a + b
        return s


if __name__ == '__main__':
    assert Solution().connectSticks([2, 4, 3]) == 14
    assert Solution().connectSticks([1, 8, 3, 5]) == 30
