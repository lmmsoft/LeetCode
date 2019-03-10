import heapq
from typing import List


class Solution2:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A)
        for _ in range(K):
            A[0] = -A[0]
            A = sorted(A)
        return sum(A)


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            val = heapq.heappop(A)
            heapq.heappush(A, -val)
        return sum(A)


if __name__ == '__main__':
    print(Solution().largestSumAfterKNegations([4, 2, 3], 1))
    print(Solution().largestSumAfterKNegations([3, -1, 0, 2], 3))
    print(Solution().largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
