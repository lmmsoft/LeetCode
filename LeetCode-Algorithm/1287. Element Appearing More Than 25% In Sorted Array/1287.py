from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = set()
        intervals = sorted(intervals)
        l = len(intervals)
        for i in range(l):
            for j in range(i + 1, l):
                if intervals[i][1] >= intervals[j][1]:
                    removed.add(j)
        return l - len(removed)


if __name__ == '__main__':
    assert Solution().removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]) == 2
