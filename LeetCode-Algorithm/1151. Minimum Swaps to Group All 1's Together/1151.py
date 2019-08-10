from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        cnt = sum(data)
        MAX = m = sum(data[0:cnt])
        for i in range(cnt, len(data)):
            m += data[i] - data[i - cnt]
            MAX = max(MAX, m)
        return cnt - MAX


if __name__ == '__main__':
    assert Solution().minSwaps([1, 0, 1, 0, 1]) == 1
    assert Solution().minSwaps([0, 0, 0, 1, 0]) == 0
    assert Solution().minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]) == 3
