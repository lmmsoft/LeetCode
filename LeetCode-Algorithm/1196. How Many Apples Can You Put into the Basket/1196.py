from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr = sorted(arr)
        s = 0
        cnt = 0
        for i in arr:
            s += i
            if s > 5000:
                return cnt
            cnt += 1
        return len(arr)


if __name__ == '__main__':
    assert Solution().maxNumberOfApples(arr=[100, 200, 150, 1000]) == 4
    assert Solution().maxNumberOfApples(arr=[900, 950, 800, 1000, 700, 800]) == 5
