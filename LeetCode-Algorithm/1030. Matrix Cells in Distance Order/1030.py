from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        d = {}

        for r in range(R):
            for c in range(C):
                dis = abs(r0 - r) + abs(c0 - c)
                # d[r,c] = dis
                d[dis, r, c] = True
        rt = sorted(d)
        ret = [[r, c] for dis, r, c in sorted(d)]
        print(ret)
        return ret


if __name__ == '__main__':
    Solution().allCellsDistOrder(R=1, C=2, r0=0, c0=0)
    Solution().allCellsDistOrder(R=2, C=2, r0=0, c0=1)
    Solution().allCellsDistOrder(R=2, C=3, r0=1, c0=2)
